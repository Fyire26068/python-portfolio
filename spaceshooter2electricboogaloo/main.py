import pygame as pg
import random as r
import math
from os import *


#Attribution
####################################################################
# Art Work Credit: "Kenney.nl" @ "www.kenney.nl"
# Code by: Anthony Garrard

####################################################################

# Game object classes
####################################################################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.shield = 100
        # self.image = pg.Surface((50,40))
        # self.image.fill(GREEN)
        self.image = player_img
        self.image = pg.transform.scale(player_img,(60,48))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width*.85 / 2
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = (HEIGHT - (HEIGHT*.05))
        self.speedx = 0
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -8
        if keystate[pg.K_RIGHT]:
            self.speedx = 8
        if keystate[pg.K_SPACE]or keystate[pg.K_UP]:
            self.shoot()
        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = pg.time.get_ticks()
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullet_group.add(bullet)
            shoot_snd.play()


class NPC(pg.sprite.Sprite):
    def __init__(self):
        # pg.sprite.Sprite.__init__(self)
        # #super(NPC, self).__init__()
        # # self.image = pg.Surface((25,25))
        # # self.image.fill(RED)
        # self.image_orig = r.choice(meteor_images)
        # self.image_orig.set_colorkey(BLACK)
        # self.image = self.image_orig.copy()
        #
        # self.rect = self.image.get_rect()
        # self.radius = int(self.rect.width * .85 / 2)
        # #pg.draw.circle(self.image,RED,self.rect.center,self.radius)
        # # self.rect.centerx = (WIDTH/2)
        # # self.rect.top = 0
        # self.rsx = r.randint(-3, 3)
        # self.rsy = r.randint(1, 8)
        # self.rect.x = r.randrange(WIDTH - self.rect.width)
        # self.rect.y = r.randrange(-100, -40)
        # self.speedx = self.rsx
        # self.speedy = self.rsy
        # self.rot = 0
        # self.rot_speed = r.randint(-8,8)
        # self.last_update = pg.time.get_ticks()
        pg.sprite.Sprite.__init__(self)
        self.image_orig = r.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = r.randrange(WIDTH - self.rect.width)
        self.rect.y = r.randrange(-150, -100)
        self.speedy = r.randrange(1, 8)
        self.speedx = r.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = r.randrange(-8, 8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        # now = pg.time.get_ticks()
        # if now - self.last_update > 50:
        #     self.last_update = now
        #     # do a barrel roll
        #     old_center = self.rect.center
        #     self.rot = (self.rot + self.rot_speed) % 360
        #     new_image = pg.transform.rotate(self.image, self.rot)
        #     self.image = new_image
        #     self.rect = self.image.get_rect()
        #     self.rect.center = old_center
        now = pg.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def spawn(self):
        m = NPC()
        all_sprites.add(m)
        npc_group.add(m)



    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10:
            self.rect.x = r.randrange(WIDTH - self.rect.width)
            self.rect.y = r.randrange(-100, -40)
            self.speedy = r.randrange(1, 8)
            self.speedx = r.randrange(-1,1)

        if self.rect.right > WIDTH:
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.speedx = -self.speedx


class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        # self.image = pg.Surface((5,10))
        # self.image.fill(BLUE)
        self.image = bullet_img
        self.image = pg.transform.scale(self.image, (15, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

####################################################################

# Game Function
#####################################################################
font_name = pg.font.match_font('arial')
def draw_text(surf, text, size, x, y, color):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_healthbar(surf, x, y, pct):
    if pct < 0 :
        pct = 0
    bar_len = 100
    bar_height = 10
    fill = (pct/100)*bar_len
    outline_rect = pg.Rect(x, y, bar_len, bar_height)
    fill_rect = pg.Rect(x, y, fill, bar_height)
    pg.draw.rect(surf, GREEN, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

####################################################################

# Game Constants
####################################################################
HEIGHT = 900
WIDTH = 600
FPS = 60

# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

title = "Shmup"
#font_name = pg.Font()

####################################################################

# initialize pygame and create window
####################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
####################################################################

#image locations
####################################################################
project_folder = path.dirname(__file__)
img_folder = path.join(project_folder,"imgs")
background_img_folder = path.join(img_folder, "background")
player_img_folder =  path.join(img_folder, "player")
enemy_img_folder = path.join(img_folder, "enemy")
snds_folder = path.join(project_folder,"snds")
base_snds_folder = path.join(snds_folder, "base")
####################################################################

# load imgs
####################################################################
#back grond img loaded
background = pg.image.load(path.join(background_img_folder,"starfield.png")).convert()
background = pg.transform.scale(background,(WIDTH,HEIGHT))
background_rect = background.get_rect()
# player img loaded
player_img = pg.image.load(path.join(player_img_folder,"player1ship.png")).convert()
#npc_img = pg.image.load(path.join(enemy_img_folder,"img_1.png")).convert()
bullet_img = pg.image.load(path.join(player_img_folder,"bullet_img.png")).convert()

# load asteroids
meteor_images = []
meteor_list = ['img_1.png', 'img_2.png', 'img_3.png', 'img_4.png', 'img_5.png', 'img_6.png', 'img_7.png',
               'img_8.png', 'img_9.png', 'img_10.png']
for img in meteor_list:
    meteor_images.append(pg.image.load(path.join(enemy_img_folder, img)).convert())

####################################################################

# load Sounds
####################################################################
shoot_snd = pg.mixer.Sound(path.join(base_snds_folder,"pew.wav"))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pg.mixer.Sound(path.join(base_snds_folder, snd)))

pg.mixer.music.load(path.join(base_snds_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play(loops=-1)
####################################################################

# create Sprite groups
####################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
####################################################################

# create Game Objects
####################################################################
player = Player()
npc = NPC()

####################################################################

# add objects to sprite groups
####################################################################
players_group.add(player)
for i in players_group:
    all_sprites.add(i)
for i in range(8):
    m = NPC()
    all_sprites.add(m)
    npc_group.add(m)

####################################################################


# Game Loop
###################
# game update Variables
########################################
playing = True
score = 0
########################################
################################################################
while playing:
    # timing
    ##################################################
    clock.tick(FPS)
    ##################################################

    # collecting Input
    ##################################################

    # Quiting the game when we hit the x
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False
            # if event.key == pg.K_SPACE or event.key == pg.K_UP:
            #     player.shoot()
        if event.type == pg.QUIT:
            playing = False


    ##################################################
    # Updates
    ##################################################
    all_sprites.update()

    # check to see if npc hit the player

    hits = pg.sprite.spritecollide(player, npc_group, True, pg.sprite.collide_circle)
    for hit in hits:
        r.choice(expl_sounds).play()
        npc.spawn()
        player.shield -= hit.radius*2
        if player.shield <= 0:
            playing = False

    # check to see if npc hit npc
    hits = pg.sprite.groupcollide(npc_group, npc_group, False, False, pg.sprite.collide_circle)
    if hits:
        npc.speedx = -npc.speedx
    # check to see if bullet hits npc
    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True)
    for hit in hits:
        score += 50 - hit.radius
        m = NPC()
        all_sprites.add(m)
        npc_group.add(m)
        r.choice(expl_sounds).play()
    ##################################################

    # Render
    ##################################################

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # draw HUD
    draw_text(screen, "Score: " + str(score), 18, WIDTH/2,10, WHITE)
    draw_healthbar(screen, 5, 10, player.shield)

    pg.display.flip()
    ##################################################

pg.quit()

################################################################
#####################