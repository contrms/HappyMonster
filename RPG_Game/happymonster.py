from room import Room
from character import Enemy
from character import Friend
import random
import action
import time

n=0
action.introdution()

#Game is a 3X3 grid

#        Base 3                      Base 10
#    0      1       2            0      1       2
#   _____________________       _____________________
#   |      |       |     |      |      |       |     |
# 0 |  00  |   01  | 02  |   0  |   0  |   1   |  2  |
#   |______|_______|_____|      |______|_______|_____|
#   |      |       |     |      |      |       |     |
# 1 |  10  |   11  | 12  |   1  |   3  |   4   |  5  |
#   |______|_______|_____|      |______|_______|_____|
#   |      |       |     |      |      |       |     |
# 2 |  20  |   21  | 22  |   2  |   6  |   7   |  8  |
#   |______|_______|_____|      |______|_______|_____|


##Create the rooms

roomList = action.createRoomList()

### add descriptions and items to the rooms
while n < 9:
  tdescription=action.get_roomDescription(n)
  roomList[n].set_description(tdescription)
  # also add items to the rooms
  roomList[n].set_has(action.get_roomItems(n))
  n=n+1

### declare the minimum and maximum numbers of friends and enemies
minEnemy=1
maxEnemy=3
minFriend=1
maxFriend=3

characterList = action.createCharacters(minEnemy,maxEnemy,minFriend,maxFriend)

numofCharacters = len(characterList)
# Use a def to determine which rooms will have characters
# returns a list of random intergers in the range 0-8
roomswithCharacters = action.ranSample(9,numofCharacters)

for n in range(len(roomswithCharacters)):
  roomList[roomswithCharacters[n]].set_characterListIndex(n)

# we need to randomly place the items on some characters
# we use our ransample to again select randomly which characters have stuff
# the range is the
hasStuff=action.ranSample(numofCharacters,random.randint(1,numofCharacters-1))
#we then randomly decide which rooms lose stuff
rooms2LoseStuff=action.ranSample(9,len(hasStuff))
### We give the items in the randomly selected rooms to the characters
### and then remove it from the room
for i in range(len(hasStuff)):
      characterList[hasStuff[i]].set_has(roomList[rooms2LoseStuff[i]].get_has())
      roomList[rooms2LoseStuff[i]].set_has(None)




 #code to verify things are working right
for n in range(9):
  roomList[n].describe()
  print (roomList[n].get_has())

for n in range(len(characterList)):
  print (characterList[n].get_name()) #
  print (characterList[n].get_has())
  print (characterList[n].get_wants())




#Now lets get motion going

location=11
life=4
backPack=[]



moveCmdDict = {'north':action.north,'south':action.south,'east':action.east,'west':action.west}
actCmdDict = ['look','?','help', 'done']
characterCmdDict =  ['hug','talk','steal','give']
roomCmds=['search','get']

backpack=[]


while life > 0:
  print ('life: ' ,life)
  new2Backpack=None
  time.sleep(1)
  current_room = roomList[int(str(location),3)]
  current_room.describe()
  action.doorDescribe(location)
  inhabitant_index =  current_room.get_characterListIndex()
  if inhabitant_index is not None:
    inhabitant = characterList[inhabitant_index]
    inhabitant.describe()
  time.sleep(1)
  command = input('enter a command (? for list of commands)>')
  if command in actCmdDict:
    if command =='done':
      action.done
      break
    elif command == 'look':
      continue
    else:
        action.help()

  elif command in moveCmdDict:
   loc=moveCmdDict[command](location)
   if loc != location:
       location = loc
       if inhabitant_index is not None and inhabitant.get_moodindex() > 1:
           inhabitant.set_moodindex(1)
  elif command in characterCmdDict:
    if inhabitant_index is not None:
      if command == 'hug':      inhabitant.hug()
      elif command == 'talk':   inhabitant.talk()
      elif command == 'steal':
        thing=input('what would you like to steal? > ')
        inhabitant.steal(thing)
      else: ###command == 'give':
        thing=input('what would you like to give to ' + inhabitant.get_name()+ '? > ')
        print (inhabitant.get_wants(),thing)
        if thing in backpack:
            if inhabitant.get_wants() == thing:
                backpack.remove(thing)
                monsterhas = inhabitant.give(thing)
                if monsterhas is not None:
                    backpack.append(monsterhas)
            else:
                inhabitant.wrongGive()
        else:
          print( 'You do not have ' + thing + 'in your backpack.')
    else:
        print ('There is nobody in this room!')
  elif command in roomCmds:
    if command =='get' :
      thing=input('what would you like to get? > ')
      if current_room.get_has() == thing:
        new2Backpack=current_room.obtain(thing)
        backpack.append(new2Backpack)
      else:
       print (thing + ' is not in this room.')
    if command =='search':
      thing=input('what would you like to search for? > ')
      if inhabitant_index is not None:
        which=input ('Do you wish to serch '+ inhabitant.get_name() + ' or ' + current_room.get_name() + ' ?')
        if which == inhabitant.get_name():
          inhabitant.search(thing)
          continue
        elif   which != current_room.get_name():
          print ('you can only search' + inhabitant.get.name() + ' or ' + current_room.get_name())
      if current_room.get_has() == thing:
        print ('Yes, it does appear that ' + thing+ ' is in this room!')
      else:
        print ('After a long fruitless search you conclude that ' + thing + ' is not here')
  elif command == 'backpack':
    print ('backpack has ' , backpack)
  else:
    print ('I do not recognize the command')
  time.sleep(1)
  if inhabitant_index is not None:
    if inhabitant.get_attack():
      life=life-1
      inhabitant.reset_attack()
      #print inhabitant.get_attack()
    if inhabitant.get_cede():
      monsterRelingush =  inhabitant.relinquish()
      backpack.append(monsterRelingush)
  happyindex=0
  for monster in characterList:
    happyindex=happyindex + monster.get_moodindex()
  if happyindex == 0:
    print ('You won!  Everyone is happy!')
    break
if life == 0:
    print ('you are Dead')
