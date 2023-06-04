from pygame import *


#Создание окон победы разных игроков
font.init()
font1 = font.Font(None, 80)
win1 = font1.render('BLUE WIN!', True, (0, 0, 255))
win2 = font1.render('RED WIN!', True, (255, 000, 0))

#длина/ширина окна
win_width = 1000
win_height = 500

#переменные картинок
img_back = 'purple.png' #картинка заданего фона
img_ball = 'ball.png' #картинка мячика
img_player1 = 'player1.png' #картинка 1 игрока
img_player2 = 'player2.png' #картинка 2 игрока

#создание окна
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

#название окна
display.set_caption("Ping-Pong")

ball_x = 10
ball_y = 10

#флаги
game_over = False #флаг окончиния цикла
finish = False #флаг окончания игры
win = False #флаг победы одного из игроков

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
    def player_move_two(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 184:
           self.rect.y += self.speed

    def player_move_one(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 184:
           self.rect.y += self.speed
          

#Экземпляры класса
player_one = Player(img_player1,50,100,34,174,10)#игрок 1
player_two = Player(img_player2,910,100,34,174,10)#игрок 2
ball1 = Player(img_ball,450,250,40,40,None)#мячик

#игровой цикл
while not game_over:
    
    for e in event.get():
       if e.type == QUIT:
           game_over = True  
    
    if not win: 
        window.blit(background,(0,0))

        #Отрисовка и управление платфорами
        player_one.player_move_one()
        player_one.reset()

        player_two.player_move_two()
        player_two.reset()

        ball.reset()

        ball.rect.x += ball_x
        ball.rect.y += ball_y


        if ball.rect.y > 460 or ball.rect.y < 0:
            ball_y *= -1

        if ball.rect.colliderect(player_one.rect):
            ball_x *= -1
        
        if ball.rect.colliderect(player_two.rect):
            ball_x *= -1

        
        if ball.rect.x < 30:
            win = True
            window.blit(win1,(370,200))
            
        if ball.rect.x > 940:
            win = True
            window.blit(win2,(370,200))
            
        
        display.update()
    time.delay(50)

