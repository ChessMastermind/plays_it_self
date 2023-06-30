import pygame, sheep, getdata, grass, constants
import time
CONST = constants.const()

pygame.init()
pygame.display.set_caption('Playing')
screen = pygame.display.set_mode((CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
#screen = pygame.display.set_mode((CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT), pygame.SCALED)
sheeps_list = []
for i in range(1, CONST.sheeps+1):
    sheeps_list.append(sheep.sheep(screen, CONST.SCREEN_WIDTH//(CONST.sheeps+1)*i, CONST.SCREEN_HEIGHT//(CONST.sheeps+1)*i, 0, 100))
print("Finished creating sheeps!")
food_list = []
for i in range(0, CONST.grass):
    food_list.append(grass.random_pos())

render = True
debag = False
done = False
start_time = time.time()
counter = 0

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
fps_text = text('FPS: ?', 0, 0)
fps = 'FPS: ?'
while not done:
    counter += 1
    #pygame.time.delay(50)
    if render:
        screen.fill((50, 50, 50))
        fps_text.draw(fps)
        if (time.time() - start_time) > 10 :
            fps = "FPS: " + str(round(counter / (time.time() - start_time), 0))
            fps_text.draw(fps)
            counter = 0
            start_time = time.time()
    else:
    	
    	if (time.time() - start_time) > 10 :
    		fps = "FPS: " + str(round(counter / (time.time() - start_time), 0))
    		print(fps)
    		counter = 0
    		start_time = time.time()
    for sheep_obj in sheeps_list:
        if render:
            sheep_obj.draw()
        sheep_obj.look(food_list, debag)
        sheep_obj.decision()
        sheep_obj.calc_new_pos()
        #sheep_obj = sheep.sheep(screen, 10, 10*i, 0, 100)
        for food_pos in food_list:
            if render:
                grass.draw(screen, food_pos)
            if sheep_obj.touched_food(food_pos):
                sheep_obj.AI[sheep_obj.ray_id][sheep_obj.level_1_id][0] += 5
                sheep_obj.AI[sheep_obj.ray_id][sheep_obj.level_1_id][1][sheep_obj.level_2_id][0] += 5
                sheep_obj.AI[sheep_obj.ray_id][sheep_obj.level_1_id][1][sheep_obj.level_2_id][1][sheep_obj.output_id][0] += 5
                food_list.remove(food_pos)
                food_list.append(grass.random_pos())
            if not sheep_obj.AI[sheep_obj.ray_id][sheep_obj.level_1_id][0] <= 0:
                sheep_obj.AI[sheep_obj.ray_id][sheep_obj.level_1_id][0] -= 0.001
            if not sheep_obj.AI[sheep_obj.ray_id][sheep_obj.level_1_id][1][sheep_obj.level_2_id][0] <= 0:
                sheep_obj.AI[sheep_obj.ray_id][sheep_obj.level_1_id][1][sheep_obj.level_2_id][0] -= 0.001
            if not sheep_obj.AI[sheep_obj.ray_id][sheep_obj.level_1_id][1][sheep_obj.level_2_id][1][sheep_obj.output_id][0] <= 0:
                sheep_obj.AI[sheep_obj.ray_id][sheep_obj.level_1_id][1][sheep_obj.level_2_id][1][sheep_obj.output_id][0] -= 0.001
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_r:
                if render:
                	render = False
                else:
                	render = True
            if event.key == pygame.K_d:
                if debag:
                	debag = False
                else:
                	debag = True
    if render:
        pygame.display.update()
    	    

