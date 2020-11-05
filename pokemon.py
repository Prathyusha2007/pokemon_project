#By Prathyusha Theerdhala
import random
from time import sleep
choice=["Charmander","Bulbasaur","Squirtle"]
cpu=random.choices(choice)
player=False
while player ==False:
  print("Welcome to the Pokémon Battleground!")
  print("\nAre you ready to choose your Pokémon?")
  player=str(input("Which Pokémon do you want to choose?\nCharmander\nSquirtle \nBulbasur \nStop"))
  print("The computer chose its Pokémon")
  if player==cpu:
    print("\nPlease wait...You will be able to see your result in a few seconds...")
    sleep(2)
    print("Tie!")
  elif player=="Charmander":
    if cpu=="Squirtle":
      print("\nPlease wait...You will be able to see your result in a few seconds...")
      sleep(2)
      print("Sorry!You lost!")
    else:
      print("\nPlease wait...You will be able to see your result in a few seconds...")
      sleep(2)
      print("You win!")
  elif player=="Squirtle":
    if cpu=="Bulbasur":
      print("\nPlease wait...You will be able to see your result in a few seconds...")
      sleep(2)
      print("Sorry!You lost!")
    else:
      print("\nPlease wait...You will be able to see your result in a few seconds...")
      sleep(2)
      print("You win!")
  elif player=="Bulbasur":
    if cpu=="Charmander":
      print("\nPlease wait...You will be able to see your result in a few seconds...")
      sleep(2)
      print("Sorry!You lost!")
    else:
      print("\nPlease wait...You will be able to see your result in a few seconds...")
      sleep(2)
      print("You win!")
  elif player =="Stop":
    print("Thank you for playing!")
    break
  else:
    print("That's not a valid play!")
player=False  
