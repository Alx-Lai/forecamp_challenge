import random
Curry_leaf_Token = '1-1ErE_@re_***$tefeN_Curr1***_Leaf'
Turmeric_Token = 'Wh@7_1s_Tur_mer1C]?'
Onion_Token = '0nioN_1$_n0t+union_ouo'
Coriander_seeds_Token = 'vvhaa@aaaAt_u_$ay_U_<3_cor1And3r????'
f = open('curry_leaf', 'w')
f.write(Curry_leaf_Token)
f.close()
f = open('turmeric4129889', 'w')
f.write(Turmeric_Token)
f.close()
f = open('_o__n__i__o______n_', 'w')
f.write(Onion_Token)
f.close()
f = open('816_2cori___a156_23nd16e23r_s1563_813e235e342d434', 'w')
f.write(Coriander_seeds_Token)
f.close()

charactors = '_1234567890abcdfghjklmnopqrstuvwxyz'
# no 'ie' which is be abandoned
def random_write_file(prefix='', length=10, valid=charactors):
    name = prefix+''.join(random.choice(valid) for _ in range(length-len(prefix)))
    f = open(name, 'w')
    f.write(''.join(random.choice(charactors) for _ in range(20)))
    f.close()

for i in range(10):
    random_write_file(prefix='cur', length=10)
for i in range(30):
    random_write_file(prefix='cur', length=20, valid='1234567890abcdfghjklmnopqrstuvwxyz')
for i in range(50):
    random_write_file(prefix='_', length=20, valid='_abcdfghjklmnopqrstuvwxyz')
for i in range(70):
    random_write_file(prefix='', length=40, valid='_1234567890abcdfghjklmnopqrstuvwxyz')
