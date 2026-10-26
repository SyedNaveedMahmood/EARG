"""CPU-only E0 renderer and manifest writer; does not run any AI model."""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from .canary import generate_scenes, render, violates


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(2**20),b''):h.update(block)
    return h.hexdigest()

def run(out: Path, seed: int=20261026) -> dict:
    if (out/'manifest.jsonl').exists() or (out/'summary.json').exists():
        raise FileExistsError(f'E0 output already exists at {out}; use a new run directory instead of overwriting')
    out.mkdir(parents=True,exist_ok=True)
    images=out/'images'
    images.mkdir(exist_ok=True)
    records=[]
    for scene in generate_scenes(seed):
        path=images/(scene.case_id+'.png')
        render(scene).save(path)
        oracle='positive' if violates(scene) else 'negative'
        records.append({"run_id":f"E0-CPU-{seed}","trial_id":scene.case_id,"stage":"E0","task_family_id":scene.case_id,"policy_id":"EARG_SHAPES_RELATION",
                        "policy_version":"1.0","evaluation_mode":"not_applicable","split":"calibration",
                        "status":"succeeded","case_kind":scene.case_kind,"oracle_label":oracle,"artifact_label":oracle,
                        "scene_graph":scene.asdict(),"image_relpath":str(path.relative_to(out)),"image_sha256":sha256(path),"artifact_sha256":sha256(path)})
    manifest=out/'manifest.jsonl'
    with manifest.open('w',encoding='utf-8') as f:
        for rec in records:f.write(json.dumps(rec,sort_keys=True)+'\n')
    counts=Counter(r['case_kind'] for r in records)
    summary={"stage":"E0","status":"cpu_symbolic_only","seed":seed,"policy_id":"EARG_SHAPES_RELATION",
             "policy_version":"1.0","counts":dict(counts),"n_images":len(records),
             "oracle_disagreements":sum((r['oracle_label']=='positive')!=(r['case_kind']=='positive') for r in records),
             "note":"No VLM, diffusion, GPU or vulnerability evaluation was conducted. Human review pending."}
    (out/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    return summary

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path,default=Path('outputs/e0'))
    ap.add_argument('--seed',type=int,default=20261026)
    args=ap.parse_args()
    print(json.dumps(run(args.out,args.seed),indent=2))

if __name__=='__main__': main()
