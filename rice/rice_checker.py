f = open('.rice', 'r')
content = f.read().strip()
f.close()

if content.count('Ri#_}csie73@>G=3)o0d!') == 81922 and len(content)==21*81922:
    print('Look like a bowl of rice!')
else:
    print('Hmmmm... that must be a bad rice!')
