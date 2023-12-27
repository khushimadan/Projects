from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1

def main():
    POINTS=0
    DELAY = 0.1
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player_start_x=0
    player_start_y=0
    player=canvas.create_rectangle(player_start_x,player_start_y,player_start_x+SIZE,player_start_y+SIZE,'blue')
    goal_start_x=360
    goal_start_y=360
    goal=canvas.create_rectangle(goal_start_x,goal_start_y,goal_start_x+SIZE,goal_start_y+SIZE,'red')
    direction='right'
    points_text=canvas.create_text(10,380,text=str(POINTS)+' POINTS',color='green')
    while True:
        key=canvas.get_last_key_press() #getting the last key pressed by the user
        if key=='ArrowLeft':
            direction='left'
        if key=='ArrowRight':
            direction='right'
        if key=='ArrowUp':
            direction='up'
        if key=='ArrowDown':
            direction='down'
        if direction=='right':
            player_start_x+=SIZE
        if direction=='left':
            player_start_x-=SIZE
        if direction=='up':
            player_start_y-=SIZE
        if direction=='down':
            player_start_y+=SIZE
        #getting coordinates of the player (blue square)
        x=canvas.get_left_x(player)
        y=canvas.get_top_y(player)
        canvas.moveto(player,player_start_x,player_start_y)
        
        #ending the game if user touches the boundary
        if x<0 or x>CANVAS_WIDTH:
            canvas.clear()
            game_over_text=canvas.create_text(CANVAS_WIDTH/2-80,CANVAS_HEIGHT/2-20,font_size=25,text='GAME OVER!',color='magenta')
            score_text=canvas.create_text(CANVAS_WIDTH/2-60,CANVAS_HEIGHT/2+10,font_size=15,text='YOUR SCORE: '+str(POINTS),color='blue')
            break
        if y<0 or y>CANVAS_HEIGHT:
            canvas.clear()
            game_over_text=canvas.create_text(CANVAS_WIDTH/2-80,CANVAS_HEIGHT/2-20,font_size=25,text='GAME OVER!',color='magenta')
            score_text=canvas.create_text(CANVAS_WIDTH/2-60,CANVAS_HEIGHT/2+10,font_size=15,text='YOUR SCORE: '+str(POINTS),color='blue')
            break
        
        # checking if the player hit the goal
        objs=canvas.find_overlapping(player_start_x,player_start_y,player_start_x+SIZE,player_start_y+SIZE)
        if objs!=['shape_0']:
            goal_start_x=random.randrange(20,380,20) #generating a goal at a random position
            goal_start_y=random.randrange(20,380,20)
            canvas.moveto(goal,goal_start_x,goal_start_y)
            DELAY-=0.005 #increasing speed after every goal
            POINTS+=1
            canvas.change_text(points_text,str(POINTS)+' POINTS')
            
        time.sleep(DELAY)
        
if __name__ == '__main__':
    main()
