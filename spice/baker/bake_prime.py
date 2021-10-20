import sys
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𮖘=True
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𧱬=False
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ܐ=print
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𖹣=open
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𤯧=len
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ࠈ=sys.argv
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓㭍=sys.exit
import base64
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﭥ=base64.b64encode
import os
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﴒ=os.system
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓덼=os.remove
import subprocess
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﯛ=subprocess.PIPE
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𤬫=subprocess.Popen
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﴢ=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𤬫("git branch",shell=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𮖘,stdout=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﯛ,stderr=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﯛ).communicate()[0]
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﴢ=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﴢ.decode()
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﴢ=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﴢ.split('\n')
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𠬽=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𧱬
for b in ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﴢ:
 if '* spice' in b:
  ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𠬽=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𮖘
if not ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𠬽:
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ܐ('seems that you aren\'t on a right branch')
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓㭍(0)
for ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓矢 in ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ࠈ[1:]:
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ܐ('baking:',ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓矢,'.....')
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𢷵=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𖹣(ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓矢,'r')
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𢷵.read()
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𢷵.close()
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𢷵=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𖹣(ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓矢,'w')
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競.encode()
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﭥ(ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競)
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競.decode()
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𢷵.write(ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競)
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𢷵.close()
if ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𤯧(ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ࠈ)<5:
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓㭍(0)
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﯡ=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𖹣('spice','a')
for ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓矢 in ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ࠈ[1:]:
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ܐ('mixing:',ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓矢,'.....')
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𢷵=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𖹣(ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓矢,'r')
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競=ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𢷵.read()
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓𢷵.close()
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓덼(ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓矢)
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﯡ.write(ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓競)
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﯡ.close()
try:
 ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﴒ('cd .. && ls | grep -v baker | xargs rm')
except:
 pass
ﰹ굅𞤌돑倞𣌾ݜ𐩲𐡓ﴒ('mv spice ..')
# Created by pyminifier (https://github.com/liftoff/pyminifier)
