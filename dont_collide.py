from p5 import *
from random import randint, seed

# Include global variables here
screen_size = 400
points = 0
lives = 3.0
status = 'RUNNING'
# Draw player function goes here
food_colours = ['#FFFF00']

def draw_player():
    global points, status, lives
    player_on = get(mouse_x, 320).hex
    if player_on == safe.hex or player_on == '#000000':
        text('🐍', mouse_x, 320)
    elif player_on in food_colours : 
        points = points + 1
        text('💖', mouse_x, 320)
    else:
        if points > 0:
            points = points - 1
        elif lives > 0:
            lives = lives - 0.2
        else:
            status = 'GAME_OVER'
        text('💀', mouse_x, 320)



# Draw obstacles function goes here
def draw_obstacles():
    seed(100)
    for i in range(10):
        obstacle_x = randint(0, screen_size)
        obstacle_y = randint(0, screen_size) + frame_count
        obstacle_y = obstacle_y % screen_size
        text('🦅', obstacle_x, obstacle_y)
    
def draw_food():
    seed(50)
    for i in range(2):
        obstacle_x = randint(0, screen_size)
        obstacle_y = randint(0, screen_size) + frame_count
        obstacle_y = obstacle_y % screen_size
        fill(255,255,0)
        no_stroke()
        ellipse(obstacle_x, obstacle_y, screen_size/10, screen_size/10)  # x, y, width, height

def title():
    fill(255,150,0)
    text_size(20)
    text(f'SNAKE Run [{points}]', 20, 30)
    text_size(40)

def draw_lives():
    global lives
    fill(255,0,0)
    emoji_lives=''
    for life in range(int(lives)):
        emoji_lives = emoji_lives + '💖'
    text_size(20)
    text(f'LIVES: {emoji_lives}', 220, 30)

    
def setup():
    # Put code to run once here
    size(screen_size, screen_size)
    text_size(30)
    global points 

def draw():
    # Put code to run every frame here
    global safe, status
    
    safe = Color(0, 100, 50)  # Add the colour of your theme
    background(safe)
    if status == 'RUNNING':
        draw_food()
        draw_obstacles()
        draw_player()
        title()
        draw_lives()
    else:
        title()
        draw_lives()
        text_size(45)
        text('💀 GAME OVER', 20,200 )
# Keep this to run your code
run()
