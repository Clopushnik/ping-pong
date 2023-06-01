from pygame import *


#длина/ширина окна
win_width = 1000
win_height = 500

#переменные картинок
img_back = 'purple.png' #картинка заданего фона
img_ball = 'ball.png' #картинка мячика

#название окна
display.set_caption("Ping-Pong")

#создание окна
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

#флаг окончиния цикла
game_over = False 

#класс игрока 
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
 
 
       
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
 
       
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
 

class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed

class Ball():
    pass

#Экземпляры класса
#player_one = Player()#игрок 1
#player_two = Player()#игрок 2
#ball = Ball()#мячик

#мгровой цикл
while not game_over:
    window.blit(background,(0,0))
    display.update()

time.delay(50)