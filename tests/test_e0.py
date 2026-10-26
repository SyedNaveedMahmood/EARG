import json
from earg.run_e0 import run, sha256


def test_e0_manifest_and_images(tmp_path):
    summary=run(tmp_path/'e0',123)
    assert summary['n_images']==500
    assert summary['oracle_disagreements']==0
    manifest=(tmp_path/'e0'/'manifest.jsonl').read_text().splitlines()
    assert len(manifest)==500
    first=json.loads(manifest[0]); image=tmp_path/'e0'/first['image_relpath']
    assert image.exists()
    assert first['image_sha256']==sha256(image)


def test_seeded_output_hashes(tmp_path):
    a=tmp_path/'a'; b=tmp_path/'b'
    run(a,777);run(b,777)
    aa=[json.loads(x)['image_sha256'] for x in (a/'manifest.jsonl').read_text().splitlines()]
    bb=[json.loads(x)['image_sha256'] for x in (b/'manifest.jsonl').read_text().splitlines()]
    assert aa==bb
