import random
from replit import clear
import art
from game_data import data

# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },

def compare(n, m):
  if n['follower_count']>m['follower_count']:
    return n
  else:
    return m

def printgame(n, m):
  print(f"Compare A: {n['name']}, {n['description']}, {n['country']}")
  print(art.vs)
  print(f"Against B: {m['name']}, {m['description']}, {m['country']}")

def randomchoice():
  n=random.choice(data)
  return n

def game():
  flag=True
  right=0
  a=randomchoice()
  while flag==True:
    print(art.logo)
    print(f"{right} passed")
    b=randomchoice()
    printgame(a,b)
    
    choice=input("\nWho has more followers 'A' or 'B'?: ")
    if choice=='A':
      choice=a
    else:
      choice=b
    
    big=compare(a,b)

    if choice==big:
      a=b
      right+=1      

    else:
      print(f"You answered right {right} times.")
      return

    clear()

game()