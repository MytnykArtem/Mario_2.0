import pygame

#python -m cProfile -o profile_data.prof Mario_2.0.py
#snakeviz profile_data.prof

#Player size = x 50, y 60

# variables
# -------------------------
best_score = [0, 0, 0]
level = "level_1"
b_size = 75
b_size = round(b_size)
p_size_x = (b_size // 5) * 4
p_size_y = b_size
track_width = 20000
track_height = 1000
fall_jump = 0
move_scene_x = 0
move_scene_y = 0
mode = "fall"
side = "r"
checkpoints = 0
objects_on = True
# -------------------------
#
#
#
#
#
#
#
#names
#-------------------------
# b_size = block_size
# gr = ground
# p_size_x = player_size_x
# p_size_y = player_size_y
#-------------------------

pygame.init()
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption('Wonderland Escape')



player_default = pygame.image.load("stand_1.png").convert_alpha()
player_default = pygame.transform.scale(player_default, (p_size_x, p_size_y))
player_stand_1 = pygame.image.load("stand_1.png").convert_alpha()
player_stand_1 = pygame.transform.scale(player_stand_1, (p_size_x, p_size_y))
player_stand_2 = pygame.image.load("stand_2.png").convert_alpha()
player_stand_2 = pygame.transform.scale(player_stand_2, (p_size_x, p_size_y))
player_standing = [player_stand_1 for _ in range(10)] + [player_stand_2 for _ in range(10)]
player_run_1 = pygame.image.load("run_1.png").convert_alpha()
player_run_1 = pygame.transform.scale(player_run_1, (p_size_x, p_size_y))
player_run_2 = pygame.image.load("run_2.png").convert_alpha()
player_run_2 = pygame.transform.scale(player_run_2, (p_size_x, p_size_y))
player_run_3 = pygame.image.load("run_3.png").convert_alpha()
player_run_3 = pygame.transform.scale(player_run_3, (p_size_x, p_size_y))
player_run_4 = pygame.image.load("run_4.png").convert_alpha()
player_run_4 = pygame.transform.scale(player_run_4, (p_size_x, p_size_y))
player_run_5 = pygame.image.load("run_5.png").convert_alpha()
player_run_5 = pygame.transform.scale(player_run_5, (p_size_x, p_size_y))
player_run_6 = pygame.image.load("run_6.png").convert_alpha()
player_run_6 = pygame.transform.scale(player_run_6, (p_size_x, p_size_y))
player_run_7 = pygame.image.load("run_7.png").convert_alpha()
player_run_7 = pygame.transform.scale(player_run_7, (p_size_x, p_size_y))
player_run_8 = pygame.image.load("run_8.png").convert_alpha()
player_run_8 = pygame.transform.scale(player_run_8, (p_size_x, p_size_y))
player_running = [player_run_1, player_run_2, player_run_3, player_run_4, player_run_5, player_run_6, player_run_7, player_run_8]
player_jump = pygame.image.load("jump.png").convert_alpha()
player_jump = pygame.transform.scale(player_jump, (p_size_x, p_size_y))
player_wall_jump = pygame.image.load("wall_jump.png").convert_alpha()
player_wall_jump = pygame.transform.scale(player_wall_jump, (p_size_x, p_size_y))
player_fall = pygame.image.load("fall.png").convert_alpha()
player_fall = pygame.transform.scale(player_fall, (p_size_x, p_size_y))

ground_grass = pygame.image.load("Grass.png").convert_alpha()
ground_grass = pygame.transform.scale(ground_grass, (b_size, b_size))
ground_default = pygame.image.load("Ground.png").convert_alpha()
ground_default = pygame.transform.scale(ground_default, (b_size, b_size))

brick_default = pygame.image.load("Block_Brick.png").convert_alpha()
brick_default = pygame.transform.scale(brick_default, (b_size, b_size))

silver_block_default = pygame.image.load("Block_Silver.png").convert_alpha()
silver_block_default = pygame.transform.scale(silver_block_default, (b_size, b_size))

gold_block_default = pygame.image.load("Block_Gold.png").convert_alpha()
gold_block_default = pygame.transform.scale(gold_block_default, (b_size, b_size))

brown_block_default = pygame.image.load("Block_Brown.png").convert_alpha()
brown_block_default = pygame.transform.scale(brown_block_default, (b_size, b_size))

orange_block_default = pygame.image.load("Block_Orange.png").convert_alpha()
orange_block_default = pygame.transform.scale(orange_block_default, (b_size, b_size))

snake_default = pygame.image.load("snake_1.png").convert_alpha()
snake_default = pygame.transform.scale(snake_default, (40, 20))
snake_1 = pygame.image.load("snake_2.png").convert_alpha()
snake_1 = pygame.transform.scale(snake_1, (40, 20))
snake_2 = pygame.image.load("snake_3.png").convert_alpha()
snake_2 = pygame.transform.scale(snake_2, (40, 20))
snake_3 = pygame.image.load("snake_4.png").convert_alpha()
snake_3 = pygame.transform.scale(snake_3, (40, 20))

mushroom_default = pygame.image.load("mushroom_1.png").convert_alpha()
mushroom_default = pygame.transform.scale(mushroom_default, (45, 50))
mushroom_1 = pygame.image.load("mushroom_2.png").convert_alpha()
mushroom_1 = pygame.transform.scale(mushroom_1, (45, 50))
mushroom_2 = pygame.image.load("mushroom_3.png").convert_alpha()
mushroom_2 = pygame.transform.scale(mushroom_2, (45, 50))
mushroom_3 = pygame.image.load("mushroom_4.png").convert_alpha()
mushroom_3 = pygame.transform.scale(mushroom_3, (45, 50))
mushroom_4 = pygame.image.load("mushroom_5.png").convert_alpha()
mushroom_4 = pygame.transform.scale(mushroom_4, (45, 50))
mushroom_5 = pygame.image.load("mushroom_6.png").convert_alpha()
mushroom_5 = pygame.transform.scale(mushroom_5, (45, 50))
mushroom_6 = pygame.image.load("mushroom_7.png").convert_alpha()
mushroom_6 = pygame.transform.scale(mushroom_6, (45, 50))
mushroom_7 = pygame.image.load("mushroom_8.png").convert_alpha()
mushroom_7 = pygame.transform.scale(mushroom_7, (45, 50))

horse_size_x = b_size
horse_size_y = b_size + b_size // 2
horse_run_1 = pygame.image.load("horse_run_1.png").convert_alpha()
horse_run_1 = pygame.transform.scale(horse_run_1, (horse_size_x, horse_size_y))  # (186, 138)
horse_run_2 = pygame.image.load("horse_run_2.png").convert_alpha()
horse_run_2 = pygame.transform.scale(horse_run_2, (horse_size_x, horse_size_y))
horse_run_3 = pygame.image.load("horse_run_3.png").convert_alpha()
horse_run_3 = pygame.transform.scale(horse_run_3, (horse_size_x, horse_size_y))
horse_run_4 = pygame.image.load("horse_run_4.png").convert_alpha()
horse_run_4 = pygame.transform.scale(horse_run_4, (horse_size_x, horse_size_y))
horse_run_5 = pygame.image.load("horse_run_5.png").convert_alpha()
horse_run_5 = pygame.transform.scale(horse_run_5, (horse_size_x, horse_size_y))
horse_run_6 = pygame.image.load("horse_run_6.png").convert_alpha()
horse_run_6 = pygame.transform.scale(horse_run_6, (horse_size_x, horse_size_y))
horse_hit_1 = pygame.image.load("horse_hit_2.png").convert_alpha()
horse_hit_1 = pygame.transform.scale(horse_hit_1, (horse_size_x, horse_size_y))
horse_hit_2 = pygame.image.load("horse_hit_3.png").convert_alpha()
horse_hit_2 = pygame.transform.scale(horse_hit_2, (horse_size_x, horse_size_y))
horse_hit_3 = pygame.image.load("horse_hit_4.png").convert_alpha()
horse_hit_3 = pygame.transform.scale(horse_hit_3, (horse_size_x + horse_size_x // 3, horse_size_y))
horse_hit_4 = pygame.image.load("horse_hit_5.png").convert_alpha()
horse_hit_4 = pygame.transform.scale(horse_hit_4, (horse_size_x + horse_size_x // 1.5, horse_size_y))
horse_hit_5 = pygame.image.load("horse_hit_6.png").convert_alpha()
horse_hit_5 = pygame.transform.scale(horse_hit_5, (horse_size_x + horse_size_x // 10, horse_size_y))

mum_run_1 = pygame.image.load("mum_run_1.png").convert_alpha()
mum_run_1 = pygame.transform.rotozoom(mum_run_1, 0, 3)
mum_run_2 = pygame.image.load("mum_run_2.png").convert_alpha()
mum_run_2 = pygame.transform.rotozoom(mum_run_2, 0, 3)
mum_run_3 = pygame.image.load("mum_run_3.png").convert_alpha()
mum_run_3 = pygame.transform.rotozoom(mum_run_3, 0, 3)
mum_run_4 = pygame.image.load("mum_run_4.png").convert_alpha()
mum_run_4 = pygame.transform.rotozoom(mum_run_4, 0, 3)
mum_run_5 = pygame.image.load("mum_run_5.png").convert_alpha()
mum_run_5 = pygame.transform.rotozoom(mum_run_5, 0, 3)
mum_run_6 = pygame.image.load("mum_run_6.png").convert_alpha()
mum_run_6 = pygame.transform.rotozoom(mum_run_6, 0, 3)
mum_hit_1 = pygame.image.load("mum_hit_1.png").convert_alpha()
mum_hit_1 = pygame.transform.rotozoom(mum_hit_1, 0, 3)
mum_hit_2 = pygame.image.load("mum_hit_2.png").convert_alpha()
mum_hit_2 = pygame.transform.rotozoom(mum_hit_2, 0, 3)
mum_hit_3 = pygame.image.load("mum_hit_3.png").convert_alpha()
mum_hit_3 = pygame.transform.rotozoom(mum_hit_3, 0, 3)
mum_hit_4 = pygame.image.load("mum_hit_4.png").convert_alpha()
mum_hit_4 = pygame.transform.rotozoom(mum_hit_4, 0, 3)
mum_hit_5 = pygame.image.load("mum_hit_5.png").convert_alpha()
mum_hit_5 = pygame.transform.rotozoom(mum_hit_5, 0, 3)
mum_stand_1 = pygame.image.load("mum_stand_1.png").convert_alpha()
mum_stand_1 = pygame.transform.rotozoom(mum_stand_1, 0, 3)
mum_stand_2 = pygame.image.load("mum_stand_2.png").convert_alpha()
mum_stand_2 = pygame.transform.rotozoom(mum_stand_2, 0, 3)

fly_plat_default = pygame.image.load("Plat_Fly_1.png")
fly_plat_default = pygame.transform.scale(fly_plat_default, (b_size, b_size // 10 * 4))
fly_plat_1 = pygame.image.load("Plat_Fly_2.png")
fly_plat_1 = pygame.transform.scale(fly_plat_1, (b_size, b_size // 10 * 4))
fly_plat_2 = pygame.image.load("Plat_Fly_3.png")
fly_plat_2 = pygame.transform.scale(fly_plat_2, (b_size, b_size // 10 * 4))
fly_plat_3 = pygame.image.load("Plat_Fly_4.png")
fly_plat_3 = pygame.transform.scale(fly_plat_3, (b_size, b_size // 10 * 4))
fly_plat_default_2 = pygame.image.load("Banana.png")
fly_plat_default_2 = pygame.transform.scale(fly_plat_default_2, (b_size // 3, b_size // 3))

jump_pad_1 = pygame.image.load("jump_pad_1.png")
jump_pad_1 = pygame.transform.scale(jump_pad_1, (b_size, b_size / 2))
jump_pad_2 = pygame.image.load("jump_pad_2.png")
jump_pad_2 = pygame.transform.scale(jump_pad_2, (b_size, (b_size / 5) * 3))
jump_pad_3 = pygame.image.load("jump_pad_3.png")
jump_pad_3 = pygame.transform.scale(jump_pad_3, (b_size, b_size))
jump_pad_4 = pygame.image.load("jump_pad_4.png")
jump_pad_4 = pygame.transform.scale(jump_pad_4, (b_size, b_size * 1.1))
jump_pad_5 = pygame.image.load("jump_pad_5.png")
jump_pad_5 = pygame.transform.scale(jump_pad_5, (b_size, b_size * 1.1))
jump_pad_default_2 = pygame.image.load("Apple.png")
jump_pad_default_2 = pygame.transform.scale(jump_pad_default_2, (b_size // 3, b_size // 3))

expand_plat_i = 1
expand_plat_original = pygame.image.load("Plat_Thin_Wood.png")
expand_plat_default = pygame.transform.scale(expand_plat_original, (expand_plat_i, b_size / 5))
expand_plat_default_2 = pygame.image.load("Cherry.png")
expand_plat_default_2 = pygame.transform.scale(expand_plat_default_2, (b_size // 3, b_size // 3))

spike_default = pygame.image.load("Spike.webp")

saw_1 = pygame.image.load("Saw_1.png")
saw_2 = pygame.image.load("Saw_2.png")
saw_3 = pygame.image.load("Saw_3.png")
saw_4 = pygame.image.load("Saw_4.png")
saw_5 = pygame.image.load("Saw_5.png")
saw_6 = pygame.image.load("Saw_6.png")
saw_7 = pygame.image.load("Saw_7.png")
saw_8 = pygame.image.load("Saw_8.png")

saw_default = pygame.image.load("SpikedBall.png")

fruit_apple = pygame.image.load("Apple.png")
fruit_apple = pygame.transform.scale(fruit_apple, (b_size / 3, b_size / 3))
fruit_banana = pygame.image.load("Banana.png")
fruit_banana = pygame.transform.scale(fruit_banana, (b_size / 3, b_size / 3))
fruit_cherry = pygame.image.load("Cherry.png")
fruit_cherry = pygame.transform.scale(fruit_cherry, (b_size / 3, b_size / 3))

coin_default = pygame.image.load("coin.png")
coin_default = pygame.transform.scale(coin_default, (b_size / 2, b_size / 2))

box_default = pygame.image.load("Box.png")
box_default = pygame.transform.scale(box_default, (b_size, b_size))




class Object:
    def __init__(self, x_pos, y_pos):
        self.x_position = (x_pos * b_size) - b_size
        self.y_position = 700 - ((y_pos * b_size) - b_size)
        # self.rect = self.default.get_rect(bottomleft=(self.x_position, self.y_position))

    def MakeSides(self):
        self.right = self.MakeSelfRect().right
        self.left = self.MakeSelfRect().left
        self.top = self.MakeSelfRect().top
        self.bottom = self.MakeSelfRect().bottom
        self.centerx = self.MakeSelfRect().centerx
        self.centery = self.MakeSelfRect().centery


    def MakeRect(self, surface):
        return surface.get_rect(bottomleft=(self.x_position - move_scene_x, self.y_position - move_scene_y))

    def MakeRect2(self, s):
        if s == "r":
            self.return_s = self.right - move_scene_x
        elif s == "l":
            self.return_s = self.left - move_scene_x
        elif s == "t":
            self.return_s = self.top - move_scene_y
        elif s == "b":
            self.return_s = self.bottom - move_scene_y
        elif s == "x":
            self.return_s = self.centerx - move_scene_x
        elif s == "y":
            self.return_s = self.centery - move_scene_y
        return self.return_s

    def ObjectRight(self, surface):
        TF = False
        for i in set(touch_objects) - set(fly_plats) - set(jump_pads) - set(expand_plats):
            if surface.right == i.MakeRect2("l") and surface.bottom > i.MakeRect2("t") and surface.top < i.MakeRect2("b"):
                TF = True
        for i in fly_plats + jump_pads + expand_plats:
            if surface.right == i.MakeRect(i.default).left and surface.bottom > i.MakeRect(i.default).top and surface.top < i.MakeRect(i.default).bottom and i.work:
                TF = True
        return TF

    def ObjectLeft(self, surface):
        TF = False
        for i in set(touch_objects) - set(fly_plats) - set(jump_pads) - set(expand_plats):
            if surface.left == i.MakeRect2("r") and surface.bottom > i.MakeRect2("t") and surface.top < i.MakeRect2("b"):
                TF = True
        for i in fly_plats + jump_pads + expand_plats:
            if surface.left == i.MakeRect(i.default).right and surface.bottom > i.MakeRect(i.default).top and surface.top < i.MakeRect(i.default).bottom  and i.work:
                TF = True
        return TF

    def ObjectUp(self, surface):
        TF = False
        for i in set(touch_objects) - set(fly_plats) - set(jump_pads) - set(expand_plats):
            if surface.top == i.MakeRect2("b") and surface.left < i.MakeRect2("r") and surface.right > i.MakeRect2("l"):
                TF = True
        for i in fly_plats + jump_pads + expand_plats:
            if surface.top == i.MakeRect(i.default).bottom and surface.left < i.MakeRect(i.default).right and surface.right > i.MakeRect(i.default).left  and i.work:
                TF = True
        return TF

    def ObjectDown(self, surface, width = 0):
        TF = False
        for i in set(touch_objects) - set(fly_plats) - set(jump_pads) - set(expand_plats):
            if surface.bottom == i.MakeRect2("t") and surface.left + width < i.MakeRect2("r") and surface.right + width > i.MakeRect2("l"):
                TF = True
        for i in fly_plats + jump_pads + expand_plats:
            if surface.bottom == i.MakeRect(i.default).top and surface.left + width < i.MakeRect(i.default).right and surface.right + width > i.MakeRect(i.default).left  and i.work:
                TF = True
        return TF



    def FallRight(self, surface):
        # FallRightTF = self.ObjectDown(surface, surface.width)
        return self.ObjectDown(surface, surface.width)

    def FallLeft(self, surface):
        # FallLeftTF = True
        # for i in touch_objects:
        #     if surface.bottom == i.MakeRect(i.default).top and surface.left - b_size < i.MakeRect(i.default).right and surface.right - b_size > i.MakeRect(i.default).left:
        #         FallLeftTF = False
        return self.ObjectDown(surface, -surface.width)



class Player(Object):
    """
    Character that will move on screen
    """
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.transparency = 0

        self.default = player_default
        self.stand_1 = player_stand_1
        self.stand_2 = player_stand_2

        self.standing = [player_stand_1 for _ in range(10)] + [player_stand_2 for _ in range(10)]

        self.run_1 = player_run_1
        self.run_2 = player_run_2
        self.run_3 = player_run_3
        self.run_4 = player_run_4
        self.run_5 = player_run_5
        self.run_6 = player_run_6
        self.run_7 = player_run_7
        self.run_8 = player_run_8

        self.running = [player_run_1, player_run_2, player_run_3, player_run_4, player_run_5, player_run_6, player_run_7, player_run_8]

        self.jump = player_jump
        self.wall_jump = player_wall_jump
        self.fall = player_fall

        self.apples = 0
        self.bananas = 0
        self.cherries = 0

        self.coins = 0


    def MakeSelfRect(self):
        """Returns a rect of the image"""
        self.default_rect = self.default.get_rect(bottomleft=(self.x_position, self.y_position))
        return self.default_rect


    def WallJumpRightTF(self):
        TF = False
        for i in touch_objects:
            if self.MakeSelfRect().right == i.MakeRect(i.default).left and self.MakeSelfRect().bottom < i.MakeRect(i.default).bottom and self.MakeSelfRect().top > i.MakeRect(i.default).top:
                TF = True
        return TF

    def WallJumpLeftTF(self):
        TF = False
        for i in touch_objects:
            if self.MakeSelfRect().left == i.MakeRect(i.default).right and self.MakeSelfRect().bottom < i.MakeRect(i.default).bottom and self.MakeSelfRect().top > i.MakeRect(i.default).top:
                TF = True
        return TF


    def MoveRight(self, num = 8):
        """Moves to the right"""
        global move_scene_x
        for x in boxes:
            if self.MakeSelfRect().right == x.MakeSelfRect().left and self.MakeSelfRect().bottom > x.MakeSelfRect().top and self.MakeSelfRect().top < x.MakeSelfRect().bottom:
                for i in range(num // 2):
                    if not x.ObjectRight(x.MakeSelfRect()):
                        x.x_position += 1

                    if not self.ObjectRight(self.MakeSelfRect()):
                        if self.MakeSelfRect().centerx < 650:  # move_scene == 0 and
                            self.x_position += 1
                        elif move_scene_x == track_width - 1300 and self.MakeSelfRect().centerx >= 650 and self.MakeSelfRect().right != 1300:
                            self.x_position += 1
                        elif move_scene_x < track_width - 1300:
                            move_scene_x += 1

        for i in range(num):
            if not self.ObjectRight(self.MakeSelfRect()):
                if self.MakeSelfRect().centerx < 650:  #move_scene == 0 and
                    self.x_position += 1
                elif move_scene_x == track_width - 1300 and self.MakeSelfRect().centerx >= 650 and self.MakeSelfRect().right != 1300:
                    self.x_position += 1
                elif move_scene_x < track_width - 1300:
                    move_scene_x += 1

    def MoveLeft(self, num = 8):
        """Moves to the left"""
        global move_scene_x
        for x in boxes:
            if self.MakeSelfRect().left == x.MakeSelfRect().right and self.MakeSelfRect().bottom > x.MakeSelfRect().top and self.MakeSelfRect().top < x.MakeSelfRect().bottom:
                for i in range(num // 2):
                    if not x.ObjectLeft(x.MakeSelfRect()):
                        x.x_position -= 1

                    if not self.ObjectLeft(self.MakeSelfRect()):
                        if self.MakeSelfRect().centerx > 650:
                            self.x_position -= 1
                        elif move_scene_x == 0 and self.MakeSelfRect().centerx <= 650 and self.MakeSelfRect().left != 0:
                            self.x_position -= 1
                        elif move_scene_x > 0:
                            move_scene_x -= 1

        for i in range(num):
            if not self.ObjectLeft(self.MakeSelfRect()):
                if self.MakeSelfRect().centerx > 650:
                    self.x_position -= 1
                elif move_scene_x == 0 and self.MakeSelfRect().centerx <= 650 and self.MakeSelfRect().left != 0:
                    self.x_position -= 1
                elif move_scene_x > 0:
                    move_scene_x -= 1

    def Move_Up_Down(self, dir):
        global move_scene_y
        if dir > 0:
            if self.MakeSelfRect().centery > 350:
                self.y_position += 1
            elif move_scene_y == 0 and self.MakeSelfRect().centery <= 350 and self.MakeSelfRect().bottom != 0:
                self.y_position += 1
            elif move_scene_y < 0:
                move_scene_y += 1

        else:
            if self.MakeSelfRect().centery > 350:  # move_scene == 0 and
                self.y_position -= 1
            elif move_scene_y == track_height - 700 and self.MakeSelfRect().centery <= 350 and self.MakeSelfRect().top != 700:
                self.x_position -= 1
            elif move_scene_y < track_height - 700:
                move_scene_y -= 1


    def Minus_Fall_Jump_Speed(self, num):
        """
        Changes the y position of player
        :param num: fall_jump
        :return: None
        """
        # global mode
        global move_scene_y
        global fall_jump
        for i in range(abs(num)):
            if num != fall_jump:
                break
            if num < 0:
                if not self.ObjectDown(self.MakeSelfRect()):
                    check_die()
                    if self.MakeSelfRect().centery > 350:
                        self.y_position += 1
                    elif move_scene_y == 0 and self.MakeSelfRect().centery <= 350 and self.MakeSelfRect().bottom != 0:
                        self.y_position += 1
                    elif move_scene_y < 0:
                        move_scene_y += 1

            elif num > 0:
                if not self.ObjectUp(self.MakeSelfRect()):
                    if self.MakeSelfRect().centery > 350:  # move_scene == 0 and
                        self.y_position -= 1
                    elif move_scene_y == track_height - 700 and self.MakeSelfRect().centery <= 350 and self.MakeSelfRect().top != 700:
                        self.x_position -= 1
                    elif move_scene_y < track_height - 700:
                        move_scene_y -= 1

            for x in range(len(horses)):
                if self.MakeSelfRect().bottom == horses[x].MakeSelfRect().top and self.MakeSelfRect().left < \
                        horses[x].MakeSelfRect().right and self.MakeSelfRect().right > horses[x].MakeSelfRect().left:
                    fall_jump = 20
                    horses[x].lives -= 1
            for x in range(len(mummys)):
                if self.MakeSelfRect().bottom == mummys[x].MakeSelfRect().top and self.MakeSelfRect().left < \
                        mummys[x].MakeSelfRect().right and self.MakeSelfRect().right > mummys[x].MakeSelfRect().left:
                    fall_jump = 20
                    mummys[x].lives -= 1


    def Change_Fall_Jump(self):
        """Checks if Minus_Fall_Jump_Speed can be called"""
        global fall_jump
        if self.ObjectUp(self.MakeSelfRect()):
            fall_jump = -1
        if fall_jump <= 0 and self.ObjectDown(self.MakeSelfRect()):
            fall_jump = 0
        else:
            self.Minus_Fall_Jump_Speed(fall_jump)
            fall_jump -= 2


    def Transparency(self):
        if self.transparency < 255:
            self.transparency += 10
        else:
            self.transparency = 255


    def CheckFruitCoin(self):
        global fruits
        global coins
        for x in range(len(fruits)):
                try:
                    if player_1.MakeSelfRect().colliderect(fruits[x].MakeSelfRect()):
                        if fruits[x].name == "a":
                            self.apples += 1
                        elif fruits[x].name == "b":
                            self.bananas += 1
                        elif fruits[x].name == "c":
                            self.cherries += 1
                        fruits.pop(x)
                except:
                    pass

        for x in range(len(coins)):
                try:
                    if player_1.MakeSelfRect().colliderect(coins[x].MakeSelfRect()):
                        self.coins += 1
                        coins.pop(x)
                except:
                    pass

    def CheckDieAnimal(self):
        global horses
        global mummys
        for x in range(len(horses)):
            try:
                if horses[x].lives <= 0:
                    horses.pop(x)
            except:
                pass

        for x in range(len(mummys)):
            try:
                if mummys[x].lives <= 0:
                    mummys.pop(x)
            except:
                pass



class Ground(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.grass = ground_grass
        self.default = ground_default

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class BrickBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = brick_default

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SilverBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = silver_block_default

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class GoldBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = gold_block_default

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class BrownBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = brown_block_default

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class OrangeBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = orange_block_default

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)



class SmallSilverBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        # self.y_position -= 1

        self.default = pygame.image.load("Block_Silver.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size / 2, b_size / 2))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SmallGoldBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        # self.y_position -= 1

        self.default = pygame.image.load("Block_Gold.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size / 2, b_size / 2))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SmallBrownBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        # self.y_position -= 1

        self.default = pygame.image.load("Block_Brown.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size / 2, b_size / 2))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SmallOrangeBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        # self.y_position -= 1

        self.default = pygame.image.load("Block_Orange.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size / 2, b_size / 2))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)



class GoldThickPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 3 * 2

        self.default = pygame.image.load("Plat_Thick_Gold.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 3))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SilverThickPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 3 * 2

        self.default = pygame.image.load("Plat_Thick_Silver.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 3))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class BrownThickPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 3 * 2

        self.default = pygame.image.load("Plat_Thick_Brown.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 3))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class OrangeThickPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 3 * 2

        self.default = pygame.image.load("Plat_Thick_Orange.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 3))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)



class GoldThinPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 10 * 9


        self.default = pygame.image.load("Plat_Thin_Gold.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 10))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SilverThinPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 10 * 9

        self.default = pygame.image.load("Plat_Thin_Silver.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 10))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class WoodThinPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 10 * 9

        self.default = pygame.image.load("Plat_Thin_Wood.png").convert_alpha()
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 10))

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)



class StartGame(Object):
    def __init__(self, x_pos, y_pos, num):
        super().__init__(x_pos, y_pos)

        self.start_arrow = pygame.image.load('Start_arrow.png').convert_alpha()
        self.start_arrow = pygame.transform.scale(self.start_arrow, (b_size // 10 * 6, b_size))
        self.start_stage = pygame.image.load('Start_stage.png').convert_alpha()
        self.start_stage = pygame.transform.scale(self.start_stage, (b_size, b_size // 4))

        if num == 1:
            self.default = self.start_arrow
        else:
            self.default = self.start_stage
            self.MakeSides()



    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class Checkpoint(Object):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.checkpoint_TF = False

        self.no_checkpoint = pygame.image.load("Checkpoint_No.png").convert_alpha()

        self.checkpoint_1 = pygame.image.load("Checkpoint_Flag_1.png").convert_alpha()
        self.checkpoint_2 = pygame.image.load("Checkpoint_Flag_2.png").convert_alpha()
        self.checkpoint_3 = pygame.image.load("Checkpoint_Flag_3.png").convert_alpha()
        self.checkpoint_4 = pygame.image.load("Checkpoint_Flag_4.png").convert_alpha()
        self.checkpoint_5 = pygame.image.load("Checkpoint_Flag_5.png").convert_alpha()
        self.checkpoint_6 = pygame.image.load("Checkpoint_Flag_6.png").convert_alpha()

        self.checkpointing = [self.checkpoint_1, self.checkpoint_1,
                              self.checkpoint_2, self.checkpoint_2,
                              self.checkpoint_3, self.checkpoint_3,
                              self.checkpoint_4, self.checkpoint_4,
                              self.checkpoint_5, self.checkpoint_5,
                              self.checkpoint_6, self.checkpoint_6]

        self.default = self.no_checkpoint


    def CheckPoint(self):
        global checkpoints
        if not self.checkpoint_TF:
            self.default = self.no_checkpoint
        else:
            self.default = self.checkpoint_1
        if not self.checkpoint_TF:
            if player_1.MakeSelfRect().colliderect(self.MakeSelfRect()):
                self.checkpoint_TF = True
                checkpoints += 1

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class EndGame(Object):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.end_no = pygame.image.load('End_No.png').convert_alpha()
        self.end_no = pygame.transform.scale(self.end_no, (b_size * 2, b_size * 2))
        self.end_1 = pygame.image.load('End_1.png').convert_alpha()
        self.end_1 = pygame.transform.scale(self.end_1, (b_size * 2, b_size * 2))
        self.end_2= pygame.image.load('End_2.png').convert_alpha()
        self.end_2 = pygame.transform.scale(self.end_2, (b_size * 2, b_size * 2 - b_size // 10))
        self.end_3 = pygame.image.load('End_3.png').convert_alpha()
        self.end_3 = pygame.transform.scale(self.end_3, (b_size * 2, b_size * 2 - b_size // 5))

        self.default = self.end_1

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def CheckPressed(self):
        if self.MakeSelfRect().top == player_1.rect.bottom and self.MakeSelfRect().left < player_1.rect.right and self.MakeSelfRect().right > player_1.rect.left:
            return True
        else:
            return False

    def CheckChange(self):
        if self.CheckPressed():
            if self.default == self.end_1:
                self.default = self.end_2
            elif self.default == self.end_2:
                self.default = self.end_3
            elif self.default == self.end_3:
                global level
                global best_score
                over_game_time = pygame.time.get_ticks()
                if best_score[2] == 0:
                    best_score[0] = over_game_time - start_game_time
                    best_score[1] = player_1.coins
                    best_score[2] = over_game_time - start_game_time - player_1.coins * 1000
                else:
                    if over_game_time - start_game_time - player_1.coins < best_score[2]:
                        best_score[0] = over_game_time - start_game_time
                        best_score[1] = player_1.coins
                        best_score[2] = over_game_time - start_game_time - player_1.coins * 1000
                level = "menu"



class Snake(Object):
    def __init__(self, x_pos, y_pos, pos_2):
        super().__init__(x_pos, y_pos)
        self.position_1 = self.x_position
        self.position_2 = (pos_2 * b_size) - b_size

        self.side = "r"

        self.default = snake_default
        self.snake_1 = snake_1
        self.snake_2 = snake_2
        self.snake_3 = snake_3

        self.going = [self.default, self.default, self.default, self.default, self.default, self.snake_1, self.snake_1, self.snake_1, self.snake_1, self.snake_1, self.snake_2, self.snake_2, self.snake_2, self.snake_2, self.snake_2, self.snake_3, self.snake_3, self.snake_3, self.snake_3, self.snake_3]



    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def Move(self):
        for _ in range(3):
            if self.side == "r":
                if self.MakeSelfRect().left + move_scene_x != self.position_2:
                    self.x_position += 1
                else:
                    self.side = "l"

            else:
                if self.MakeSelfRect().left + move_scene_x != self.position_1:
                    self.x_position -= 1
                else:
                    self.side = "r"
        # if self.side == "r":
        #     for i in range(3):
        #         if not self.ObjectRight(self.MakeSelfRect()) and self.FallRight(self.MakeSelfRect()):
        #             if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
        #                 self.side = "l"
        #             else:
        #                 self.x_position += 1
        #         else:
        #             self.side = "l"
        #
        # if self.side == "l":
        #     for i in range(3):
        #         if not self.ObjectLeft(self.MakeSelfRect()) and self.FallLeft(self.MakeSelfRect()):
        #             if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
        #                 self.side = "r"
        #             else:
        #                 self.x_position -= 1
        #         else:
        #             self.side = "r"

class Mushroom(Object):
    def __init__(self, x_pos, y_pos, pos_2):
        super().__init__(x_pos, y_pos)
        self.position_1 = self.x_position
        self.position_2 = (pos_2 * b_size) - b_size

        self.side = "r"

        self.default = mushroom_default
        self.mushroom_1 = mushroom_1
        self.mushroom_2 = mushroom_2
        self.mushroom_3 = mushroom_3
        self.mushroom_4 = mushroom_4
        self.mushroom_5 = mushroom_5
        self.mushroom_6 = mushroom_6
        self.mushroom_7 = mushroom_7

        self.going = [self.default, self.default,
                        self.mushroom_1, self.mushroom_1,
                        self.mushroom_2, self.mushroom_2,
                        self.mushroom_3, self.mushroom_3,
                        self.mushroom_4, self.mushroom_4,
                        self.mushroom_5, self.mushroom_5,
                        self.mushroom_6, self.mushroom_6,
                        self.mushroom_7, self.mushroom_7
                      ]



        # while not self.ObjectLeft(self.MakeSelfRect()) and self.FallLeft(self.MakeSelfRect()):
        #     self.x_position -= 1
        # self.position_1 = self.x_position
        #
        # while not self.ObjectRight(self.MakeSelfRect()) and self.FallRight(self.MakeSelfRect()):
        #     self.x_position += 1
        # self.position_2 = self.x_position

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def Move(self):
        for _ in range(5):
            if self.side == "r":
                if self.MakeSelfRect().left + move_scene_x != self.position_2:
                    self.x_position += 1
                else:
                    self.side = "l"

            else:
                if self.MakeSelfRect().left + move_scene_x != self.position_1:
                    self.x_position -= 1
                else:
                    self.side = "r"

        # if self.side == "r":
        #     for i in range(4):
        #         if not self.ObjectRight(self.MakeSelfRect()) and self.FallRight(self.MakeSelfRect()):
        #             self.x_position += 1
        #             # if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
        #             #     self.side = "l"
        #             # else:
        #             #     self.x_position += 1
        #         else:
        #             self.side = "l"
        #
        # if self.side == "l":
        #     for i in range(4):
        #         if not self.ObjectLeft(self.MakeSelfRect()) and self.FallLeft(self.MakeSelfRect()):
        #             self.x_position -= 1
        #             # if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
        #             #     self.side = "r"
        #             # else:
        #             #     self.x_position -= 1
        #         else:
        #             self.side = "r"

class Horse(Object):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.lives = 4

        self.size_x = b_size * 2
        self.size_y = b_size + b_size // 2

        self.side = "r"

        self.run_1 = horse_run_1
        self.run_2 = horse_run_1
        self.run_3 = horse_run_1
        self.run_4 = horse_run_1
        self.run_5 = horse_run_1
        self.run_6 = horse_run_1

        self.hit_1 = horse_hit_1
        self.hit_2 = horse_hit_2
        self.hit_3 = horse_hit_2
        self.hit_4 = horse_hit_2
        self.hit_5 = horse_hit_2

        self.default = self.run_1

        self.run = [self.run_1] * 3 + [self.run_2] * 3 + [self.run_3] * 3 + [self.run_4] * 3 + [self.run_5] * 3 + [self.run_6] * 3
        self.hit = [self.hit_1, self.hit_2, self.hit_3, self.hit_4, self.hit_5]

        self.default_to_die = False



    def CheckMode(self):
        if self.side == "r":
            if player_1.MakeSelfRect().left <= self.MakeSelfRect().right + b_size and player_1.MakeSelfRect().left >= self.MakeSelfRect().right and player_1.MakeSelfRect().top < self.MakeSelfRect().bottom and player_1.MakeSelfRect().bottom > self.MakeSelfRect().top:
                if self.default not in self.hit:
                    self.default = self.hit_1
            else:
                pass
                # self.mode = "run"

        elif self.side == "l":
            if player_1.MakeSelfRect().right >= self.MakeSelfRect().left - b_size and player_1.MakeSelfRect().right <= self.MakeSelfRect().left and player_1.MakeSelfRect().top < self.MakeSelfRect().bottom and player_1.MakeSelfRect().bottom > self.MakeSelfRect().top:
                if self.default not in self.hit:
                    self.default = self.hit_1
            else:
                pass
                # self.mode = "run"

        # return self.mode

    def ChangeDefault(self):
        if self.default in self.run:
            self.default = self.run[0]
            self.run.append(self.run[0])
            self.run.pop(0)
            # self.default not in self.hit

        else:
            if self.default == self.hit_1:
                self.default = self.hit_2
            elif self.default == self.hit_2:
                self.default = self.hit_3
            elif self.default == self.hit_3:
                self.default = self.hit_4
            elif self.default == self.hit_4:
                self.default = self.hit_5
            elif self.default == self.hit_5:
                self.default = self.run[0]
                self.run.append(self.run[0])
                self.run.pop(0)
            # if self.side == "r":
            #     self.default = pygame.transform.flip(self.hit[0], True, False)
            # else:
            #     self.default = self.hit[0]
            # self.hit.append(self.hit[0])
            # self.hit.pop(0)

    def MakeSelfRect(self):
        if self.side == "r":
            return self.default.get_rect(bottomleft=(self.x_position - move_scene_x, self.y_position - move_scene_y))
        else:
            return self.default.get_rect(bottomright=(self.x_position - move_scene_x + self.size_x, self.y_position - move_scene_y))

    def Move(self):
        if self.default not in self.hit:
            if self.side == "r":
                for i in range(2):
                    if not self.ObjectRight(self.MakeSelfRect()) and self.FallRight(self.MakeSelfRect()):
                        if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
                            self.side = "l"
                        else:
                            self.x_position += 1
                    else:
                        self.side = "l"

            elif self.side == "l":
                for i in range(2):
                    if not self.ObjectLeft(self.MakeSelfRect()) and self.FallLeft(self.MakeSelfRect()):
                        if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
                            self.side = "r"
                        else:
                            self.x_position -= 1
                    else:
                        self.side = "r"

        else:
            if self.side == "r":
                pass

            elif self.side == "l":
                pass

class Mummy(Object):
    def __init__(self, x_pos, y_pos, pos_1, pos_2):
        super().__init__(x_pos, y_pos)

        self.position_1 = (pos_1 * b_size) - b_size
        self.position_2 = (pos_2 * b_size) - b_size

        self.size_x = b_size * 1.5
        self.size_y = b_size * 2

        self.lives = 5

        self.mode = "run"

        self.side = "l"

        self.run_1 = mum_run_1
        self.run_2 = mum_run_2
        self.run_3 = mum_run_3
        self.run_4 = mum_run_4
        self.run_5 = mum_run_5
        self.run_6 = mum_run_6

        self.hit_1 = mum_hit_1
        self.hit_2 = mum_hit_2
        self.hit_3 = mum_hit_3
        self.hit_4 = mum_hit_4
        self.hit_5 = mum_hit_5

        self.stand_1 = mum_stand_1
        self.stand_2 = mum_stand_2

        self.default = self.run_1

        self.run = [self.run_1] * 3 + [self.run_2] * 3 + [self.run_3] * 3 + [self.run_4] * 3 + [self.run_5] * 3 + [self.run_6] * 3
        # + [self.run_3] * 3 + [self.run_4] * 3 + [self.run_5] * 3 + [self.run_6] * 3
        self.hit = [self.hit_1, self.hit_2, self.hit_3, self.hit_4, self.hit_5]

        self.default_to_die = False



    def CheckMode(self):
        if self.side == "r":
            if player_1.MakeSelfRect().left <= self.MakeSelfRect().right + 35 and player_1.MakeSelfRect().left >= self.MakeSelfRect().right and player_1.MakeSelfRect().top < self.MakeSelfRect().bottom and player_1.MakeSelfRect().bottom > self.MakeSelfRect().top:
                if self.default not in self.hit:
                    self.default = self.hit_1
            else:
                pass
                # self.mode = "run"

        elif self.side == "l":
            if player_1.MakeSelfRect().right >= self.MakeSelfRect().left - 35 and player_1.MakeSelfRect().right <= self.MakeSelfRect().left and player_1.MakeSelfRect().top < self.MakeSelfRect().bottom and player_1.MakeSelfRect().bottom > self.MakeSelfRect().top:
                if self.default not in self.hit:
                    self.default = self.hit_1
            else:
                pass
                # self.mode = "run"

        # return self.mode

    def ChangeDefault(self):
        if self.default in self.run:
            self.default = self.run[0]
            self.run.append(self.run[0])
            self.run.pop(0)
            # self.default not in self.hit

        else:
            if self.default == self.hit_1:
                self.default = self.hit_2
            elif self.default == self.hit_2:
                self.default = self.hit_3
            elif self.default == self.hit_3:
                self.default = self.hit_4
            elif self.default == self.hit_4:
                self.default = self.hit_5
            elif self.default == self.hit_5:
                self.default = self.run[0]
                self.run.append(self.run[0])
                self.run.pop(0)
            # if self.side == "r":
            #     self.default = pygame.transform.flip(self.hit[0], True, False)
            # else:
            #     self.default = self.hit[0]
            # self.hit.append(self.hit[0])
            # self.hit.pop(0)

    def MakeSelfRect(self):
        if self.side == "r":
            return self.default.get_rect(bottomleft=(self.x_position - move_scene_x, self.y_position - move_scene_y))
        else:
            return self.default.get_rect(bottomright=(self.x_position - move_scene_x + self.size_x, self.y_position - move_scene_y))

    def Move(self):
        if self.default not in self.hit:
            if self.side == "r":
                for i in range(3):
                    if self.MakeSelfRect().left + move_scene_x != self.position_2:
                        if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
                            self.side = "l"
                        else:
                            self.x_position += 1
                    else:
                        self.side = "l"
                        self.x_position -= 30


            elif self.side == "l":
                for i in range(3):
                    if self.MakeSelfRect().right - move_scene_x != self.position_1:
                        if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
                            self.side = "r"
                        else:
                            self.x_position -= 1
                    else:
                        self.side = "r"
                        self.x_position += 30

        else:
            if self.side == "r":
                pass

            elif self.side == "l":
                pass



class FlyPlat(Object):
    def __init__(self, x_pos, y_pos, pos, fly, num = 5):
        super().__init__(x_pos, y_pos)

        # self.position_1 = (pos_1 * b_size) - b_size
        # self.position_2 = 700 - ((pos_2 * b_size) - b_size)

        self.work = objects_on

        self.transparency = 125

        self.fly = fly
        self.num = num

        if fly == "RightLeft":
            self.position_1 = self.x_position
            self.position_2 = (pos * b_size) - b_size
            self.direction = "r"
        else:
            self.position_1 = self.y_position
            self.position_2 = 700 - ((pos * b_size) - b_size)
            self.direction = "d"


        self.default = fly_plat_default
        self.fly_plat_1 = fly_plat_1
        self.fly_plat_2 = fly_plat_2
        self.fly_plat_3 = fly_plat_3

        self.going = [self.default, self.default, self.fly_plat_1, self.fly_plat_1,
                           self.fly_plat_2, self.fly_plat_2, self.fly_plat_3, self.fly_plat_3]

        self.default_2 = fly_plat_default_2


    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def MakeSelfRectFruit(self):
        return self.default_2.get_rect(bottomleft=(self.x_position - move_scene_x + b_size // 3, self.y_position - move_scene_y - b_size // 20))

    def Move(self):
        if self.work:
            global fall_jump
            global player_1
            for x in range(self.num):
                if self.fly == "UpDown":
                    if self.MakeSelfRect().bottom == player_1.MakeSelfRect().top and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left:
                        fall_jump = -1
                    if self.direction == "u":
                        if self.MakeSelfRect().top == player_1.MakeSelfRect().bottom and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left:
                            if player_1.ObjectUp(player_1.MakeSelfRect()):
                                self.direction = "d"
                                reset()
                    else:
                        if self.MakeSelfRect().bottom == player_1.MakeSelfRect().top and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left:
                            self.direction = "u"
                            fall_jump = -1
                        if self.MakeSelfRect().bottom == player_1.MakeSelfRect().top and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left:
                            if player_1.ObjectDown(player_1.MakeSelfRect()):
                                self.direction = "u"
                                reset()

                if self.fly == "RightLeft":
                    if self.direction == "r":
                        if self.MakeSelfRect().left + move_scene_x != self.position_2:
                            self.x_position += 1
                            if self.MakeSelfRect().top == player_1.MakeSelfRect().bottom and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left:
                                player_1.MoveRight(1)
                                # player_1.x_position += 1
                        else:
                            self.direction = "l"

                    if self.direction == "l":
                        if self.MakeSelfRect().left + move_scene_x != self.position_1:
                            self.x_position -= 1
                            if self.MakeSelfRect().top == player_1.MakeSelfRect().bottom and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left:
                                player_1.MoveLeft(1)
                                # player_1.x_position -= 1
                        else:
                            self.direction = "r"
                else:
                    if self.direction == "d":
                        if self.MakeSelfRect().bottom + move_scene_y != self.position_2:
                            if self.MakeSelfRect().top == player_1.MakeSelfRect().bottom and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left:
                                player_1.Move_Up_Down(1)
                                fall_jump = 0
                            self.y_position += 1
                        else:
                            self.direction = "u"

                    if self.direction == "u":
                        if self.MakeSelfRect().bottom + move_scene_y != self.position_1:
                            if self.MakeSelfRect().top == player_1.MakeSelfRect().bottom and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left:
                                player_1.Move_Up_Down(-1)
                                fall_jump = 0
                            self.y_position -= 1
                        else:
                            self.direction = "d"

class JumpPad(Object):

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.work = objects_on

        self.transparency = 125

        self.jump_pad_1 = jump_pad_1
        self.jump_pad_2 = jump_pad_2
        self.jump_pad_3 = jump_pad_3
        self.jump_pad_4 = jump_pad_4
        self.jump_pad_5 = jump_pad_5
        self.default_2 = jump_pad_default_2

        self.default = self.jump_pad_1


    def MakeSelfImage(self):
        return self.default

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def MakeSelfRectFruit(self):
        return self.default_2.get_rect(bottomleft=(self.x_position - move_scene_x + b_size // 3, self.y_position - move_scene_y - b_size // 10))

    def CheckJump(self):
        if self.work:
            global fall_jump
            if self.MakeSelfRect().top == player_1.MakeSelfRect().bottom and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left and self.default == self.jump_pad_1:
                self.default = self.jump_pad_4
                fall_jump = 40

            elif self.default == self.jump_pad_1:
                pass
            elif self.default == self.jump_pad_2:
                self.default = self.jump_pad_1
            elif self.default == self.jump_pad_3:
                self.default = self.jump_pad_2
            elif self.default == self.jump_pad_4:
                self.default = self.jump_pad_3

class ExpandPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos, pos_2):
        super().__init__(x_pos, y_pos)
        self.position_2 = (pos_2 * b_size) - b_size
        self.original_x = self.x_position

        self.y_position -= b_size - b_size / 5

        self.work = objects_on

        self.transparency = 125

        self.stop_i = expand_plat_i
        self.i = expand_plat_i

        self.original = expand_plat_original
        self.default = expand_plat_default
        self.default_2 = expand_plat_default_2

        while self.MakeSelfRect().right <= self.position_2 - move_scene_x:
            self.x_position += 1
        self.stop_i = self.x_position - self.original_x

        self.x_position = self.original_x


    def MakeSelfRect(self):
        return self.default.get_rect(bottomleft=(self.x_position - move_scene_x, self.y_position - move_scene_y))

    def MakeSelfRectFruit(self):
        return self.default_2.get_rect(bottomleft=(self.x_position - move_scene_x + b_size // 8, self.y_position - move_scene_y))

    def CheckWork(self):
        if self.work:
            self.default = pygame.transform.scale(self.original, (self.i, b_size / 5))
            for i in range(5):
                if self.i < self.stop_i:
                    self.i += 1



class Spike(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos, sz = 2):
        super().__init__(x_pos, y_pos)

        self.size = sz

        self.default = spike_default
        self.default = pygame.transform.scale(self.default, (b_size / self.size, b_size / self.size))


    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class Saw(Object):

    def __init__(self, x_pos, y_pos, sz):
        super().__init__(x_pos, y_pos)

        self.size = sz

        self.saw_1 = saw_1
        self.saw_1 = pygame.transform.scale(self.saw_1, (b_size * self.size , b_size * self.size))
        self.saw_2 = saw_2
        self.saw_2 = pygame.transform.scale(self.saw_2, (b_size * self.size , b_size * self.size))
        self.saw_3 = saw_3
        self.saw_3 = pygame.transform.scale(self.saw_3, (b_size * self.size , b_size * self.size))
        self.saw_4 = saw_4
        self.saw_4 = pygame.transform.scale(self.saw_4, (b_size * self.size , b_size * self.size))
        self.saw_5 = saw_5
        self.saw_5 = pygame.transform.scale(self.saw_5, (b_size * self.size , b_size * self.size))
        self.saw_6 = saw_6
        self.saw_6 = pygame.transform.scale(self.saw_6, (b_size * self.size , b_size * self.size))
        self.saw_7 = saw_7
        self.saw_7 = pygame.transform.scale(self.saw_7, (b_size * self.size , b_size * self.size))
        self.saw_8 = saw_8
        self.saw_8 = pygame.transform.scale(self.saw_8, (b_size * self.size , b_size * self.size))

        self.going = [self.saw_1, self.saw_2, self.saw_3, self.saw_4, self.saw_5, self.saw_6, self.saw_7, self.saw_8]

        self.default = self.saw_1


    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class Siked_Ball(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.fall = False

        self.gravity_pull = 0

        self.default = saw_default
        self.default = pygame.transform.scale(self.default, (b_size * 1.5, b_size * 1.5))


    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def CheckFall(self):
        if not self.fall:
            if player_1.rect.right >= self.MakeSelfRect().left and not self.ObjectDown(self.MakeSelfRect()):
                self.fall = True
        if self.ObjectDown(self.MakeSelfRect()):
            self.fall = False
        if self.fall:
            self.gravity_pull += 4
            for i in range(self.gravity_pull):
                if not self.ObjectDown(self.MakeSelfRect()):
                    self.y_position += 1

class Fire(Object):

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.stage_off = pygame.image.load("fire_stage_off.png")
        self.stage_off = pygame.transform.scale(self.stage_off, (b_size , b_size))

        self.stage_on = pygame.image.load("fire_stage_on.png")
        self.stage_on = pygame.transform.scale(self.stage_on, (b_size , b_size))

        self.fire_1 = pygame.image.load("fire_1.png")
        self.fire_1 = pygame.transform.scale(self.fire_1, (b_size , b_size))
        self.fire_2 = pygame.image.load("fire_2.png")
        self.fire_2 = pygame.transform.scale(self.fire_2, (b_size , b_size))
        self.fire_3 = pygame.image.load("fire_3.png")
        self.fire_3 = pygame.transform.scale(self.fire_3, (b_size , b_size))

        self.going = [self.fire_1, self.fire_1, self.fire_2, self.fire_2, self.fire_3, self.fire_3]

        self.default = self.stage_off

        self.delay = 1500
        self.delay_after = 3000

        self.start = 0
        self.over = 0

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def MakeSelfRectFire(self):
        return self.fire_1.get_rect(bottomleft=(self.x_position - move_scene_x, self.y_position - b_size - move_scene_y))

    def CheckOn(self):
        self.now = pygame.time.get_ticks()
        if self.MakeSelfRect().top == player_1.MakeSelfRect().bottom and self.MakeSelfRect().left < player_1.MakeSelfRect().right and self.MakeSelfRect().right > player_1.MakeSelfRect().left:
            if self.start == 0:
                self.start = pygame.time.get_ticks()
        # else:
        #     if self.over == 0:
        #         self.over = pygame.time.get_ticks()

        if self.over + self.delay_after <= self.now and self.over != 0:
            self.start = 0
            self.over = 0

        if self.start + self.delay <= self.now and self.start != 0:
            self.default = self.stage_on
            if self.over == 0:
                self.over = pygame.time.get_ticks()
        else:
            self.default = self.stage_off
            self.over = 0



class Fruit(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos, nm):
        super().__init__(x_pos, y_pos)

        self.x_position += b_size / 3
        self.y_position -= b_size / 3

        self.original_y = self.y_position

        self.name = nm

        if  self.name == "a":
            self.default = fruit_apple
        elif  self.name == "b":
            self.default = fruit_banana
        elif  self.name == "c":
            self.default = fruit_cherry

        # self.default = pygame.transform.scale(self.default, (b_size / 3, b_size / 3))

        self.go = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]


    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class Coin(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.x_position += b_size / 4
        self.y_position -= b_size / 4

        self.original_y = self.y_position

        self.default = coin_default

        self.go = [1, 1, 1, 1,  2, 2, 2, 2,  3, 3, 3, 3,  4, 4, 4, 4,  3, 3, 3, 3,  2, 2, 2, 2]


    def MakeSelfRect(self):
        return self.MakeRect(self.default)



class Box(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.gravity_pull = 0

        self.default = box_default

        self.MakeSides()

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def CheckFall(self):
        self.MakeSides()

        if not self.ObjectDown(self.MakeSelfRect()):
            self.gravity_pull += 3
        else:
            self.gravity_pull = 0

        for i in range(self.gravity_pull):
            if not self.ObjectDown(self.MakeSelfRect()):
                self.y_position += 1



# player_1 = Player(0, 0)
# check_p_1 = Checkpoint(0, 0)


def blit():
    """Blits all the objects"""
    global player_1

    screen.blit(blue_sky, blue_sky_rect)

    for x in saws:
        if check_visible(x):
            screen.blit(x.going[0], x.MakeSelfRect())
            x.going.append(x.going[0])
            x.going.pop(0)

    for i in range(len(list_grs)):
        if check_visible(list_grs[i]):
            if list_grounds_decide[i] == "grass":
                screen.blit(list_grs[i].grass, list_grs[i].MakeSelfRect())
            elif list_grounds_decide[i] == "ground":
                screen.blit(list_grs[i].default, list_grs[i].MakeSelfRect())

    for x in set(touch_objects) - set(list_grs) - set(fly_plats) - set(jump_pads) - set(expand_plats):
        if check_visible(x):
            screen.blit(x.default, x.MakeSelfRect())

    for x in spikes + spiked_balls:
        if check_visible(x):
            screen.blit(x.default, x.MakeSelfRect())

    for x in fires:
        if x.default == x.stage_on:
            if check_visible(x):
               screen.blit(x.going[0], x.MakeSelfRect())
               x.going.append(x.going[0])
               x.going.pop(0)


    for x in start_games:
        if x.default == x.start_arrow:
            if check_visible(x):
               screen.blit(x.start_arrow, x.MakeSelfRect())

    for x in check_ps:
        if x.checkpoint_TF:
            screen.blit(x.checkpointing[0], x.MakeSelfRect())
            x.checkpointing.append(x.checkpointing[0])
            x.checkpointing.pop(0)
        else:
            screen.blit(x.no_checkpoint, x.MakeSelfRect())


    for x in snakes + mushrooms:
        if check_visible(x):
            if x.side == "l":
                screen.blit(x.going[0], x.MakeSelfRect())
            if x.side == "r":
                screen.blit(pygame.transform.flip(x.going[0], True, False), x.MakeSelfRect())
            x.going.append(x.going[0])
            x.going.pop(0)

    for x in horses + mummys:
        if check_visible(x):
            if x.side == "r":
                screen.blit(pygame.transform.flip(x.default, True, False), x.MakeSelfRect())
            else:
                screen.blit(x.default, x.MakeSelfRect())


    for x in fly_plats:
        if check_visible(x):
            if x.work:
                x.going[0].set_alpha(255)
                screen.blit(x.going[0], x.MakeSelfRect())
            else:
                x.going[0].set_alpha(x.transparency)
                screen.blit(x.going[0], x.MakeSelfRect())
                screen.blit(x.default_2, x.MakeSelfRectFruit())
            x.going.append(x.going[0])
            x.going.pop(0)

    for x in jump_pads:
        if check_visible(x):
            if x.work:
                x.default.set_alpha(255)
                screen.blit(x.default, x.MakeSelfRect())
            else:
                x.default.set_alpha(x.transparency)
                screen.blit(x.default, x.MakeSelfRect())
                screen.blit(x.default_2, x.MakeSelfRectFruit())

    for x in expand_plats:
        if check_visible(x):
            if x.work:
                x.default.set_alpha(255)
                screen.blit(x.default, x.MakeSelfRect())
            else:
                x.default.set_alpha(x.transparency)
                screen.blit(x.default, x.MakeSelfRect())
                screen.blit(x.default_2, x.MakeSelfRectFruit())


    find_find_mode = find_mode()

    if find_find_mode == "stand":
        player_1.standing[0].set_alpha(player_1.transparency)
        if side == "r":
            screen.blit(player_1.standing[0], player_1.MakeSelfRect())
        else:
            screen.blit(pygame.transform.flip(player_1.standing[0], True, False), player_1.MakeSelfRect())
        player_1.standing.append(player_1.standing[0])
        player_1.standing.pop(0)

    elif find_find_mode == "run":
        player_1.running[0].set_alpha(player_1.transparency)
        if side == "r":
            screen.blit(player_1.running[0], player_1.MakeSelfRect())
        else:
            screen.blit(pygame.transform.flip(player_1.running[0], True, False), player_1.MakeSelfRect())
        player_1.running.append(player_1.running[0])
        player_1.running.pop(0)

    elif find_find_mode == "jump":
        player_1.jump.set_alpha(player_1.transparency)
        player_1.running = [player_1.run_1, player_1.run_2, player_1.run_3, player_1.run_4, player_1.run_5, player_1.run_6, player_1.run_7, player_1.run_8]
        if side == "r":
            screen.blit(player_1.jump, player_1.MakeSelfRect())
        else:
            screen.blit(pygame.transform.flip(player_1.jump, True, False), player_1.MakeSelfRect())

    elif find_find_mode == "fall":
        player_1.fall.set_alpha(player_1.transparency)
        player_1.running = [player_1.run_1, player_1.run_2, player_1.run_3, player_1.run_4, player_1.run_5, player_1.run_6, player_1.run_7, player_1.run_8]
        if side == "r":
            screen.blit(player_1.fall, player_1.MakeSelfRect())
        else:
            screen.blit(pygame.transform.flip(player_1.fall, True, False), player_1.MakeSelfRect())

    elif find_find_mode == "wall":
        player_1.wall_jump.set_alpha(player_1.transparency)
        player_1.running = [player_1.run_1, player_1.run_2, player_1.run_3, player_1.run_4, player_1.run_5, player_1.run_6, player_1.run_7, player_1.run_8]
        if side == "r":
            screen.blit(player_1.wall_jump, player_1.MakeSelfRect())
        else:
            screen.blit(pygame.transform.flip(player_1.wall_jump, True, False), player_1.MakeSelfRect())


    for x in fruits + coins:
        if check_visible(x):
            x.y_position = x.original_y + x.go[0]
            screen.blit(x.default, x.MakeSelfRect())
            x.go.append(x.go[0])
            x.go.pop(0)


    screen.blit(apple, apple_rect)
    screen.blit(banana, banana_rect)
    screen.blit(cherry, cherry_rect)
    screen.blit(coin_1, coin_1_rect)

    global apples, bananas, cherries, coins_not_list, apples_count, apples_count_rect, banana_count, banana_count_rect, cherry_count, cherry_count_rect, coin_count, coin_count_rect

    if apples != player_1.apples:
        apples = player_1.apples
        apples_count = text.render(f"{player_1.apples}", True, 'Black')
        apples_count_rect = apples_count.get_rect(topleft=(340, 5))
    screen.blit(apples_count, apples_count_rect)

    if bananas != player_1.bananas:
        bananas = player_1.bananas
        banana_count = text.render(f"{player_1.bananas}", True, 'Black')
        banana_count_rect = apples_count.get_rect(topleft=(490, 5))
    screen.blit(banana_count, banana_count_rect)

    if cherries != player_1.cherries:
        cherries = player_1.cherries
        cherry_count = text.render(f"{player_1.cherries}", True, 'Black')
        cherry_count_rect = cherry_count.get_rect(topleft=(640, 5))
    screen.blit(cherry_count, cherry_count_rect)

    if coins_not_list != player_1.coins:
        coins_not_list = player_1.coins
        coin_count = text.render(f"{player_1.coins}", True, 'Black')
        coin_count_rect = coin_count.get_rect(topleft=(890, 5))
    screen.blit(coin_count, coin_count_rect)

    screen.blit(go_back_button, go_back_button_rect)
    screen.blit(restart_button, restart_button_rect)

def keys_pressed():
    """What happens when keys are pressed"""
    global fall_jump, move_scene_y
    keys = pygame.key.get_pressed()
    find_find_mode = find_mode()
    object_down = player_1.ObjectDown(player_1.MakeSelfRect())
    if keys[pygame.K_RIGHT]:
        if find_find_mode == "wall":
            fall_jump = 0
            if not object_down:
                check_die()
                if player_1.MakeSelfRect().centery > 350:
                    player_1.y_position += 1
                elif move_scene_y == 0 and player_1.MakeSelfRect().centery <= 350 and player_1.MakeSelfRect().bottom != 0:
                    player_1.y_position += 1
                elif move_scene_y < 0:
                    move_scene_y += 1
        else:
            player_1.MoveRight()

    if keys[pygame.K_LEFT]:
        if find_find_mode == "wall":
            fall_jump = 0
            if not object_down:
                check_die()
                if player_1.MakeSelfRect().centery > 350:
                    player_1.y_position += 1
                elif move_scene_y == 0 and player_1.MakeSelfRect().centery <= 350 and player_1.MakeSelfRect().bottom != 0:
                    player_1.y_position += 1
                elif move_scene_y < 0:
                    move_scene_y += 1
        else:
            player_1.MoveLeft()

    if keys[pygame.K_UP] and object_down:
        fall_jump = 28

    elif keys[pygame.K_UP] and not object_down and fall_jump == 0 and find_find_mode == "wall":
        fall_jump = 17

def find_mode():
    global mode
    global side
    keys = pygame.key.get_pressed()
    object_right = player_1.ObjectRight(player_1.MakeSelfRect())
    object_left = player_1.ObjectLeft(player_1.MakeSelfRect())
    object_down = player_1.ObjectDown(player_1.MakeSelfRect())
    player_1_rect = player_1.MakeSelfRect()
    if keys[pygame.K_RIGHT]:
        side = "r"
        if object_down:
            if object_right:
                mode = "stand"
            else:
                mode = "run"
        if not object_down and object_right:
            mode = "wall"
        if not object_down and not object_right:
            if fall_jump >= 0:
                mode = "jump"
            else:
                mode = "fall"

        for x in boxes:
            if player_1_rect.right == x.MakeSelfRect().left and player_1_rect.bottom > x.MakeSelfRect().top and player_1_rect.top < x.MakeSelfRect().bottom:
                if not x.ObjectRight(x.MakeSelfRect()):
                    mode = "run"


    elif keys[pygame.K_LEFT]:
        side = "l"
        if object_down:
            if object_left:
                mode = "stand"
            else:
                mode = "run"
        if not object_down and object_left:
            mode = "wall"
        if not object_down and not object_left:
            if fall_jump >= 0:
                mode = "jump"
            else:
                mode = "fall"

        for x in boxes:
            if player_1_rect.left == x.MakeSelfRect().right and player_1_rect.bottom > x.MakeSelfRect().top and player_1.MakeSelfRect().top < x.MakeSelfRect().bottom:
                if not x.ObjectLeft(x.MakeSelfRect()):
                    mode = "run"

    else:
        mode = "stand"

    if fall_jump > 0:
        mode = "jump"
    elif fall_jump < 0 and not object_left and not object_right:
        mode = "fall"

    return mode

def start_play():
    global list_grounds_decide
    global checkpoints
    global fall_jump
    global move_scene_x
    global move_scene_y
    global mode
    global side
    global start_games
    global check_ps
    global end_games
    global player_1
    global snakes
    global mushrooms
    global horses
    global mummys
    global fly_plats
    global jump_pads
    global spikes
    global saws
    global expand_plats
    global spiked_balls
    global fires
    global fruits
    global coins
    global list_grs
    global boxes
    global touch_objects
    global start_game_time
    global apples, bananas, cherries, coins_not_list

    # variables
    # -------------------------
    start_game_time = pygame.time.get_ticks()
    fall_jump = 0
    move_scene_x = 0
    move_scene_y = 0
    mode = "fall"
    side = "r"
    checkpoints = 0
    apples = -1
    bananas = -1
    cherries = -1
    coins_not_list = -1
    # -------------------------

    list_grs = [
        Ground(1, 2),
        Ground(2, 2),
        Ground(3, 2),
        Ground(4, 1),
        Ground(5, 1),
        Ground(6, 1),
        Ground(7, 1),
        Ground(8, 1),
        Ground(9, 1),
        Ground(10, 1),
        Ground(11, 1),
        Ground(9, 2),
        Ground(10, 3),
        Ground(11, 4),
        Ground(17, 2),
        Ground(16, 3),
        Ground(15, 4),
        Ground(15, 1),
        Ground(16, 1),
        Ground(17, 1),
        Ground(18, 1),
        Ground(19, 1),
        Ground(20, 1),
        Ground(21, 2),
        Ground(22, 3),
        Ground(23, 3),
        Ground(24, 3),
        Ground(25, 3),
        Ground(26, 3),
        Ground(26, 2),
        Ground(27, 2),
        Ground(28, 2),
        Ground(29, 2),
        Ground(30, 2),
        Ground(31, 4),
        Ground(32, 4),
        Ground(33, 3),
        Ground(34, 2),
        Ground(35, 2),
        Ground(36, 1),
        Ground(37, 1),
        Ground(38, 1),
        Ground(39, 1),
        Ground(40, 1),
        Ground(41, 1),
        Ground(42, 1),
        Ground(43, 1),
        Ground(44, 1),
        Ground(45, 1),
        Ground(46, 1),
        Ground(47, 1),
        Ground(48, 1),
        Ground(49, 1),
        Ground(50, 2),
        Ground(51, 2),
        Ground(52, 3),
        Ground(53, 1),
        Ground(54, 1),
        Ground(55, 1),
        Ground(56, 1),
        Ground(57, 1),
        Ground(58, 1),
        Ground(59, 2),
        Ground(60, 2),
        Ground(61, 7),
        Ground(62, 7),
        Ground(63, 7),
        Ground(64, 7),
        Ground(65, 1),
        Ground(66, 1),
        Ground(67, 1),
        Ground(68, 1),
        Ground(69, 1),
        Ground(70, 1),
        Ground(71, 8),
        Ground(72, 7),
        Ground(72, 8),
        Ground(73, 8),
        Ground(72, 3),
        Ground(73, 2),
        Ground(74, 1),
        Ground(75, 1),
        Ground(110, 1),
        Ground(111, 3),
        Ground(112, 4),
        Ground(113, 5),
        Ground(114, 6),
        Ground(115, 6),
        Ground(116, 5),
        Ground(117, 3),
        Ground(118, 2),
        Ground(119, 2),
        Ground(120, 2),
        Ground(127, 2),
        Ground(128, 2),
        Ground(129, 2),
        Ground(130, 3),
        Ground(131, 4),
        Ground(132, 6),
        Ground(133, 5),
        Ground(133, 6),
        Ground(133, 7),
        Ground(134, 6),
        Ground(134, 7),
        Ground(134, 8),
        Ground(133, 1),
        Ground(134, 1),
        Ground(135, 1),
        Ground(136, 1),
        Ground(137, 1),
        Ground(138, 1),
        Ground(139, 1),
        Ground(140, 1),
        Ground(141, 1),
        Ground(142, 1),
        Ground(143, 1),
                ]

    plats = [
        SilverThickPlat(7, 8),
        SilverThickPlat(6, 8),

        SilverThickPlat(13, 10),
        SilverThickPlat(14, 10),

        SilverThickPlat(15, 13),
        SilverThickPlat(16, 13),

        SilverThickPlat(27, 13),
        SilverThickPlat(28, 13),
        SilverThickPlat(29, 13),

        SilverThickPlat(23, 6),
        SilverThickPlat(24, 6),
        SilverThickPlat(25, 6),

        OrangeThickPlat(89, 12),
        OrangeThickPlat(90, 12),
        OrangeThickPlat(89, 16),
        OrangeThickPlat(90, 16),

        OrangeThickPlat(93, 14),
        OrangeThickPlat(94, 14),
        OrangeThickPlat(93, 18),
        OrangeThickPlat(94, 18),

        SilverThinPlat(98, 18),
        SilverThinPlat(99, 18),
        SilverThinPlat(100, 18),
        SilverThinPlat(101, 18),
        SilverThinPlat(102, 18),
        SilverThinPlat(103, 18),
        SilverThinPlat(104, 18),
        SilverThinPlat(105, 18),
        SilverThinPlat(106, 18),

        BrownThickPlat(108, 15),
        BrownThickPlat(109, 15),

        BrownThickPlat(110, 12),
        BrownThickPlat(111, 12),

        BrownThickPlat(112, 9),
        BrownThickPlat(113, 9),

        OrangeThickPlat(73, 7),
        OrangeThickPlat(72, 6),

        OrangeThickPlat(134, 5),
        OrangeThickPlat(133, 4),
            ]

    list_blocks = [
        GoldBlock(40, 5),
        GoldBlock(41, 5),
        GoldBlock(42, 5),
        GoldBlock(43, 5),
        GoldBlock(39, 6),
        GoldBlock(44, 6),
        SmallSilverBlock(39.5, 5.5),
        SmallSilverBlock(44, 5.5),

        BrickBlock(49, 6),
        BrickBlock(50, 6),
        BrickBlock(51, 6),
        BrickBlock(52, 6),
        BrickBlock(53, 6),

        SmallSilverBlock(60.5, 7.5),

        BrownBlock(62, 1),
        BrownBlock(62, 2),
        BrownBlock(62, 3),
        BrownBlock(62, 4),
        BrownBlock(62, 5),
        BrownBlock(62, 6),
        BrownBlock(63, 1),
        BrownBlock(63, 2),
        BrownBlock(63, 3),
        BrownBlock(63, 4),
        BrownBlock(63, 5),
        BrownBlock(63, 6),

        # SmallOrangeBlock(74, 8.5),
        # SmallOrangeBlock(73, 7.5),
        # SmallOrangeBlock(72, 6.5),
        # SmallOrangeBlock(72, 4),
        # SmallOrangeBlock(73, 3),
        # SmallOrangeBlock(74, 2),

        SilverBlock(98, 18),
        SilverBlock(107, 18),

        BrickBlock(138, 5),
        BrickBlock(138, 6),
        BrickBlock(138, 7),
        BrickBlock(138, 8),
        BrickBlock(138, 9),
        BrickBlock(138, 9),

        BrickBlock(139, 4),
        BrickBlock(139, 5),
        BrickBlock(139, 6),
        BrickBlock(139, 7),
        BrickBlock(139, 8),
        BrickBlock(139, 9),
        BrickBlock(139, 10),

        SmallBrownBlock(138.5, 4.5)
                   ]

    list_grs_copy = []

    for i in list_grs:
        No_Blocks_Down = True
        for x in plats + list_blocks + list_grs:
            if i.MakeSelfRect().bottom == x.MakeSelfRect().top and i.MakeSelfRect().left == x.MakeSelfRect().left:
                No_Blocks_Down = False
        if No_Blocks_Down:
            for m in range((((700 - i.y_position) + b_size) // b_size)):
                list_grs_copy.append(Ground(((i.x_position + b_size) // b_size), m))

    list_grs = list_grs_copy + list_grs

    list_grounds_decide = []
    for i in list_grs:
        grass_TF = True
        for x in list_grs:
            if i.MakeSelfRect().top == x.MakeSelfRect().bottom and i.MakeSelfRect().left == x.MakeSelfRect().left:
                grass_TF = False
        if grass_TF:
            list_grounds_decide.append("grass")
        else:
            list_grounds_decide.append("ground")


    player_1 = Player(2, 3)

    start_game_arrow = StartGame(2, 3, 1)
    start_game_stage = StartGame(2.4, 3, 2)
    start_games = [
        start_game_arrow,
        start_game_stage
    ]

    check_ps = [
        Checkpoint(73, 9)
    ]

    end_games = [
        # EndGame(1, 3)
    ]

    snakes = [
        Snake(22, 4, 26),
        Snake(36, 2, 39),
        Snake(49, 7, 52),
        Snake(127, 3, 129),
              ]

    mushrooms = [
        Mushroom(4, 2, 8),
        Mushroom(18, 2, 20),
        Mushroom(22, 4, 26),
        Mushroom(61, 8, 64),
        Mushroom(71, 9, 73),
        Mushroom(118, 3, 120),
        Mushroom(133, 2, 135),
        Mushroom(137, 2, 143),
                 ]



    fly_plats = [
        FlyPlat(17, 16, 25,"RightLeft"),
        FlyPlat(44, 8, 54,"RightLeft"),
        FlyPlat(78, 7, 2,"UpDown"),
        FlyPlat(80, 8, 84,"RightLeft"),
        FlyPlat(86, 11, 4, "UpDown"),
                 ]

    jump_pads = [
        JumpPad(11, 5),
        JumpPad(47, 2),
        JumpPad(59, 3),
    ]

    expand_plats = [
        ExpandPlat(65, 3, 68),
        ExpandPlat(121, 2, 127)
    ]


    spikes = [
        Spike(21, 3),
        Spike(21.5, 3),

        Spike(28, 14),
        Spike(28.5, 14),

        Spike(39, 7, 1),
        Spike(44, 7, 1),

        Spike(50, 3),
        Spike(50.5, 3),

        Spike(58, 2, 1),

        Spike(65, 2, 1),
        Spike(66, 2, 1),
        Spike(67, 2, 1),
        Spike(68, 2, 1),
        Spike(69, 2, 1),
        Spike(70, 2, 1),

        Spike(136, 2),
        Spike(136.5, 2),
              ]

    saws = [
        Saw(29.5, 1.5, 3),
        Saw(52.5, 0.5, 3),
        Saw(137, 6, 3),
            ]

    spiked_balls = []#Siked_Ball(36, 7)]

    fires = [
        Fire(40, 2),
        Fire(41, 2),
        Fire(42, 2),
        Fire(43, 2),
             ]


    # jump_pad = apple, fly_plat = banana, expand_plat = cherry

    fruits = [
        Fruit(6, 9, "b"),
        Fruit(27, 3, "a"),
        Fruit(29, 14, "c"),
        Fruit(33, 4, "a"),
        Fruit(40, 6, "a"),
        Fruit(52, 7, "b"),
        Fruit(65, 4, "b"),
        Fruit(72, 9, "b"),
        Fruit(94, 19, "c"),
              ]

    coins = [
        Coin(1, 5),
        Coin(2, 5),
        Coin(3, 5),
        Coin(1, 6),
        Coin(2, 6),
        Coin(3, 6),

        Coin(13, 11),
        Coin(14, 11),

        Coin(15, 14),
        Coin(16, 14),

        Coin(23, 7),
        Coin(24, 7),
        Coin(25, 7),

        Coin(36, 2),
        Coin(37, 2),
        Coin(38, 2),
        Coin(39, 2),

        Coin(42, 6),
        Coin(43, 6),

        Coin(49, 2),
        Coin(51, 3),

        Coin(49, 7),
        Coin(50, 7),

        Coin(56, 2),
        Coin(57, 2),

        Coin(72, 5),
        Coin(73, 4),
        Coin(73, 5),
        Coin(73, 6),

        Coin(89, 13),
        Coin(90, 13),

        Coin(89, 17),
        Coin(90, 17),

        Coin(93, 15),
        Coin(94, 15),
             ]

    horse_1 = Horse(7, 2)
    horse_2 = Horse(15, 3)
    horses = []

    mummy_1 = Mummy(7, 2, 5, 8)
    mummys = []

    box_1 = Box(5, 4)
    boxes = []

    touch_objects = list_grs + plats + fires + list_blocks + boxes
    touch_objects.append(start_game_stage)

def reset():
    global move_scene_x
    global move_scene_y
    global player_1
    global fall_jump
    if checkpoints == 0:
        move_scene_x = 10000
        move_scene_y = 0
        player_1.x_position = 75
        player_1.y_position = 550 - 1 - 400
    if checkpoints == 1:
        move_scene_x = 4770
        move_scene_y = -288
        player_1.x_position = 620
        player_1.y_position = 388 - 1
    fall_jump = 0
    player_1.transparency = 0

def check_die():
    global fall_jump
    global mushrooms

    for x in snakes:
        if player_1.MakeSelfRect().colliderect(x.MakeRect(x.default)):
            reset()

    for x in range(len(mushrooms)):
        try:
            player_1.MakeSelfRect().bottom == mushrooms[x].MakeSelfRect().top and player_1.MakeSelfRect().left < mushrooms[x].MakeSelfRect().right and player_1.MakeSelfRect().right > mushrooms[x].MakeSelfRect().left

        except:
            pass

        else:
            if player_1.MakeSelfRect().bottom == mushrooms[x].MakeSelfRect().top and player_1.MakeSelfRect().left < \
                    mushrooms[x].MakeSelfRect().right and player_1.MakeSelfRect().right > mushrooms[x].MakeSelfRect().left:
                fall_jump = 15
                mushrooms.pop(x)
            elif player_1.MakeSelfRect().colliderect(mushrooms[x].MakeRect(mushrooms[x].default)):
                reset()

    for x in spikes + saws + spiked_balls:
        if player_1.MakeSelfRect().colliderect(x.MakeSelfRect()):
            reset()

    for x in fires:
        if player_1.MakeSelfRect().colliderect(x.MakeSelfRectFire()) and x.default == x.stage_on:
            reset()

    for x in horses + mummys:
        if player_1.MakeSelfRect().colliderect(x.MakeSelfRect()): # and x.default == x.hit_4:
            reset()

    if player_1.MakeSelfRect().top > 700:
        reset()

def check_make_work():
    if event.type == pygame.MOUSEBUTTONDOWN:
        for x in jump_pads + fly_plats + expand_plats:
            if not x.work:
                if x.MakeSelfRect().collidepoint(event.pos):

                    if x in jump_pads:
                        if player_1.apples >= 1:
                            player_1.apples -= 1
                            x.work = True

                    elif x in fly_plats:
                        if player_1.bananas >= 1:
                            player_1.bananas -= 1
                            x.work = True

                    elif x in expand_plats:
                        if player_1.cherries >= 1:
                            player_1.cherries -= 1
                            x.work = True


    # for x in jump_pads:
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         if x.MakeSelfRect().collidepoint(event.pos):
    #             if not x.work:
    #                 if player_1.apples >= 1:
    #                     player_1.apples -= 1
    #                     x.work = True

def init_all():
    for x in snakes:
        x.Move()
    for x in mushrooms:
        x.Move()
    for x in horses:
        x.ChangeDefault()
        x.Move()
        x.CheckMode()
    for x in mummys:
        x.ChangeDefault()
        x.Move()
        x.CheckMode()

    for x in fly_plats:
        x.Move()

    for x in jump_pads:
        x.CheckJump()
    for x in expand_plats:
        x.CheckWork()
    for x in spiked_balls:
        x.CheckFall()
    for x in fires:
        x.CheckOn()

    for x in check_ps:
        x.CheckPoint()
    for x in end_games:
        x.CheckChange()

    for x in boxes:
        x.CheckFall()

def check_visible(x):
    surface_rect = x.MakeSelfRect()
    if surface_rect.left <= 1300 and surface_rect.right >= 0 and surface_rect.top <= 700 and surface_rect.bottom >= 0:
        return True
    else:
        return False



text = pygame.font.Font(None, 50)

blue_sky = pygame.image.load("Blue_Sky.webp")
blue_sky = pygame.transform.rotozoom(blue_sky, 0, 6)
blue_sky_rect = blue_sky.get_rect(center=(100, 100))

orange_bck = pygame.image.load("Orange_Colour.png")
orange_bck = pygame.transform.rotozoom(orange_bck, 0, 1.5)
orange_bck_rect = orange_bck.get_rect(topleft=(0, 0))

play_button = pygame.image.load("Play_Button.png")
play_button = pygame.transform.rotozoom(play_button, 0, 0.1)
play_button_rect = play_button.get_rect(center=(650, 250))

go_back_button = pygame.image.load("Go_Back.png")
go_back_button = pygame.transform.rotozoom(go_back_button, 0, 0.1)
go_back_button_rect = go_back_button.get_rect(topright=(1300, 0))

restart_button = pygame.image.load("Restart.png")
restart_button = pygame.transform.rotozoom(restart_button, 0, 0.05)
restart_button_rect = restart_button.get_rect(topleft=(0, 0))

apple = pygame.image.load("Apple.png")
apple = pygame.transform.scale(apple, (30, 30))
apple_rect = apple.get_rect(topleft=(300, 5))

banana = pygame.image.load("Banana.png")
banana = pygame.transform.scale(banana, (30, 30))
banana_rect = banana.get_rect(topleft=(450, 5))

cherry = pygame.image.load("Cherry.png")
cherry = pygame.transform.scale(cherry, (30, 30))
cherry_rect = cherry.get_rect(topleft=(600, 5))

coin_1 = pygame.image.load("coin.png")
coin_1 = pygame.transform.scale(coin_1, (30, 30))
coin_1_rect = coin_1.get_rect(topleft=(850, 5))

coin_2 = pygame.transform.scale(coin_1, (50, 50))
coin_2_rect = coin_2.get_rect(center=(745, 530))

clock = pygame.time.Clock()
while True:
    start_play()

    while level == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    level = "level_1"
                    start_play()

        screen.blit(orange_bck, orange_bck_rect)
        screen.blit(play_button, play_button_rect)

        text = pygame.font.Font(None, 75)

        best_score_text = text.render(f"Best Score:", True, 'Black')
        best_score_text_rect = best_score_text.get_rect(center=(650, 450))

        screen.blit(best_score_text, best_score_text_rect)

        best_score_num_text = text.render(f"{"0" if best_score[2] == 0 else best_score[2] / 1000} s", True, 'Black')
        if best_score[2] == 0:
            best_score_num_text = text.render("0s", True, 'Black')
            best_score_num_text_rect = best_score_num_text.get_rect(center=(650, 525))
            screen.blit(best_score_num_text, best_score_num_text_rect)
        else:
            best_score_num_text = text.render(f"{best_score[0] / 1000}s -     {best_score[1]}", True, 'Black')
            best_score_num_text_rect = best_score_num_text.get_rect(center=(650, 530))
            screen.blit(best_score_num_text, best_score_num_text_rect)

            best_score_num_text = text.render(f"{best_score[2] / 1000}s", True, 'Black')
            best_score_num_text_rect = best_score_num_text.get_rect(center=(650, 590))
            screen.blit(best_score_num_text, best_score_num_text_rect)

            screen.blit(coin_2, coin_2_rect)

        pygame.display.update()
        clock.tick(60)

    while level == "level_1":
        #print(move_scene_x, move_scene_y, player_1.x_position, player_1.y_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_back_button_rect.collidepoint(event.pos):
                    level = "menu"
                if restart_button_rect.collidepoint(event.pos):
                    start_play()

            check_make_work()

        init_all()

        player_1.CheckFruitCoin()
        player_1.CheckDieAnimal()

        keys_pressed()
        player_1.Change_Fall_Jump()
        player_1.Transparency()
        check_die()
        blit()

        pygame.display.update()
        clock.tick(60)