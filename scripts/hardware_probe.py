"""Non-invasive hardware/OS probe. Does not install or download models."""
import json, platform, shutil, subprocess, sys
from datetime import datetime, timezone
report={"utc":datetime.now(timezone.utc).isoformat(),"platform":platform.platform(),"python":sys.version,"nvidia_smi_present":bool(shutil.which('nvidia-smi'))}
if shutil.which('nvidia-smi'):
    p=subprocess.run(['nvidia-smi','--query-gpu=name,memory.total,memory.free,driver_version','--format=csv,noheader,nounits'],capture_output=True,text=True,timeout=20)
    report['nvidia_smi']={"exit_code":p.returncode,"stdout":p.stdout.strip(),"stderr":p.stderr.strip()}
try:
    import torch
    report['torch']={"version":torch.__version__,"cuda_version":torch.version.cuda,"cuda_available":torch.cuda.is_available()}
    if torch.cuda.is_available():report['torch']['device']=torch.cuda.get_device_name(0)
except ImportError:
    report['torch']='not_installed'
print(json.dumps(report,indent=2))
