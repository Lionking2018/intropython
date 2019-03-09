import subprocess
import shutil
import shlex

NOTEBOOKS = ('intro', 'jupyter')

for notebook in NOTEBOOKS:
    src = notebook + '.ipynb'
    dst = notebook + '-custom.ipynb'
    shutil.copy(src, dst)

cmd = 'git checkout -- .'
subprocess.run(shlex.split(cmd))

cmd = 'git pull'
subprocess.run(shlex.split(cmd))
