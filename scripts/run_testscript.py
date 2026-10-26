import subprocess
import sys
for folder in ('tests/api', 'tests/ui'):
    result=subprocess.run([sys.executable,'-m','testscript','check',folder],check=False)
    if result.returncode:
        raise SystemExit(result.returncode)
status=0
for name in ('api','ui'):
    result=subprocess.run([sys.executable,'-m','testscript','run','tests/'+name,'--output','testscript-results/'+name],check=False)
    status=max(status,result.returncode)
raise SystemExit(status)
