import pygame
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀=True
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓=False
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦤞=print
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𗏓=range
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﮐ=open
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸骧=None
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦹮=abs
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫕜=Exception
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸䌓=pygame.quit
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦿕=pygame.event
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦇔=pygame.font
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𠗫=pygame.time
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ދ=pygame.display
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﱞ=pygame.init
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𑊑=pygame.Rect
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𭹨=pygame.Color
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﭥ=pygame.draw
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸鯬=pygame.locals
from ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸鯬 import*
import time
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐼑=time.Clock
import random
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸졤=random.randint
import imp
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐰐=imp.load_source
import sys
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𭉢=sys.argv
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𪳵=sys.exit
import subprocess
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐡋=subprocess.PIPE
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸椋=subprocess.Popen
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𠆪=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸椋("git branch",shell=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀,stdout=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐡋,stderr=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐡋).communicate()[0]
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𠆪=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𠆪.decode()
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𠆪=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𠆪.split('\n')
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﻹ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
for b in ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𠆪:
 if '* meat' in b:
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﻹ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀
if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﻹ:
 ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦤞('seems that you aren\'t on a right branch')
 ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𪳵(0)
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ=40
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𠝘=(0,0,0)
ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
class ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𘡿:
 def __init__(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐠡):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.parent_screen=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐠡
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x=120
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y=120
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸迸(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ:
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﭥ.circle(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.parent_screen,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𭹨('White'),(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x+20,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y+20),20)
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ཟ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸졤(1,24)*ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸졤(1,19)*ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ
class ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﵸ:
 def __init__(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐠡):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.parent_screen=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐠡
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.direction='down'
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.length=1
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x=[40]
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y=[40]
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ܞ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.direction='left'
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸פֿ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.direction='right'
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞤈(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.direction='up'
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𭿂(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.direction='down'
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸퓔(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  for ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ in ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𗏓(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.length-1,0,-1):
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ]=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ-1]
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ]=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ-1]
  if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.direction=='left':
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x[0]-=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ
  if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.direction=='right':
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x[0]+=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ
  if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.direction=='up':
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y[0]-=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ
  if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.direction=='down':
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y[0]+=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸迸()
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸迸(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ:
   for ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ in ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𗏓(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.length):
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﭥ.rect(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.parent_screen,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𭹨('Yellow'),ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𑊑(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ],ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ],ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ))
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﯥ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.length+=1
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.x.append(-40)
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.y.append(-40)
  if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.length==20:
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ࡎ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﮐ('fat_snake','w')
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ࡎ.write('W0w_7He_Py+h0n_1$_$trooooonG!')
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ࡎ.close()
class ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ፋ:
 def __init__(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞠟,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𥒱):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞠟
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𥒱
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﴖ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  return(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.x[0],ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.y[0]);
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫗾(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  return ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.length
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐡤(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  return ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.direction
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𧺃(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  return(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple.x,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple.y)
class ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸䙳:
 def __init__(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ,argv):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﱞ()
  if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ:
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ދ.set_caption("Codebasics Snake And Apple Game")
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ދ.set_mode((1000,800))
  else:
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸骧
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﵸ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface)
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.draw()
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𘡿(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface)
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple.draw()
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.clock=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𠗫.Clock()
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.Human_control=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀
  if 'snake_hacker' in argv:
   try:
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𢖦=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐰐('',f'./snake_hacker.py')
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.player_ai=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𢖦.TeamAI(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ፋ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple))
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.Human_control=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
   except:
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦤞(f'snake_hacker.py cannot load')
    raise f'snake_hacker.py cannot load'
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦤞('Human_control',ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.Human_control)
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𝚽(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﵸ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface)
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𘡿(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface)
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﶒ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ,x1,y1,x2,y2):
  if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦹮(x1-x2)<ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ and ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦹮(y1-y2)<ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ:
   return ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀
  return ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﷸ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ:
   return
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﭥ.rect(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𭹨('Black'),ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𑊑(0,0,1000,800))
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸탞(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﷸ()
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.walk()
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple.draw()
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣇯()
  if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ:
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ދ.flip()
  for ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ in ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𗏓(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.length):
   if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﶒ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.x[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ],ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.y[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ],ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple.x,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple.y):
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.increase_length()
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.apple.move()
  for ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ in ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𗏓(3,ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.length):
   if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﶒ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.x[0],ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.y[0],ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.x[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ],ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.y[ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᜋ]):
    raise "Collision Occurred"
  if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.x[0]-ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ<0 or ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.x[0]+ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ>1000 or ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.y[0]-ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ<0 or ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.y[0]+ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﹻ>800:
   raise "Hit the boundry error"
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣇯(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ:
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𡵶=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦇔.SysFont('arial',30)
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𑐚=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𡵶.render(f"Score: {self.snake.length}",ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀,(200,200,200))
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface.blit(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𑐚,(850,10))
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﻙ(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﷸ()
  if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ:
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𡵶=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦇔.SysFont('arial',30)
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐫔=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𡵶.render(f"Game is over! Your score is {self.snake.length}",ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀,(255,255,255))
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦤞(f"Game is over! Your score is {self.snake.length}")
   if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.length>=20:
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ࡎ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﮐ('fat_snake','w')
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ࡎ.write('W0w_7He_Py+h0n_1$_$trooooonG!')
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ࡎ.close()
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface.blit(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐫔,(200,300))
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐣩=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𡵶.render("To play again press Enter. To exit press Escape!",ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀,(255,255,255))
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦤞("To play again press Enter. To exit press Escape!")
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.surface.blit(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐣩,(200,350))
   ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ދ.flip()
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦤞(f"Game is over! Your score is {self.snake.length}")
  '''
        if self.snake.length >= 20:
            f = open('fat_snake', 'w')
            f.write('W0w_7He_Py+h0n_1$_$trooooonG!')
            f.close()
        '''  
 def ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐤷(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ):
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫷿=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ڽ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
  if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.Human_control:
   while ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫷿:
    for ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸趰 in ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𦿕.get():
     if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸趰.type==KEYDOWN:
      if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸趰.key==K_ESCAPE:
       ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫷿=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
       ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ދ.quit()
       ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸䌓()
      if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸趰.key==K_RETURN:
       ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ڽ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
      if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ڽ:
       if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸趰.key==K_LEFT and ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.direction!='right':
        ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.move_left()
       if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸趰.key==K_RIGHT and ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.direction!='left':
        ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.move_right()
       if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸趰.key==K_UP and ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.direction!='down':
        ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.move_up()
       if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸趰.key==K_DOWN and ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.direction!='up':
        ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.move_down()
     elif ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸趰.type==QUIT:
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫷿=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ދ.quit()
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸䌓()
    try:
     if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ڽ:
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸탞()
    except ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫕜 as e:
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﻙ()
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ڽ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𝚽()
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.clock.tick(30)
  else:
   while ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫷿:
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞤒=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.player_ai.decide()
    if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞤒=='esc':
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫷿=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
     if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ:
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ދ.quit()
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸䌓()
    if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞤒=='return':
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ڽ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
    if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ڽ:
     if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞤒=='left' and ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.direction!='right':
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.move_left()
     if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞤒=='right' and ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.direction!='left':
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.move_right()
     if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞤒=='up' and ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.direction!='down':
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.move_up()
     if ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𞤒=='down' and ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.direction!='up':
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.snake.move_down()
    try:
     if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ڽ:
      ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸탞()
    except ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫕜 as e:
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ﻙ()
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𫷿=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𣊓
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𝚽()
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ｽ.clock.tick(30)
   else:
    if not ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ:
     ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ދ.quit()
    ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸䌓()
if __name__=='__main__':
 if '-n' in ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𭉢:
  ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸ᵳ=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐦀
 ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐳮=ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸䙳(ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𭉢)
 ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐳮.ﺌﲳ綍𡴁ﲓ햻푟𒋈蔸𐤷()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
