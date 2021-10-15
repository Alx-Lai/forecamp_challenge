import sys
import base64
import os
import subprocess
branch = subprocess.Popen("git branch", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
branch = branch.decode()
branch = branch.split('\n')
ok = False
for b in branch:
    if '* spice' in b:
        ok = True
if not ok:
    print('seems that you aren\'t on a right branch')
    sys.exit(0)
for file in sys.argv[1:]:
    print('baking:',file,'.....')
    f = open(file, 'r')
    content = f.read()
    f.close()
    f = open(file, 'w')
    content = content.encode()
    content = base64.b64encode(content)
    content = content.decode()
    f.write(content)
    f.close()
if len(sys.argv) < 5:
    sys.exit(0)
output = open('spice', 'a')
for file in sys.argv[1:]:
    print('mixing:',file,'.....')
    f = open(file, 'r')
    content = f.read()
    f.close()
    os.remove(file)
    output.write(content)
output.close()
try:
    os.system('rm ../*')
except:
    pass
os.system('mv spice ..')
