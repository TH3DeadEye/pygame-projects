import pygame
import sys
from scripts.entities import PhisicsEntity
from scripts.utils import load_image

class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('Platfromer')
        self.screen = pygame.display.set_mode((650, 480))   
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        #loading assets
        self.player = PhisicsEntity(self, 'player', (50,50), (8,15))

        #game vars
        self.movement = [False, False]
        
        self.assets = {
            'player': load_image('entities/player.png')
        }

        
    def run(self):
        while True: 
            #rendering the player
            self.display.fill((100,250,100))
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)
            
            #handeling event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  

                #inputs
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0]= True 
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = False  

            #loading the background
           

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()