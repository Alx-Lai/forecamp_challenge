import sys
import base64
import os
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
os.system('rm ../*')
os.system('mv spice ..')
