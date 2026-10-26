"""Check only package structure/config validity; no download, model inference or claimed experiment."""
from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
required = [
    'PROPOSAL_12GB.md','README.md','AGENTS.md','CODEX_START_PROMPT.md',
    'protocols/H0_HARDWARE_QUALIFICATION.md','protocols/E0_CPU_POLICY_VALIDATION.md',
    'protocols/E1_CHECKPOINT_AUDIT.md','protocols/E2_EDIT_COMPOSITION.md',
    'protocols/E3_REWRITE_LOCALIZATION.md','docs/08_NOVELTY_AUDIT.md',
    'configs/pilot.yaml','configs/canary_policy.yaml','schemas/trial.schema.json',
    'src/earg/canary.py','src/earg/run_e0.py',
]
for item in required:
    assert (ROOT/item).exists(), f'Missing: {item}'
config = yaml.safe_load((ROOT/'configs/pilot.yaml').read_text(encoding='utf-8'))
policy = yaml.safe_load((ROOT/'configs/canary_policy.yaml').read_text(encoding='utf-8'))
schema = json.loads((ROOT/'schemas/trial.schema.json').read_text(encoding='utf-8'))
assert config['experiments']['E0']['positive']==200
assert config['experiments']['E0']['hard_negative']==200
assert config['experiments']['E0']['ordinary_negative']==100
assert config['experiments']['E1']['families']*len(config['experiments']['E1']['intent_variants'])*len(config['experiments']['E1']['paths'])*len(config['sampling']['seeds'])==288
assert config['experiments']['E2']['families']*len(config['experiments']['E2']['image_variants'])*len(config['experiments']['E2']['instruction_variants'])*len(config['sampling']['seeds'])==144
assert config['experiments']['E3']['selected_e1_instances']*len(config['experiments']['E3']['incremental_paths'])*len(config['sampling']['seeds'])==36
assert policy['policy_id']=='EARG_SHAPES_RELATION'
assert 'trial_id' in schema['required']
print(f'PACKAGE OK: {len(required)} required artifacts present; E0=500 E1=288 E2=144 E3_extra=36; policy={policy["policy_id"]}')
