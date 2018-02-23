class Character():

    # Create a character
    def __init__(self, char_name):
        self.name = char_name
        self.description = None
        self.conversation = None
        self.has = None
        self.wants = None
        self.moodindex = 1
        self.mood=['happy','calm','mad','really angry']
        self.attacked=False
        self.cede=False

    def set_description(self, description):
      ### allows the programer to set the description of teh character
        self.description = description

    def describe(self):
    ###prints the character nam, description and mood
        print( self.name + ', ' +self.description + ' is here in the room!' )
        print( self.name + ' appears to be ' + self.mood[self.moodindex])

    def get_name(self):
    ### command returns teh characters name
        return self.name

    def set_has(self,has):
    ### allows the programer to set the item in has
        self.has = has

    def get_has(self):
     ### returns what the character has
        return self.has

    def clear_has(self):
    ### sets what the chracter has to an empty state
        self.has = None

    def reset_attack(self):
    ### sets the attack boolen to False
        self.attacked = False
    def get_attack(self):
    ### returns whether or nor character has attacked
            return self.attacked

    def set_cede(self):
    ### sets the give or cede check to True
        self.cede = True

    def get_cede(self):
    ### returns whether or nor character is giving up what he has
        return self.cede

    def set_wants(self,wants):
     ### allows the programer to set the item the character wants
        self.wants = wants

    def get_wants(self):
        return self.wants

    #set and get the character moode
    def increase_moodindex(self):
     ### increases the charater moode index by 1.  The higher the index
     ### the madder he is.  Also decrease teh likelhood of a succesful interaction
        self.moodindex = self.moodindex + 1

    def set_moodindex(self,moodMod):
    ### returns the word description of teh characters mood
        self.moodindex = moodMod
    def get_mood(self):
    ### prints the mood he charater is in
        print ( self.name + ' seems to be ' + self.mood[self.moodindex] )
    def get_moodindex(self):
     ### returns the mood index setting
        return self.moodindex

    #action defs

    def relinquish(self):
      ### method to transfer item from monster to adventurer
        if self.has is not None:
          handOver = self.has
          self.clear_has()
          self.cede= False
          return handOver
        else:
          self.cede=False
          return None

    def happyCheck(self):
    ### method to check to see if the character is happy
    ### happy characters do not attack are just happy
      if self.has==self.wants or self.moodindex == 0:
        self.moodindex = 0
        print ('I am HAPPY!.  I have my '+ self.wants)
        return True
      else:
        return False

    def hugAct(self,attackp,tellp):
    ### the method for a hug.  Check to see if the character is happy.
    ### then determines if teh monster attacked.  if no attack it then
    #### sends you to a method to determine if he will talk to you
      import action
      import random
      if self.happyCheck():
        return
      #determine if he is going to attack you
      if self.dieRoll(attackp):
        print (self.name + ', ' +self.description + action.assaultGenerator())
        self.set_moodindex(3)
        self.attacked = True
      else:
        #he did not attack but lets see if he wants to tell you something
        print (self.name +  '  says')
        print ('Thanks I need that.')
        self.tell(tellp)
        if self.moodindex < 3 :  self.increase_moodindex()

    def give(self,thing):
    ### allows the adventure to give an items to a charater
    ### if the character has an item he gives it to the adventure
    ### character mood is set to happy
        import action
        monsterhas = None
        if self.has is not None:
            monsterhas = self.has
            self.clear_has()
        print(self.name +  ' eyes tear up with happiness.  He gives you a hug!')
        self.moodindex = 0
        self.has = thing
        if monsterhas is not None:
            print (' here I want to give you my ' + monsterhas)
        return monsterhas



    def wrongGive(self):
    ### Method if adventurer tries to give monster something he does not want
      if self.happyCheck():
        self.happyCheck()
        return
      #determine if he is going to attack you
      if  self.dieRoll(.5):
        print (self.name + ', ' +self.description + action.assaultGenerator())
        self.set_moodindex(3)
        self.attacked = True
      else:
        #he did not attack
        print (self.name +  '  says')
        print ("I don't want that!")
        if self.moodindex < 3 :  self.increase_moodindex()
        print (self.name + ' did not attack you but I would not try giving him the worng item giveagain!')


    def dieRoll(self,prob):
        import random
        if random.random() > prob/self.moodindex:
          return True
        else: False

    def tell(self,prob):
    ### this method has nest loops.  the outer loops is to determine if the monster talks
    ### the next loop dtermines if he is going to talk about what he has or what he wants
    ### the inner loop determines if he talks about what he has or gives it to the adventuer
      import random
      if self.dieRoll(prob):
        if self.dieRoll(prob):
          if self.has is not None:
            if self.dieRoll(prob):
              #print random.random(), prob/self.moodindex
              print (" Here what I have is yours.  Take my " + self.has)
              self.set_cede()
            else:
              print ('Do you like my ' + self.has)
        else:
          print ('Boy , I wish I had a ' + self.wants)
      else:
        print (self.name + ', ' +self.description + ' does not wish to talk right now.')
        print ('I would not push my luck '+ self.name + ' does not look like the talkitive type')

    def searchAct(self,thing,attackp,searchp):
    ### method to determine if a search of a charater was succesful
      import random
      if self.happyCheck():
        self.happyCheck()
        return
      if self.dieRoll(attackp):
        print (self.name + ', ' +self.description + ' beats the snot out of you!')
        self.set_moodindex(3)
        self.attacked=True
      else:
        if self.dieRoll(searchp):
          print ('Boy, you are lucky! ' + self.name + ' does have ' + thing +'.')
          print ('But he was not happy about being searched!')
        else:
          print ('After a brief pat down while ' + self.name + ' growled at you.')
          print ('you are still not certain if ' + self.name + ' has ' + thing + ' or not.')
        if self.moodindex < 3 :  self.increase_moodindex()


    def talkAct(self,attackp,tellp):
      if self.happyCheck():
        self.happyCheck()
        return
      if self.dieRoll(attackp):
        print (self.name + ', ' +self.description + ' beats the snot out of you!')
        self.set_moodindex(3)
        self.attacked=True
      else:
        self.tell(tellp)
        if self.moodindex < 3  :  self.increase_moodindex()

    def stealAct(self,thing,attackp,relingushp):
      import random
      if self.happyCheck():
        return
      if self.has == thing:
        if self.dieRoll(relingushp):
          print ('You are extremely lucky and take ' + self.has)
          self.set_cede()
          if self.moodindex < 3 :  self.increase_moodindex()
          return
        else:
          print (self.name + ' has ' + thing + ' and is not happy that you tried to steal it!')
          if self.moodindex < 3 :  self.increase_moodindex()
      else:
        print (self.name + ' does not have ' + thing + ' and is not happy that you tried to steal from him!')
        if self.moodindex < 2 :  self.increase_moodindex()
      if self.dieRoll(attackp):
          print (self.name + ', ' +self.description + ' beats the snot out of you!')
          self.set_moodindex(3)
          self.attacked=True
      else:
        print (self.name + ' did not attack you but I would not try stealing from him again!')


