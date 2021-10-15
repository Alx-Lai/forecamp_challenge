import os
import base64
import sys

try:
    f = open('./fat_snake', 'r')
except:
    print('nothing happen')
    sys.exit(0)
content = f.read()
if '7He_Py+h0n_1$_$trooooonG' not in content:
    print('nothing happen')
    sys.exit(0)
if '--help' in sys.argv:
    print('-h cut head')
    print('-t cut tail')
    print('-c cut into chunk')
    sys.exit(0)
elif '-h' in sys.argv:
    if content == 'W0w_7He_Py+h0n_1$_$trooooonG!':
        content = 'W0w_7He_Py+h0n_1$_$trooooonG'
        f.close()
        f = open('./fat_snake', 'w')
        f.write(content)
        f.close()
        print('now you get a headless fat snake')
        sys.exit(0)
    else:
        print('nothing happen')
        sys.exit(0)
elif '-t' in sys.argv:
    if content == 'W0w_7He_Py+h0n_1$_$trooooonG!':
        print('you cut the tail, but the snake bite you and run away')
        os.remove('fat_snake')
        sys.exit(0)
    elif content == 'W0w_7He_Py+h0n_1$_$trooooonG':
        content = '7He_Py+h0n_1$_$trooooonG'
        f.close()
        f = open('./fat_snake', 'w')
        f.write(content)
        f.close()
        print('now you get a processed fat snake, but how can we turn it into small piece of meat?')
        sys.exit(0)
    else:
        print('nothing happen')
        sys.exit(0)
elif '-c' in sys.argv:
    if content == 'W0w_7He_Py+h0n_1$_$trooooonG!':
        print('you hurt it, but the snake bite you and run away')
        os.remove('fat_snake')
        sys.exit(0)
    elif content == 'W0w_7He_Py+h0n_1$_$trooooonG':
        print('maybe tail is poison')
        sys.exit(0)
    elif content == '7He_Py+h0n_1$_$trooooonG':
        content = base64.b64encode(content.encode())
        content = content.decode()
        print('there u got the meat')
        f.close()
        os.remove('fat_snake')
        f = open('meat', 'w')
        f.write(content)
        f.close()
        sys.exit(0)
    else:
        print('content',content)
        print('nothing happen')
        sys.exit(0)
    
