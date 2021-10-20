import os
䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐨳=open
䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م=print
䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋ࠓ=os.remove
import base64
䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋ﶈ=base64.b64encode
import sys
䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𬺜=sys.argv
䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒=sys.exit
try:
 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤=䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐨳('./fat_snake','r')
except:
 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('nothing happen')
 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮=䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.read()
if '7He_Py+h0n_1$_$trooooonG' not in 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮:
 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('nothing happen')
 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
if '--help' in 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𬺜:
 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('-h cut head')
 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('-t cut tail')
 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('-c cut into chunk')
 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
elif '-h' in 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𬺜:
 if 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮=='W0w_7He_Py+h0n_1$_$trooooonG!':
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮='W0w_7He_Py+h0n_1$_$trooooonG'
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.close()
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤=䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐨳('./fat_snake','w')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.write(䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮)
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.close()
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('now you get a headless fat snake')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
 else:
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('nothing happen')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
elif '-t' in 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𬺜:
 if 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮=='W0w_7He_Py+h0n_1$_$trooooonG!':
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('you cut the tail, but the snake bite you and run away')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋ࠓ('fat_snake')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
 elif 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮=='W0w_7He_Py+h0n_1$_$trooooonG':
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮='7He_Py+h0n_1$_$trooooonG'
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.close()
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤=䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐨳('./fat_snake','w')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.write(䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮)
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.close()
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('now you get a processed fat snake, but how can we turn it into small piece of meat?')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
 else:
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('nothing happen')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
elif '-c' in 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𬺜:
 if 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮=='W0w_7He_Py+h0n_1$_$trooooonG!':
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('you hurt it, but the snake bite you and run away')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋ࠓ('fat_snake')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
 elif 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮=='W0w_7He_Py+h0n_1$_$trooooonG':
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('maybe tail is poison')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
 elif 䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮=='7He_Py+h0n_1$_$trooooonG':
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮=䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋ﶈ(䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮.encode())
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮=䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮.decode()
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('there u got the meat')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.close()
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋ࠓ('fat_snake')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤=䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐨳('meat','w')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.write(䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮)
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋餤.close()
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
 else:
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('content',䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋𐦮)
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋م('nothing happen')
  䵎ࢤ𐽅𡘌𨊝𞢊𞤗뵁훋苒(0)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
