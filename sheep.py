import rays_math
import pygame
import constants

from math import cos, sin, radians
pygame.init()
CONST = constants.const()

class sheep:
    def __init__(self, screen, x: int = 0, y: int = 0, angle: int = 0, ray_len: int = 50, rays_amount: int = 30, color: tuple = (255, 255, 255), width: int = 10, height: int = 10):
        debag = False
        self.screen = screen

        self.width = width
        self.height = height

        self.x = x
        self.y = y
        self.angle = angle
        self.color = color

        self.ray_len = ray_len
        self.rays_amount = rays_amount

        if debag:
            print(" You see that because debag is On!")
            print("==================================")
            print("self.width: " + str(self.width))
            print("self.height: " + str(self.height))
            print("self.x: " + str(self.x))
            print("self.y: " + str(self.y))
            print("self.angle: " + str(self.angle) + "\n")

        self.what_player_see = []
        for i in range(0, self.rays_amount+1):
            self.what_player_see.append(0)
#       v Makes Artificial Nerons v
        self.AI = []
        for input in range(0, self.rays_amount+1):
            self.AI.append([])
            for level_1 in range(0, self.rays_amount):
                self.AI[input].append([1000000, []])
                for level_2 in range(0, self.rays_amount):
                    self.AI[input][level_1][1].append([1000000, []])
                    for output in range(-rays_amount//2,self.rays_amount//2):
                        self.AI[input][level_1][1][level_2][1].append([1000000, output])

    def change_characteristics(self, x: int = 0, y: int = 0, angle: int = 0, ray_len: int = 50, rays_amount: int = 30, color: tuple = (255, 255, 255), width: int = 10, height: int = 10):
        """ Changes values of already created object
        """
        self.width = width
        self.height = height

        self.x = x
        self.y = y
        self.angle = angle
        self.color = color

        self.ray_len = ray_len
        self.rays_amount = rays_amount

        self.obj = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def look(self, food_list:list, debag:bool = False, debag_color_1:tuple = (50, 250, 50), debag_color_2:tuple = (250, 250, 50), debag_color_3: tuple = (50,250,250), debag_width:int = 1):
        """Checks for nearby food 
        """
        if debag:
            result = rays_math.check_if_ray_touching_points(self.x+(self.width//2), self.y+(self.height//2), self.angle-(self.rays_amount//2), self.angle+(self.rays_amount//2), food_list, self.ray_len)
            self.what_player_see = result[0]
            food_that_sheep_see = result[1]
            for food_cords in food_that_sheep_see:
                pygame.draw.line(self.screen, debag_color_1, self.obj.center, food_cords, debag_width)
            pygame.draw.line(self.screen, (200, 0 ,0), self.obj.center, (self.x + cos(radians(self.angle-self.rays_amount//2))*self.ray_len, self.y + sin(radians(self.angle-self.rays_amount//2))*self.ray_len), debag_width)
            pygame.draw.line(self.screen, debag_color_2, self.obj.center, (self.x + cos(radians(self.angle+self.rays_amount//2))*self.ray_len, self.y + sin(radians(self.angle+self.rays_amount//2))*self.ray_len), debag_width)
            for i in range(0, len(self.what_player_see)-1):
                if self.what_player_see[i+1] != 0:
                    pygame.draw.line(self.screen, debag_color_3, self.obj.center, (self.x + cos(radians(self.angle+i-self.rays_amount//2))*self.ray_len, self.y + sin(radians(self.angle+i-self.rays_amount//2))*self.ray_len), 3)

        else:
            self.what_player_see = rays_math.check_if_ray_touching_points(self.x+(self.width//2), self.y+(self.height//2), self.angle-(self.rays_amount//2), self.angle+(self.rays_amount//2), food_list, self.ray_len)[0]

    def calc_new_pos(self, speed: int = 1):
        """ Moves object forward
        """
        SCREEN_WIDTH = CONST.SCREEN_WIDTH
        SCREEN_HEIGHT = CONST.SCREEN_HEIGHT
        self.angle = self.angle%360
        if self.angle < 0:
            self.angle = 360 - self.angle
        self.y += speed*sin(radians(self.angle))
        if self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
        if self.y < 0:
            self.y = 0
        self.x += speed*cos(radians(self.angle))
        if self.x > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH
        if self.x < 0:
            self.x = 0
        
    def draw(self):
        """ Draw an object on screen
        """
        self.obj = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    
    def decision(self, debag:bool = False):
        rays_that_found_food = []
        keys = []
        #Output -> ray_id
        for i in range(0, len(self.what_player_see)):
            if self.what_player_see[i] != 0:
                rays_that_found_food.append(i)
        if rays_that_found_food == []:
            self.ray_id = 0
            keys = []
            for level_1 in range(0, self.rays_amount):
                keys.append(self.AI[0][level_1][0])
            self.level_1_id = rays_math.find_biggest_number_in_list_with_id(keys)[1]
        else:
            self.ray_id = 0
            self.level_1_id = 0
            for ray in rays_that_found_food:
                for level_1 in range(0, self.rays_amount):
                    if self.AI[ray][level_1][0] >= self.AI[self.ray_id][self.level_1_id][0]:
                        self.ray_id = ray
                        self.level_1_id = level_1
        #level_1_id -> level_2_id
        keys = []
        for level_2 in range(0, self.rays_amount):
            keys.append(self.AI[self.ray_id][self.level_1_id][1][level_2][0])
        self.level_2_id = rays_math.find_biggest_number_in_list_with_id(keys)[1]
        #level_2_id -> output_id
        keys = []
        for output in range(0, self.rays_amount//2):
            keys.append(self.AI[self.ray_id][self.level_1_id][1][self.level_2_id][1][output][0])
        self.output_id = rays_math.find_biggest_number_in_list_with_id(keys)[1]

        choice = self.AI[self.ray_id][self.level_1_id][1][self.level_2_id][1][self.output_id][1]
        if debag:
            print(str(choice+0.01)[0:3], end='     ')
        #START TEMP
        #choice = 1
        #END TEMP
        if choice <= -15:
        	choice = -15
        elif choice >= 15:
        	choice = 15
        self.angle += choice
         
    def touched_food(self, food_pos):
        return rays_math.check_if_point_in_sqr(self.x, self.x+self.width, self.y, self.y+self.height, food_pos)
