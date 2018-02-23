from character import Enemy
from character import Friend
from room import Room
import random
import itertools

###
###  Room Creation
###

#list of room names
roomNames=('Masterbedroom','Bathroom','Bedroom','Library','Living room','Kitchen','Study','Foyar','Dining room')
#room descriptions in a dictionary
rooms={"Masterbedroom":'large room with a huge bed',
       "Bathroom":'Small room with a bath',
       "Bedroom": 'mall room with a single bed',
       "Library":'large room with a lot of books',
       "Living room":'Large room with a big screen TV',
       "Kitchen":'large room with lots of knifes',
       "Study":'Smaller room with desk and file cabinets',
       "Foyar":'small room with umbrella stand',
       "Dining room":'large room with table and chairs',}

#Dictionary of items
roomItems={"Masterbedroom":'pillow',
       "Bathroom":'toilet brush',
       "Bedroom": 'sheet',
       "Library":'book',
       "Living room":'tv remote',
       "Kitchen":'knife',
       "Study":'file',
       "Foyar":'umbrella',
       "Dining room":'fork'}

###create roomsList with room instances in list
def createRoomList():
  roomList = [Room(name) for name in roomNames]
  return roomList

### returns the list of roomnames
def get_roomName(n):
  return roomNames[n]

### returns the room descripiton of the of theindex in room names
def get_roomDescription(n):
  return rooms[roomNames[n]]

### returns the item of the of the index in room names
def get_roomItems(n):
  return roomItems[roomNames[n]]

####
####character creation
####

characternames=['Noah','Liam','Mason','Jacob','William','Ethan','James','Alexander','Michael','Benjamin']
adjectivesBad=['foul','rotten','vile','disagreeable','obnoxious','disgusting','repulsive','repugnant','distasteful']
adjectivesGood=['nice','kind','kindhearted','benevolent','pleasant','considerate','good','peaceful','warmhearted']
type = ['banshee','ghost','skeleton','mummy','zombie','fairy','orc','gremlin','dragon']
items=['pillow','toilet brush','sheet','book','tv Remote','knife','file','umbrella','fork']
#randomize the list of items
random.shuffle(items)
#every charater wants something.  The goal of the game is to give each charater what he wants
wants =items

#randomize the names
random.shuffle(characternames)
random.shuffle(adjectivesBad)
random.shuffle(adjectivesGood)
random.shuffle(type)

###  creates a list of values from zero up to by not including rlentgh
###  and then returns a random subset or sample of the slist of size rsize
def ranSample(rlentgh,rsize):
  temp=[]
  for i in range(rlentgh):
    temp.append(i)
  return random.sample(temp,rsize)

def createCharacters(minE,maxE,minF,maxF):
  #use random to create 1 to 3 enemies and friends
  numofEnemies = random.randint(minE, maxE)
  numofFriends = random.randint(minF, maxF)
  #create the enemy list
  enemiesList=[]
  for i in range(numofEnemies):
    # create a list with the enemy instances
    enemiesList.append(Enemy(characternames[i]))
    # set the descriptions for the enemies
    tdescription=('a ' + adjectivesBad[i] + " " + type[i])
    enemiesList[i].set_description(tdescription)
    # want list is created in createCharacter.py
    enemiesList[i].set_wants(wants[i])
  #create the friend list
    friendsList=[]
  for i in range(numofFriends):
      #we need to create an index to make sure we do not assin a want that is assigned to an enemy
      j = i + numofEnemies
      # create a list with the enemy instances
      friendsList.append(Friend(characternames[j]))
      # set the descriptions
      tdescription=('a '+ adjectivesGood[j] + " " + type[j])
      friendsList[i].set_description(tdescription)
      # want list is created in createCharacter.py
      friendsList[i].set_wants(wants[j])
  #combine the two lists
  characterList=friendsList+enemiesList
  return characterList



def createFriends(numofFriends,numofEnemies):
  friendsList=[]
  for i in range(numofFriends):
      #we need to create an index to make sure we do not assin a want that is assigned to an enemy
      j = i + numofEnemies
      # create a list with the enemy instances
      friendsList.append(Friend(characternames(j)))
      # set the descriptions
      tdescription=('a '+ adjectivesGood(i) + " " + type(j))
      friendsList[i].set_description(tdescription)
      # want list is created in createCharacter.py
      friendsList[i].set_wants(wants(j))



