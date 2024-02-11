import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self,win_width,win_height,path):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.win_width = win_width
        self.win_height = win_height
        starPoint_X = win_width/2
        startPoint_Y = win_height-100
        self.rect = self.image.get_rect(midbottom =(starPoint_X,startPoint_Y))
        self.speed_X  = 2
        self.speed_Y = 2

    def player_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.rect.y += (-self.speed_Y)
            if self.rect.y <=0:
                self.rect.y =0

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed_Y
            if self.rect.bottom >=self.win_height:
                self.rect.bottom =self.win_height

        if keys[pygame.K_LEFT]:
            self.rect.x += (-self.speed_X)
            if self.rect.x <=0:
                self.rect.x =0

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_X
            if self.rect.right >=self.win_width:
                self.rect.right =self.win_width
    
    def update(self):
        self.player_input()


class Turbo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        fire1 = pygame.image.load('space/PNG/Effects/fire16.png')
        fire2 = pygame.image.load('space/PNG/Effects/fire17.png')
        self.fire = [fire1,fire2]
        self.fire_index = 0


        self.image = self.fire[self.fire_index]
        self.rect = self.image.get_rect(midbottom =(384,700))

    def animation_state(self):
        self.fire_index += 0.2
        if self.fire_index >= len(self.fire): self.fire_index = 0
        self.image = self.fire[int(self.fire_index)]

    def update(self):
        self.animation_state()

