import json
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def test_experiment_counts():
    x=yaml.safe_load((ROOT/'configs/pilot.yaml').read_text())
    n=len(x['sampling']['seeds'])
    assert x['experiments']['E1']['families']*2*2*n==288
    assert x['experiments']['E2']['families']*2*2*n==144
    assert x['experiments']['E3']['selected_e1_instances']*1*n==36


def test_schema_loads():
    s=json.loads((ROOT/'schemas/trial.schema.json').read_text())
    assert s['$schema'].endswith('2020-12/schema')