# def ranSample creates a list of intergers starting at 0 and is the first value long
# it then returns a list of intergers that is a sample or subset of that created list and the lentgh is set by the secon vlue
#in this case we have 9 rooms and we want to place the numoffriends and numof enemies
#randomly in those nine rooms. a sample of the list [0,1,2,3,4,5,6,7,8]
#that is the total number of enenies and friends long will randomly place characters
#in the rooms






def get_charactername(self,index):
  return self.characternames[index]

def get_adjectivesBad(self,index):
  return self.adjectivesBad[index]

def get_adjectivesGood(self, index):
  return self.adjectivesGood[index]

def get_type(self, index):
  return self.type[index]

def get_wants(self,index):
  return self.wants[index]

def get_has(self,index):
  return self.has[index]

def get_item(self,index):
    return self.items[index]


#Game is a 3X3 grid
# we are using base three math since teh rooms are assigned a
# value 0,1,2 for the east west loaction in the first position
# value 0,1,2 for the North south location in the second postion
#
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


def north(loc):
  if loc < 3:
    print('There is not a door to the north')
    return loc
  else:
    newlocation=loc-10
    return newlocation

def south(loc):
    if loc > 19:
      print('There is not a door to the south')
      return loc
    else:
      newlocation=loc+10
      return newlocation

def east(loc):
    if loc % 10 == 2:
      print('There is not a door to the east')
      return loc
    else:
      newlocation=loc+1
      return newlocation

def west(loc):
    if loc % 10 == 0:
      print('There is not a door to the west')
      return loc
    else:
      newlocation=loc-1
    return newlocation



def look():
 return

def introdution():
  fhand = open("readme.txt")
  for n, line in enumerate(fhand):
    if n > 3 and n< 20: print(line)

def hug(self,enemiesList,friendsList,current_room,inhabitant):
    return
def talk(self,current_room,inhabitant):
    return
def steal(self,current_room,inhabitant,item):
    return
def give(self,current_room,inhabitant,item):
    return
def find(self,current_room,inhabitant,item):
    return
def get(self,current_room,inhabitant,item):
    print ('get')
def help():
  print ('For help on a command, enter the command')
  helpthing= input('for a list of commands type list >')
  if helpthing == 'list':
    fhand = open("readme.txt")
    for n, line in enumerate(fhand):
      if n > 21 and n< 49: print(line)
  elif helpthing in helpDict:
    helpcommand(helpthing)
  else:
    print ('I do not recognize the command')


helpDict={'north':(48,51),
          'south':(50,53),
          'east':(54,57),
          'west':(52,55),
          'look':(94,99),
          '?':(101,105),
          'help':(104,108),
          'done':(107,111),
          'hug':(57,63),
          'talk':(62,68),
          'steal':(67,74),
          'give':(73,80),
          'search':(79,85),
          'get':(90,95)}
def helpcommand(cmd):
  fhand = open("readme.txt")
  tulip= helpDict[cmd]
  for n, line in enumerate(fhand):
    if n > tulip[0] and n < tulip[1]: print(line.rstrip())

def done(self):
    print ('I hope you enjoyed the game.')
    return ('break')

#### assault generator

assaultList=(' beats you like a rented mule.',
            ' opens a can of whoop ass and give you a full serving.',
            ' beats you like a red headed step child.',
            ' gets all medieval on your butt.',
            ' delivers you a knuckle sandwich with a side of culiflower ear.',
            ' beats you like you stole something.',
            ' knocks you into next tuesday.',
            ' mops the floor with you and hangs you out to dry.',
            ' beats you like your Daddy should have!',
            ' gives you a huge serving of slap stew.',
            ' beats you so hard your kids will be born dizzy.',
            ' knocks the snot out of you.',
            ' beats the stuffing out of you',
            ' beats the living daylights out of you.',
            ' thrashes you so hard, the good samaritan would have walked past you!',
            ' takes you out to the woodshed.',
            ' beats you black and blue',
            ' does a Chuck Norris on you',
            ' beats you so hard that you look like a Picasso painting!',
            ' beats you so hard that you make roadkill "cute".')

def assaultGenerator():
  return assaultList[random.randint(0,19)]

##### The Doors

doorDict={0: 'There are doors to the east and south.',
          1: 'There are doors to the east ,south and west.',
          2: 'There are doors to the south and west.',
          3: 'There are doors to the north, east and south.',
          4: 'There are doors to the north, east ,south and west.',
          5: 'There are doors to the north ,south and west.',
          6: 'There are doors to the north and east.',
          7: 'There are doors to the north, east and west.',
          8: 'There are doors to the north and west.'}

def doorDescribe(loc):
  print (doorDict[int(str(loc),3)])
