import pgzrun, random

WIDTH = 640
HEIGHT = 480

left_player = Rect(5, 5, 20,50)
right_player = Rect(WIDTH - 25, 5, 20,50)
ball = Rect(WIDTH/2, HEIGHT/2, 10,10)

y_speed = 5
x_speed = 5

def update():
    global y_speed, x_speed

    ball.y += y_speed
    ball.x += x_speed
    if ball.bottom >= HEIGHT or ball.top <= 0:
        y_speed = -1*y_speed
    if ball.right >= WIDTH or ball.left <= 0:
        x_speed = -1*x_speed
    if ball.colliderect(left_player) or ball.colliderect(right_player):
        x_speed = -x_speed
        y_speed += random.randint(-2,2)

    if keyboard.w:
        left_player.y-=5
    elif keyboard.s:
        left_player.y+=5

    if left_player.top<=0:
        left_player.top = 0
    if left_player.bottom>=HEIGHT:
        left_player.bottom = HEIGHT

    right_player.y = ball.y

    if keyboard.UP:
        right_player.y-=5
    elif keyboard.DOWN:
        right_player.y+=5

    if right_player.top<=0:
        right_player.top = 0
    if right_player.bottom>=HEIGHT:
        right_player.bottom = HEIGHT

def draw():
    screen.clear()
    screen.draw.filled_rect(left_player, "white")
    screen.draw.filled_rect(right_player, "white")
    screen.draw.filled_rect(ball, "white")


pgzrun.go()