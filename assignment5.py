#!/usr/bin/env python

print "You're in a big white room with nothing in it except for two staircases. Staircase 1 goes up and Staircase 2 goes down, which one do you choose? Pick 1 or 2."

stair = raw_input("> ")

if stair == "1":
    print "At the top of the staircase, there's a giant python next to a pile of cash.  What do you do?"
    print "1. Take the money and run."
    print "2. Pet the snake."

    snake = raw_input("> ")


    if snake == "1":
        print "You pissed the snake off. He chases you and eats you. Better luck next time!"
    elif snake == "2":
        print "The snake is your friend now. You get to keep the pile of money.  Good job!"
    else:
        print "Well, doing %s is probably better. The snake goes to sleep." % snake

elif stair == "2":
    print "At the bottom of the staircase, you meet a leprechuan at the end of a rainbow. What do you do next?"
    print "1. Slide down the rainbow with the leprechuan."
    print "2. Run to the end of the rainbow to steal the leprechuan's gold."
    print "3. Ask the leprechuan if he knows the Lucky Charms leprechuan."
  

    leprechuan = raw_input("> ")


    if leprechuan == "1" or leprechuan == "2":
        print "You made it to the end of the rainbow, so you get to keep part of the pot of gold.  Good job!"
    else:
        print "You pissed the leprechuan off. No gold for you. Better luck next time!"

else:
    print "Suddenly a huge monster appears and knocks you down the staircase and you die. Better lucky next time!"