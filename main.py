from pygame import*

class Game_sprite(sprite.Sprite):
    def __init__(self, img, w, h, x, y):
        super().__init__()
        self.image = transform.scale(img, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.image, self.rect)


class PlatformUp(Game_sprite):
    def __init__(self):
        super().__init__(image.load('platformUp.png'), 190, 30, 100, 45)

class PlatformDown(Game_sprite):
    def __init__(self):
        super().__init__(image.load('platformDown.png'), 190, 30, 700, 500)

class Ball(Game_sprite):
    def __init__(self):
        super().__init__(image.load('ball.png'), 80, 60, 450, 300)
        self.x = 3
        self.y = -3
    def update(self, platformUp, platformDown):
        self.rect.x += self.x
        self.rect.y += self.y

        if self.rect.x <= 0 or self.rect.x > 700:
            self.x *= -1
        if self.rect.colliderect(platformUp):
            self.y = 3
        if self.rect.colliderect(platformDown):
            self.y = -3
        if self.rect.y <= 0:
            self.rect.x = 350
            self.rect.y = 450
            #посчитать очки
        if self.rect.y >= 700:
            self.rect.x = 450
            self.rect.y = 300
            #посчитать очки
        super().update()    


screen = display.set_mode((900,600))
display.set_caption('pong')
platformUp = PlatformUp()
platformDown = PlatformDown()
ball = Ball()

background = transform.scale(image.load('background.png'), (900, 600))

button_play = transform.scale(image.load('play.png'), (200, 150))
button_quit = transform.scale(image.load('quit.png'), (200, 80))


clock = time.Clock()
game = True
menu = True
finish = True
while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                x, y = mouse.get_pos()
                if menu:
                    if x > 350 and x < 550 and y > 200 and y < 280:
                        menu = False
                        finish = False
                        #перезапуск персов
                    if x > 350 and x < 550 and y > 400 and y < 480:
                       game = False
    screen.blit(background, (0,0))
    if menu:
        screen.blit(button_play, (350, 200))
        screen.blit(button_quit, (350, 300))
    elif not(finish):
        ball.update(platformUp, platformDown)
        platformUp.update()
        platformDown.update()
    display.update()