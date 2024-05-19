import os
import random
import time

green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
normal = '\033[0m'


def idea_file():
  f = open('my.idea', '+a')

  new_idea = input(
      '\n\nEnter Your idea fast or else it will get off from your head😁😑\n\n----> '
  )

  f.write(f"{new_idea}\n")
  print(green,'\n\nyour idea is recordered in my.idea file',normal)
  print('\n\nsaving...')
  time.sleep(2)
  os.system('clear')
  f.close()
  menu()


def randome_file_idea():
  f = open('my.idea', 'r')
  random_idea = f.read()
  sentence = random_idea.split('\n')#by doing split we have converted string into list
  #in split we have mention \n that means make list based on \n 
  #it means where ever you found a back slash n you have to take it and drop it into [] brackets
  # where every there are \n inculding with the other sring take all and convert it into list
  # you can prefere the image named undertant rmove and split for bettern understanding
  print(blue)
  sentence.remove('')
  radon_sentence = random.choice(sentence)
  os.system('clear')
  for i in range(1, 11):
    print()
    print()
    print()
    print('\033[35m', radon_sentence, '\033[0m')
    print(blue, '\n\nredirecting you to main menu in 10 seconds', normal)
    print(i)
    time.sleep(1)
    os.system('clear')
  menu()
  f.close()


def menu():
  user = input(
      'what you want to do\n\n1. store idea\n\n2. see an random idea?\n\nPress ENTER for exit\n---> '
  )

  if user == '1':
    idea_file()
  elif user == '2':
    randome_file_idea()
  else:
    print('\n\nexiting...')
    time.sleep(2)
    exit()


menu()
