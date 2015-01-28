#!/usr/bin/env python

sally = 4
sam = 10
susan = 5
apple_total = 30

apples_picked = apple_total - ( sally + sam + susan )

print "Last weekend, Sally, Sam, and Susan went to an apple orchard to pick apples."
print "Sally picked" , sally , "apples, Sam picked" ,  sam , "apples, and Susan picked" , susan , "apples." 
print "Together, Sally, Sam, and Susan picked" ,  apple_total , "apples at the orchard."


tim = 100

print "Today, Tim visited the apple orchard and picked %d apples." % tim
print "Tim picked" , tim / sam , "times more apples than Sam," , tim / susan , "times more apples than Susan, and" , tim / sally , "times more apples than Sally."
print "Tim picked more than" , apple_total * 3 , "apples, which is three times the total number of apples that Sally, Sam, and Susan picked."
print "After Tim picked apples, the new total number of apples was" , apples_picked + tim , "."
print "The girls picked" , ( apple_total + tim ) - ( sally + susan ) , "fewer apples than the boys."







