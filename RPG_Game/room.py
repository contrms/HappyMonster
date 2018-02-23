class Room():
  def __init__(self,room_name):
    self.name = room_name
    self.description = None
    self.linked_rooms= {}
    self.characterListIndex=None
    self.has=None

  def set_characterListIndex(self,index):
    self.characterListIndex = index

  def get_characterListIndex(self):
    return self.characterListIndex

  #set and get what room has
  def set_has(self,has):
     self.has = has
  def get_has(self):
     return self.has

  def set_description(self, room_description):
    self.description = room_description

  def get_description(self):
    return self.description

  def describe(self):
    print ("your are in the", self.name)
    print( self.description )

  def name(self,room_name):
    self.name = room_name

  def get_name(self):
    return self.name

  def link_room(self, room_to_link, direction):
    self.linked_rooms[direction] = room_to_link
    #print( self.name + " linked rooms :" + repr(self.linked_rooms) )

  def get_details(self):
    print ("your are in the", self.name)
    self.describe()
    for direction in self.linked_rooms:
        room = self.linked_rooms[direction]
        print( "The " + room.get_name() + " is " + direction)

  def move(self, direction):
    if direction in self.linked_rooms:
        return self.linked_rooms[direction]
    else:
        print("You can't go that way")
        return self
  def obtain(self,thing):
    thing=thing
    self.set_has(None)
    return thing
