# Weronika 17 & 18/08/2020

class Pokemon :
  def __init__(self, name, level, health, max_health, type1, is_knocked_out, experience) :
    self.name = name
    self.level = level
    self.health = health
    self.max_health = max_health
    self.type = type1
    self.is_knocked_out = is_knocked_out
    self.experience = experience

  def lose_health(self, damage):
    self.health -= damage
    print("\nLosing health.\n" + self.name + " now has " + str(self.health) + "health.")

  def gain_health(self, x):
    if (self.health + x >= self.max_health ):
      self.health = self.max_health
    else :
      self.health += x
    print("\nGaining health.\n" + self.name + " now has " + str(self.health) + "health.")

  def knock_out(self):
    self.health = 0
    print("\nKnock out.\n" + self.name + " now has " + str(self.health) + "health.")

  def revive(self) :
    self.health = 100
    print("\nRevival.\n" + self.name + " now has " + str(self.health) + "health.")

  def attack(self, anotherPok):
    if (self.is_knocked_out) :
      print("Pokemon " + self.name + " is knocked out, it won't attack. Choose another pokemon?")
    else:      
      if (self.type == "Fire") :
        if (anotherPok.type == "Fire"):
          damage = anotherPok.level / 2
          anotherPok.lose_health(damage)
          print("\n"+ anotherPok.name +" pokemon received damage of " + str(damage) + ".")
        elif (anotherPok.type == "Water"):
          damage = anotherPok.level / 2
          anotherPok.lose_health(damage)
          print("\n"+ anotherPok.name +" pokemon received damage of " + str(damage) + ".")
        elif (anotherPok.type == "Grass"):
          damage = anotherPok.level * 2
          anotherPok.lose_health(damage)
          print("\n"+ anotherPok.name +" pokemon received damage of " + str(damage) + ".")
      if (self.type == "Water") :
        if (anotherPok.type == "Fire"):
          damage = anotherPok.level * 2
          anotherPok.lose_health(damage)
          print("\n"+ anotherPok.name +" pokemon received damage of " + str(damage) + ".")
        elif (anotherPok.type == "Water"):
          damage = anotherPok.level / 2
          anotherPok.lose_health(damage)
          print("\n"+ anotherPok.name +" pokemon received damage of " + str(damage) + ".")
        elif (anotherPok.type == "Grass"):
          damage = anotherPok.level / 2
          anotherPok.lose_health(damage)
          print("\n"+ anotherPok.name +" pokemon received damage of " + str(damage) + ".")
      if (self.type == "Grass") :
        if (anotherPok.type == "Fire"):
          damage = anotherPok.level / 2
          anotherPok.lose_health(damage)
          print("\n"+ anotherPok.name +" pokemon received damage of " + str(damage) + ".")
        elif (anotherPok.type == "Water"):
          damage = anotherPok.level * 2
          anotherPok.lose_health(damage)
          print("\n"+ anotherPok.name +" pokemon received damage of " + str(damage) + ".")
        elif (anotherPok.type == "Grass"):
          damage = anotherPok.level / 2
          anotherPok.lose_health(damage)
          print("\n"+ anotherPok.name +" pokemon received damage of " + str(damage) + ".")
    self.experience += 1
    if (self.experience < 10):
      self.level = 1
    elif (self.experience < 20):
      self.level = 2
    elif (self.experience < 30):
      self.level = 3
    elif (self.experience < 40):
      self.level = 4
    elif (self.experience < 50):
      self.level = 5
    else :
      self.level = 6
      

class Trainer:
  def __init__(self, pokemons, name, potions, activePok):
    self.pokemons = pokemons
    self.name = name
    self.potions = potions
    self.activePok = activePok
  
  def use_potion(self):
    self.pokemons[self.activePok].health += 10
    print("\nHealth potion used on "+self.pokemons[self.activePok].name+".")
  
  def attack(self, other_trainer):
    their_pokemon=other_trainer.pokemons[other_trainer.activePok]
    self.pokemons[self.activePok].attack(their_pokemon)
    if (self.pokemons[self.activePok].is_knocked_out == False):
      print("\nYour current pokemon just attacked "+ their_pokemon.name +".")
  
  def switch_pokemon(self, newPok):
    if (self.pokemons[newPok].is_knocked_out is True):
      print("\nThe pokemon you are trying to pick is knocked out. Either revive/heal it first or choose another one")      
    else:
      self.activePok = newPok
      print("\nYour new active pokemon is "+self.pokemons[self.activePok].name+".")
        
    

  
pokemon1 = Pokemon("Pokemon1", 1, 70, 100, "Fire", True, 2)
pokemon2 = Pokemon("Pokemon2", 1, 70, 100, "Water", False, 1)
pokemon3 = Pokemon("Pokemon3", 1, 70, 100, "Grass", False, 9)
trainer1 = Trainer([pokemon1, pokemon2, pokemon3], "Trainer1", 3, 0)

pokemon11 = Pokemon("Pokemon11", 3, 80, 100, "Fire", False, 10)
pokemon22 = Pokemon("Pokemon22", 3, 80, 100, "Water", False, 15)
pokemon33 = Pokemon("Pokemon33", 3, 80, 100, "Grass", False, 20)
trainer2 = Trainer([pokemon11, pokemon22, pokemon33], "Trainer2", 6, 2)

# print("\nName: " + pokemon1.name + ", level: " + str(pokemon1.level) +", health: "+ str(pokemon1.health) +", max health: "+ str(pokemon1.max_health) +", type: "+ pokemon1.type +", is knocked out?: "+ str(pokemon1.is_knocked_out) + ".")

# print("\nName: " + pokemon11.name + ", level: " + str(pokemon11.level) +", health: "+ str(pokemon11.health) +", max health: "+ str(pokemon11.max_health) +", type: "+ pokemon11.type +", is knocked out?: "+ str(pokemon11.is_knocked_out) + ".")

# pokemon1.lose_health(10)
#pokemon1.gain_health(100760)
# pokemon1.knock_out()
# pokemon1.revive()
# pokemon1.attack(pokemon11)
#trainer1.attack(trainer2)
# print("\nName: " + pokemon11.name + ", level: " + str(pokemon11.level) +", health: "+ str(pokemon11.health) +", max health: "+ str(pokemon11.max_health) +", type: "+ pokemon11.type +", is knocked out?: "+ str(pokemon11.is_knocked_out) + ".")

# trainer1.use_potion()
# print("\nName: " + pokemon1.name + ", level: " + str(pokemon1.level) +", health: "+ str(pokemon1.health) +", max health: "+ str(pokemon1.max_health) +", type: "+ pokemon1.type +", is knocked out?: "+ str(pokemon1.is_knocked_out) + ".")

# trainer1.switch_pokemon(2)
# print(pokemon3.level)
# trainer1.attack(trainer2)
# print(pokemon3.level)

class Fire(Pokemon):
  def roar(self):
    print("ROAAAAAAAR")

pokemon4 = Fire("Pokemon1", 1, 70, 100, "Fire", True, 2)

pokemon4.roar()






