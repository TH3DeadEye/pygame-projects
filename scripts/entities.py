import pygame 

class PhisicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.e_type = e_type
        self.pos = list(pos)
        self.size = size 
        self.velocity = [0, 0]

    def update(self, movemnt = (0, 0)):  
            frame_movemnt = (movemnt[0] + self.velocity[0], movemnt[1] + self.velocity[1])
            #updating the x pos
            self.pos[0] += frame_movemnt[0]
            #updating the y pos
            self.pos[1] += frame_movemnt[1]

    def render(self, surface):
        surface.blit(self.game.assets['player'], self.pos)