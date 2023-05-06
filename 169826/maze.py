from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed=player_speed

        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys= key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -=self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x +=self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y +=self.speed

class Enemy(GameSprite):
    naprav='left'
    def update(self):
        if self.rect.x <=win_width - 230:
            self.naprav='right'
        if self.rect.x >= win_width - 85:
            self.naprav='left'
        if self.naprav == 'left':
            self.rect.x-=self.speed
        if self.naprav == 'right':
            self.rect.x+=self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1=color_1
        self.color_2=color_2
        self.color_3=color_3

        self.width = wall_width
        self.height = wall_height

        self.image=Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        
        self.rect = self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

win_width=700
win_height=500
window=display.set_mode((win_width,win_height))
display.set_caption('labirint')

background=transform.scale(image.load('background.jpg'),(win_width,win_height))

player=Player('hero.png',5,win_height - 80, 5)
monster=Enemy('cyborg.png',win_width - 80,280,2)

final=GameSprite('treasure.png',win_width - 120, win_height - 80,0)

w1=Wall(150,110,190,50,20,450,20)
w2=Wall(150,110,190,50,20,20,300)
w3=Wall(150,110,190,150,300,20,300)
w4=Wall(150,110,190,250,20,20,300)
w5=Wall(150,110,190,350,300,20,300)
w6=Wall(150,110,190,450,20,20,300)


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

game=True
clock=time.Clock()

font.init()
font=font.Font(None,70)
win = font.render('YOU WIN!', True, (255,215,0))
lose=font.render('YOU LOSE!', True, (100, 0, 0))

while game:
    
    for e in event.get():
        if e.type ==QUIT:
            game = False
        player.update()
        monster.update()
    monster.reset()
    final.reset()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    if game:
        window.blit(background,(0,0))
        player.reset()

    if sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,monster):
        game = False
        window.blit(lose,(200,200))
        kick.play
    if sprite.collide_rect(player,final):
        game = False
        window.blit(win,(200,200))
        money.play

    display.update()
    clock.tick(60)