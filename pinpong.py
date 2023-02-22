from time import time as timer
from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h): 
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(player_image), (self.w, self.h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        pass

speed_x = randint(3, 7)
speed_y = randint(3, 7)

font.init()

pinpong = Ball('pngwing.com.png', 200, 200, 5, 50, 50)
player1 = Player('платформа.png', 0, 0, 5, 30, 120)
player2 = Player('платформа.png', 670, 0, 5, 30, 120)

window = display.set_mode((700, 500))
display.set_caption('Пинпонг')
background = transform.scale(image.load('фон.png'), (700, 500))

font = font.Font(None, 56)

lose1 = font.render('Player 1 lose!', True, (255, 0, 0))
lose2 = font.render('Player 2 lose!', True, (255, 0, 0))

clock = time.Clock()
FPS = 60

finish = False
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False


    if not finish:

        window.blit(background,(0,0))

        pinpong.rect.x += speed_x
        pinpong.rect.y += speed_y

        if pinpong.rect.y > 450:
            speed_y = randint(3, 7)
            speed_y *= -1

        if pinpong.rect.y < 0:
            speed_y = randint(3, 7)


        if sprite.collide_rect(pinpong, player2):
            speed_x = randint(3, 7)
            speed_x *= -1 

        if sprite.collide_rect(pinpong, player1):
            speed_x = randint(3, 7)


        if pinpong.rect.x < 0:
            window.blit(lose1, (200, 200))
            finish = True

        if pinpong.rect.x > 650:
            window.blit(lose2, (200, 200))
            finish = True


        pinpong.update()
        pinpong.reset()

        player1.update_right()
        player1.reset()

        player2.update_left()
        player2.reset()

        display.update()

    clock.tick(FPS)