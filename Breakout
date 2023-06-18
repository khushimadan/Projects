from graphics import Canvas
import time

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600
PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 10
BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH-BRICK_GAP*9) / 10
BRICK_HEIGHT = 10

def main():
    canvas = Canvas(CANVAS_WIDTH,CANVAS_HEIGHT)
    
    #creating all the bricks on canvas
    start_x=0
    start_y=50
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'red')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    start_y+=BRICK_HEIGHT+BRICK_GAP
    start_x=0
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'red')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    start_x=0
    start_y+=BRICK_HEIGHT+BRICK_GAP
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'orange')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    start_y+=BRICK_HEIGHT+BRICK_GAP
    start_x=0
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'orange')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    start_x=0
    start_y+=BRICK_HEIGHT+BRICK_GAP
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'yellow')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    start_y+=BRICK_HEIGHT+BRICK_GAP
    start_x=0
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'yellow')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    start_x=0
    start_y+=BRICK_HEIGHT+BRICK_GAP
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'green')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    start_y+=BRICK_HEIGHT+BRICK_GAP
    start_x=0
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'green')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    start_x=0
    start_y+=BRICK_HEIGHT+BRICK_GAP
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'blue')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    start_y+=BRICK_HEIGHT+BRICK_GAP
    start_x=0
    for i in range(10):
        brick=canvas.create_rectangle(start_x,start_y,start_x+BRICK_WIDTH,start_y+BRICK_HEIGHT,'blue')
        start_x=start_x+BRICK_WIDTH+BRICK_GAP
    paddle_x=CANVAS_WIDTH/2-PADDLE_WIDTH/2
    paddle=canvas.create_rectangle(paddle_x,PADDLE_Y,paddle_x+PADDLE_WIDTH,PADDLE_Y+PADDLE_HEIGHT,'black')
    
    #adding a ball
    BALL_RADIUS = 10
    start_x=CANVAS_WIDTH/2-BALL_RADIUS
    start_y=CANVAS_HEIGHT/2-BALL_RADIUS
    ball=canvas.create_oval(start_x,start_y,start_x+BALL_RADIUS*2,start_y+BALL_RADIUS*2,'blue')
    change_x=10
    change_y=10
    DELAY=0.001
    count=0
    total_bricks=100
    points=0
    points_text=canvas.create_text(10,15,text=str(points)+' POINTS',font_size=15,color='black')
    #playing game
    while True:
        start_x+=change_x
        start_y+=change_y
        canvas.moveto(ball,start_x,start_y)
        if start_y>=CANVAS_HEIGHT:
            if count!=3:
                count+=1
                start_x=CANVAS_WIDTH/2-BALL_RADIUS
                start_y=CANVAS_HEIGHT/2-BALL_RADIUS
                canvas.moveto(ball,start_x,start_y)
        if count==3: #ending game after user hits bottom wall 3 times!
            canvas.clear()
            text=canvas.create_text(CANVAS_WIDTH/2-80,CANVAS_HEIGHT/2-20,text="GAME OVER!",font_size=25,color='magenta')
            text1=canvas.create_text(CANVAS_WIDTH/2-45,CANVAS_HEIGHT/2+15,text="POINTS: "+str(points),font_size=15,color='blue')
            break
        change_x,change_y=bouncing(canvas,start_x,start_y,change_x,change_y)
        mouse_x=canvas.get_mouse_x() #getting mouse's x coordinate
        canvas.moveto(paddle,mouse_x-PADDLE_WIDTH/2,PADDLE_Y) #moving paddle along with the mouse
        colliding_list=canvas.find_overlapping(start_x,start_y,start_x+BALL_RADIUS*2,start_y+BALL_RADIUS*2) #list of objects colliding with the ball
        if colliding_list!=['shape_101']: #shape_101 is the ball and checking if the list contains anything except the ball
            if 'shape_100' in colliding_list: #if ball hits the paddle
                change_y=-change_y #bounce upwards
                canvas.moveto(ball,start_x+change_x,start_y+change_y) 
            else:
                for i in colliding_list: #if the ball hits a brick
                    if i!='shape_101':
                        total_bricks-=1 #keeping track of number of bricks left
                        canvas.delete(i) #removing the brick from the canvas
                        points+=20
                        canvas.change_text(points_text,str(points)+' POINTS')
                        if total_bricks==0: #if ball hits the last brick, end the game
                            canvas.clear()
                            text=canvas.create_text(CANVAS_WIDTH/2-200,CANVAS_HEIGHT/2-20,text="CONGRATULATIONS! YOU WON",font_size=25,color='magenta')
                            break
                        #increasing speed after hitting 20 bricks
                        if total_bricks<=80 and total_bricks>60:
                            DELAY-=0.0002
                        if total_bricks<=60 and total_bricks>40:
                            DELAY-=0.0002
                        if total_bricks<=40:
                            DELAY-=0.0002
                change_y=-change_y
                canvas.moveto(ball,start_x+change_x,start_y+change_y)
        time.sleep(DELAY)
        
#bouncing the ball off the 3 walls
def bouncing(canvas,start_x,start_y,change_x,change_y):
    if start_x<=0 or start_x>=CANVAS_WIDTH:
        change_x=-change_x
    if start_y<=0:
        change_y=-change_y
    return change_x,change_y
    
if __name__ == '__main__':
    main()
