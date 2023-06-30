import pygame
pygame.init()
class text:
    global screen
    def __init__(self, text: str, x=0, y=0, color=(255, 255, 255), size=50):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size
    def draw(self, text):
        if text != "":
            self.text = text
        font = pygame.font.SysFont(None, self.size)
        self.text_obj = font.render(self.text, True, self.color)
        screen.blit(self.text_obj, (self.x, self.y))
