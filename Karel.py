from karel.stanfordkarel import *

def main():
    travel_north()
    if front_is_blocked():
        paint_1st_corner()
    turn_left()
    while front_is_clear():
        move()
    paint_2nd_corner()
    turn_left()
    move_to_wall()
    paint_3rd_corner()
    turn_left()
    for i in range(4):
        move()
    pick_beeper()
    turn_left()
    travel_south()
    turn_right()
    move()
    turn_right()
    move_to_wall()
    turn_left()
    move_to_wall()
    turn_left()
    paint_4th_corner()

'''karel visits the temples in the southern part of India and 
picks up a beeper everytime it rings a bell'''

def travel_south():
    ascend_temple()
    move()
    pick_beeper()
    move()
    turn_right()
    move()
    turn_left()
    descend_temple()

def ascend_temple():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
        move()
        if beepers_present():
            pick_beeper()

def descend_temple():
    while front_is_clear():
        move()
        turn_right()
        move()
        turn_left()
        if beepers_present():
            pick_beeper()
        
'''karel visits the hilly region in the northern part of India and 
picks up a beeper whenever it comes across a monkey'''

def travel_north():
    for i in range(9):
        ascend_hill()
        move()
        descend_hill()
        
def ascend_hill():
    turn_left()
    while right_is_blocked():
        move()
        if beepers_present():
            pick_beeper()
    turn_right()
    
def descend_hill():
    turn_right()
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
    turn_left()
            
'''picking up beepers one by one present at all 4 corners and
painting each one of them a different color using colors of the 
Indian Flag'''

def paint_1st_corner():
    if beepers_present():
        pick_beeper()
    paint_corner('GREEN')
def paint_2nd_corner():
    if beepers_present():
        pick_beeper()
    paint_corner('WHITE')
def paint_3rd_corner():
    if beepers_present():
        pick_beeper()
    paint_corner('ORANGE')
def paint_4th_corner():
    if beepers_present():
        pick_beeper()
    paint_corner('BLUE')
    
#Some important functions

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

#calling main function

if __name__ == '__main__':
    main()