class Enemy(Character):
  def __init__(self, char_name):
    super().__init__(char_name)
    self.has = None


  def diceRoll(self,prob):
        import random
        if random.random() <  prob/self.moodindex:
          return True
        else:
          False



  def search(self,thing):
    import time
    print ('You are going to search '+ self.description + ' Really?')
    time.sleep(2)
    self.searchAct(thing,.5,.25)


  def steal(self,thing):
    import time
    print ('I would not try stealing from '+ self.description + ' Good Luck!')
    time.sleep(2)
    self.stealAct(thing,.5,.5)

  def hug(self):
    print (self.name + ', ' +self.description + ' does not seem like the hugging type')
    self.hugAct(.5,.25)

  def talk(self):
    print (self.name + ', ' +self.description + ' does not seem like the talkitive type')
    self.talkAct(.75,.5)

class Friend(Character):
  def __init__(self, char_name):
    super().__init__(char_name)
    self.has = None
  def hug(self):
    print (self.name + ', ' +self.description + ' may not like hugging')
    self.hugAct(.9,.5)

  def talk(self):
    print ('talking my not be ' + self.name + '  thing')
    self.talkAct(0.9,.5)

  def steal(self,thing):
    import time
    print ('You are going to steal from '+ self.description + ' Really?')
    time.sleep(2)
    self.stealAct(thing,.25,.25)

  def search(self,thing):
    import time
    print ('You are going to search'+ self.description + ' Really?')
    time.sleep(2)
    self.searchAct(thing,.75,.75)

  def dieRoll(self,prob):
        import random
        if random.random() > prob/self.moodindex:
          return True
        else: False
