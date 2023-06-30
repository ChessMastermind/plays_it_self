import math

def check_if_ray_touching_points(bot_x, bot_y, ray_angle_start, ray_angle_finished, food_list, ray_len):
    what_player_see = [0]
    for i in range(0, ray_angle_finished-ray_angle_start):
        what_player_see.append(0)
    rays_that_player_see = []
    for food_cords in food_list:
        if check_if_point_in_sqr((bot_x - ray_len), (bot_x + ray_len), (bot_y - ray_len), (bot_y + ray_len), food_cords):
            l_sqr = (bot_x-food_cords[0])**2 + (bot_y-food_cords[1])**2
            if ray_len**2 >= l_sqr:
                if food_cords[1]-bot_y == 0:
                    pass
                else:
                    angle_to_food_calc_by_atan = math.degrees(math.atan2((food_cords[1]-bot_y), (food_cords[0]-bot_x)))
                    if angle_to_food_calc_by_atan >= 0:
                    	angle_to_food = angle_to_food_calc_by_atan
                    else:
                    	angle_to_food = 360 + angle_to_food_calc_by_atan
                    
                    if angle_to_food <= (ray_angle_finished) and angle_to_food >= (ray_angle_start):
                    
                            l = round(l_sqr**0.5, 2)
                            if l >= 10:
                                what_player_see[int(round(angle_to_food-ray_angle_start, 0))] += (ray_len-l)/ray_len
                            else:
                                what_player_see[int(round(angle_to_food-ray_angle_start, 0))] += 1
                            rays_that_player_see.append(food_cords)
                    
                   	
    if what_player_see.__contains__(1):
        return what_player_see, rays_that_player_see
    else:
        what_player_see[0] = 1
        return what_player_see, rays_that_player_see

def check_if_point_in_sqr(x_start, x_finish, y_start, y_finish, point) -> bool:
    if point[0] >= x_start and point[0] <= x_finish and point[1] >= y_start and point[1] <= y_finish:
        return True
    else: 
        return False


def find_biggest_number_in_list_with_id(l):
    max_num = 0
    max_num_id = 0
    for i in range(0, len(l)):
        if max_num <= l[i]:
            max_num = l[i]
            max_num_id = i
    return (max_num, max_num_id)
