user1=input("What you will be your 1st move...ROCK/PAPER/SCISSOR : ").lower()
bot1="ROCK".lower()
#1
if user1==bot1:
  print("  DRAW.. \n Player : 0 \n Bot : 0")
#2
  user2=input("What you will be your 2nd move...ROCK/PAPER/SCISSOR : ").lower()
  bot2="PAPER".lower()
  if user2==bot2:
      print("  DRAW.. \n Player : 0 \n Bot : 0")
  if user2=="rock":
      print("  LOSE.. \n Player : 0 \n Bot : 1")
  if user2=="scissor":
      print("  WIN.. \n Player : 1 \n Bot : 0") 
#3
  user3=input("What you will be your 3rd move...ROCK/PAPER/SCISSOR : ").lower()
  bot3="SCISSOR".lower()
  if user3==bot3:
      print("  DRAW.. \n Player : 0 \n Bot : 0")
  if user3=="rock":
      print("  WIN.. \n Player : 1 \n Bot : 1")
  if user3=="paper":
      print("  LOSE.. \n Player : 0 \n Bot : 1") 
#1
if user1=="paper":
  print("  WIN..\n Player : 1 \n Bot : 0")
#2
  user2=input("What you will be your 2nd move...ROCK/PAPER/SCISSOR : ").lower()
  bot2="PAPER".lower()
  if user2==bot2:
      print("  DRAW.. \n Player : 1 \n Bot : 0")
  if user2=="rock":
      print("  LOSE.. \n Player : 1 \n Bot : 1")
  if user2=="scissor":
      print("  WIN.. \n Player : 2 \n Bot : 0")
#3
  user3=input("What you will be your 3rd move...ROCK/PAPER/SCISSOR : ").lower()
  bot3="SCISSOR".lower()
  if user3==bot3:
      print("  DRAW.. \n Player : 1 \n Bot : 0")
  if user3=="rock":
      print("  WIN.. \n Player : 2 \n Bot : 1")
  if user3=="paper":
      print("  LOSE.. \n Player : 1 \n Bot : 1") 
#1
if user1=="scissor":
  print("  LOSE..\n Player : 0 \n Bot : 1 ")

#2
  user2=input("What you will be your 2nd move...ROCK/PAPER/SCISSOR : ").lower()
  bot2="PAPER".lower()
  if user2==bot2:
      print("  DRAW.. \n Player : 0 \n Bot : 1")
  if user2=="rock":
      print("  LOSE.. \n Player : 0 \n Bot : 2")
  if user2=="scissor":
      print("  WIN.. \n Player : 1 \n Bot : 1") 
#3
  user3=input("What you will be your 3rd move...ROCK/PAPER/SCISSOR : ").lower()
  bot3="SCISSOR".lower()
  if user3==bot3:
      print("  DRAW.. \n Player : 0 \n Bot : 1")
  if user3=="rock":
      print("  WIN.. \n Player : 1 \n Bot : 1")
  if user3=="paper":
      print("  LOSE.. \n Player : 0 \n Bot : 2")