import random
def random_str(length):
    return ''.join(random.choice('0123456789!@#$%^&*.\'"') for _ in range(length))
f = open('.rice', 'w')
f.write(random_str(10)+'['+'Ri#_}csie73@>G=3)o0d!'*20+']'+random_str(10))
f.close()