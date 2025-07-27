import pygame

#Player size = x 50, y 60

# variables
# -------------------------
best_score = 1000000000
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

#names
#-------------------------
# b_size = block_size
# gr = ground
# p_size_x = player_size_x
# p_size_y = player_size_y
#-------------------------

class Object:
    def __init__(self, x_pos, y_pos):
        self.x_position = (x_pos * b_size) - b_size
        self.y_position = 700 - ((y_pos * b_size) - b_size)


    def MakeRect(self, surface):
        return surface.get_rect(bottomleft=(self.x_position - move_scene_x, self.y_position - move_scene_y))


    def ObjectRight(self, surface):
        TF = False
        for i in set(touch_objects) - set(fly_plats) - set(jump_pads) - set(expand_plats):
            if surface.right == i.MakeRect(i.default).left and surface.bottom > i.MakeRect(i.default).top and surface.top < i.MakeRect(i.default).bottom:
                TF = True
        for i in fly_plats + jump_pads + expand_plats:
            if surface.right == i.MakeRect(i.default).left and surface.bottom > i.MakeRect(i.default).top and surface.top < i.MakeRect(i.default).bottom and i.work:
                TF = True
        return TF

    def ObjectLeft(self, surface):
        TF = False
        for i in set(touch_objects) - set(fly_plats) - set(jump_pads) - set(expand_plats):
            if surface.left == i.MakeRect(i.default).right and surface.bottom > i.MakeRect(i.default).top and surface.top < i.MakeRect(i.default).bottom:
                TF = True
        for i in fly_plats + jump_pads + expand_plats:
            if surface.left == i.MakeRect(i.default).right and surface.bottom > i.MakeRect(i.default).top and surface.top < i.MakeRect(i.default).bottom  and i.work:
                TF = True
        return TF

    def ObjectUp(self, surface):
        TF = False
        for i in set(touch_objects) - set(fly_plats) - set(jump_pads) - set(expand_plats):
            if surface.top == i.MakeRect(i.default).bottom and surface.left < i.MakeRect(i.default).right and surface.right > i.MakeRect(i.default).left:
                TF = True
        for i in fly_plats + jump_pads + expand_plats:
            if surface.top == i.MakeRect(i.default).bottom and surface.left < i.MakeRect(i.default).right and surface.right > i.MakeRect(i.default).left  and i.work:
                TF = True
        return TF

    def ObjectDown(self, surface, width = 0):
        TF = False
        for i in set(touch_objects) - set(fly_plats) - set(jump_pads) - set(expand_plats):
            if surface.bottom == i.MakeRect(i.default).top and surface.left + width < i.MakeRect(i.default).right and surface.right + width > i.MakeRect(i.default).left:
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

        self.default = pygame.image.load("stand_1.png")
        self.default = pygame.transform.scale(self.default, (p_size_x, p_size_y))

        self.stand_1 = pygame.image.load("stand_1.png")
        self.stand_1 = pygame.transform.scale(self.stand_1, (p_size_x, p_size_y))
        self.stand_2 = pygame.image.load("stand_2.png")
        self.stand_2 = pygame.transform.scale(self.stand_2, (p_size_x, p_size_y))
        self.standing = [self.stand_1 for _ in range(10)] + [self.stand_2 for _ in range(10)]

        self.run_1 = pygame.image.load("run_1.png")
        self.run_1 = pygame.transform.scale(self.run_1, (p_size_x, p_size_y))
        self.run_2 = pygame.image.load("run_2.png")
        self.run_2 = pygame.transform.scale(self.run_2, (p_size_x, p_size_y))
        self.run_3 = pygame.image.load("run_3.png")
        self.run_3 = pygame.transform.scale(self.run_3, (p_size_x, p_size_y))
        self.run_4 = pygame.image.load("run_4.png")
        self.run_4 = pygame.transform.scale(self.run_4, (p_size_x, p_size_y))
        self.run_5 = pygame.image.load("run_5.png")
        self.run_5 = pygame.transform.scale(self.run_5, (p_size_x, p_size_y))
        self.run_6 = pygame.image.load("run_6.png")
        self.run_6 = pygame.transform.scale(self.run_6, (p_size_x, p_size_y))
        self.run_7 = pygame.image.load("run_7.png")
        self.run_7 = pygame.transform.scale(self.run_7, (p_size_x, p_size_y))
        self.run_8 = pygame.image.load("run_8.png")
        self.run_8 = pygame.transform.scale(self.run_8, (p_size_x, p_size_y))
        self.running = [self.run_1, self.run_2, self.run_3, self.run_4, self.run_5, self.run_6, self.run_7, self.run_8]

        self.jump = pygame.image.load("jump.png")
        self.jump = pygame.transform.scale(self.jump, (p_size_x, p_size_y))

        self.wall_jump = pygame.image.load("wall_jump.png")
        self.wall_jump = pygame.transform.scale(self.wall_jump, (p_size_x, p_size_y))

        self.fall = pygame.image.load("fall.png")
        self.fall = pygame.transform.scale(self.fall, (p_size_x, p_size_y))

        self.apples = 0
        self.bananas = 0
        self.cherries = 0

        self.coins = 0

    def MakePlayerRect(self):
        """Returns a rect of the image"""
        self.default_rect = self.default.get_rect(bottomleft=(self.x_position, self.y_position))
        return self.default_rect


    def WallJumpRightTF(self):
        TF = False
        for i in touch_objects:
            if self.MakePlayerRect().right == i.MakeRect(i.default).left and self.MakePlayerRect().bottom < i.MakeRect(i.default).bottom and self.MakePlayerRect().top > i.MakeRect(i.default).top:
                TF = True
        return TF

    def WallJumpLeftTF(self):
        TF = False
        for i in touch_objects:
            if self.MakePlayerRect().left == i.MakeRect(i.default).right and self.MakePlayerRect().bottom < i.MakeRect(i.default).bottom and self.MakePlayerRect().top > i.MakeRect(i.default).top:
                TF = True
        return TF


    def MoveRight(self, num = 8):
        """Moves to the right"""
        global move_scene_x
        for x in boxes:
            if self.MakePlayerRect().right == x.MakeSelfRect().left and self.MakePlayerRect().bottom > x.MakeSelfRect().top and self.MakePlayerRect().top < x.MakeSelfRect().bottom:
                for i in range(num // 2):
                    if not x.ObjectRight(x.MakeSelfRect()):
                        x.x_position += 1

                    if not self.ObjectRight(self.MakePlayerRect()):
                        if self.MakePlayerRect().centerx < 650:  # move_scene == 0 and
                            self.x_position += 1
                        elif move_scene_x == track_width - 1300 and self.MakePlayerRect().centerx >= 650 and self.MakePlayerRect().right != 1300:
                            self.x_position += 1
                        elif move_scene_x < track_width - 1300:
                            move_scene_x += 1

        for i in range(num):
            if not self.ObjectRight(self.MakePlayerRect()):
                if self.MakePlayerRect().centerx < 650:  #move_scene == 0 and
                    self.x_position += 1
                elif move_scene_x == track_width - 1300 and self.MakePlayerRect().centerx >= 650 and self.MakePlayerRect().right != 1300:
                    self.x_position += 1
                elif move_scene_x < track_width - 1300:
                    move_scene_x += 1

    def MoveLeft(self, num = 8):
        """Moves to the left"""
        global move_scene_x
        for x in boxes:
            if self.MakePlayerRect().left == x.MakeSelfRect().right and self.MakePlayerRect().bottom > x.MakeSelfRect().top and self.MakePlayerRect().top < x.MakeSelfRect().bottom:
                for i in range(num // 2):
                    if not x.ObjectLeft(x.MakeSelfRect()):
                        x.x_position -= 1

                    if not self.ObjectLeft(self.MakePlayerRect()):
                        if self.MakePlayerRect().centerx > 650:
                            self.x_position -= 1
                        elif move_scene_x == 0 and self.MakePlayerRect().centerx <= 650 and self.MakePlayerRect().left != 0:
                            self.x_position -= 1
                        elif move_scene_x > 0:
                            move_scene_x -= 1

        for i in range(num):
            if not self.ObjectLeft(self.MakePlayerRect()):
                if self.MakePlayerRect().centerx > 650:
                    self.x_position -= 1
                elif move_scene_x == 0 and self.MakePlayerRect().centerx <= 650 and self.MakePlayerRect().left != 0:
                    self.x_position -= 1
                elif move_scene_x > 0:
                    move_scene_x -= 1

    def Move_Up_Down(self, dir):
        global move_scene_y
        if dir > 0:
            if self.MakePlayerRect().centery > 350:
                self.y_position += 1
            elif move_scene_y == 0 and self.MakePlayerRect().centery <= 350 and self.MakePlayerRect().bottom != 0:
                self.y_position += 1
            elif move_scene_y < 0:
                move_scene_y += 1

        else:
            if self.MakePlayerRect().centery > 350:  # move_scene == 0 and
                self.y_position -= 1
            elif move_scene_y == track_height - 700 and self.MakePlayerRect().centery <= 350 and self.MakePlayerRect().top != 700:
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
                if not self.ObjectDown(self.MakePlayerRect()):
                    check_die()
                    if self.MakePlayerRect().centery > 350:
                        self.y_position += 1
                    elif move_scene_y == 0 and self.MakePlayerRect().centery <= 350 and self.MakePlayerRect().bottom != 0:
                        self.y_position += 1
                    elif move_scene_y < 0:
                        move_scene_y += 1

            elif num > 0:
                if not self.ObjectUp(self.MakePlayerRect()):
                    if self.MakePlayerRect().centery > 350:  # move_scene == 0 and
                        self.y_position -= 1
                    elif move_scene_y == track_height - 700 and self.MakePlayerRect().centery <= 350 and self.MakePlayerRect().top != 700:
                        self.x_position -= 1
                    elif move_scene_y < track_height - 700:
                        move_scene_y -= 1

            for x in range(len(horses)):
                if self.MakePlayerRect().bottom == horses[x].MakeSelfRect().top and self.MakePlayerRect().left < \
                        horses[x].MakeSelfRect().right and self.MakePlayerRect().right > horses[x].MakeSelfRect().left:
                    fall_jump = 20
                    horses[x].lives -= 1
            for x in range(len(mummys)):
                if self.MakePlayerRect().bottom == mummys[x].MakeSelfRect().top and self.MakePlayerRect().left < \
                        mummys[x].MakeSelfRect().right and self.MakePlayerRect().right > mummys[x].MakeSelfRect().left:
                    fall_jump = 20
                    mummys[x].lives -= 1


    def Change_Fall_Jump(self):
        """Checks if Minus_Fall_Jump_Speed can be called"""
        global fall_jump
        if self.ObjectUp(self.MakePlayerRect()):
            fall_jump = -1
        if fall_jump <= 0 and self.ObjectDown(self.MakePlayerRect()):
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
                    if player_1.MakePlayerRect().colliderect(fruits[x].MakeSelfRect()):
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
                    if player_1.MakePlayerRect().colliderect(coins[x].MakeSelfRect()):
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

        self.grass = pygame.image.load("Grass.png")
        self.grass = pygame.transform.scale(self.grass, (b_size, b_size))

        self.default = pygame.image.load("Ground.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class BrickBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = pygame.image.load("Block_Brick.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SilverBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = pygame.image.load("Block_Silver.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class GoldBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = pygame.image.load("Block_Gold.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class BrownBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = pygame.image.load("Block_Brown.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class OrangeBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = pygame.image.load("Block_Orange.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)



class SmallSilverBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position -= 1

        self.default = pygame.image.load("Block_Silver.png")
        self.default = pygame.transform.scale(self.default, (b_size / 2, b_size / 2))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SmallGoldBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position -= 1

        self.default = pygame.image.load("Block_Gold.png")
        self.default = pygame.transform.scale(self.default, (b_size / 2, b_size / 2))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SmallBrownBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position -= 1

        self.default = pygame.image.load("Block_Brown.png")
        self.default = pygame.transform.scale(self.default, (b_size / 2, b_size / 2))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SmallOrangeBlock(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position -= 1

        self.default = pygame.image.load("Block_Orange.png")
        self.default = pygame.transform.scale(self.default, (b_size / 2, b_size / 2))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)



class GoldThickPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 3 * 2

        self.default = pygame.image.load("Plat_Thick_Gold.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 3))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SilverThickPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 3 * 2

        self.default = pygame.image.load("Plat_Thick_Silver.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 3))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class BrownThickPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 3 * 2

        self.default = pygame.image.load("Plat_Thick_Brown.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 3))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class OrangeThickPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position = self.y_position - b_size / 3 * 2

        self.default = pygame.image.load("Plat_Thick_Orange.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 3))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)



class GoldThinPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = pygame.image.load("Plat_Thin_Gold.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 10))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class SilverThinPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = pygame.image.load("Plat_Thin_Silver.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 10))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class WoodThinPlat(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.default = pygame.image.load("Plat_Thin_Wood.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 10))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)



class StartGame(Object):
    def __init__(self, x_pos, y_pos, num):
        super().__init__(x_pos, y_pos)

        self.start_arrow = pygame.image.load('Start_arrow.png')
        self.start_arrow = pygame.transform.scale(self.start_arrow, (b_size // 10 * 6, b_size))
        self.start_stage = pygame.image.load('Start_stage.png')
        self.start_stage = pygame.transform.scale(self.start_stage, (b_size, b_size // 4))

        if num == 1:
            self.default = self.start_arrow
        else:
            self.default = self.start_stage

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class Checkpoint(Object):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.checkpoint_TF = False

        self.no_checkpoint = pygame.image.load("Checkpoint_No.png")

        self.checkpoint_1 = pygame.image.load("Checkpoint_Flag_1.png")
        self.checkpoint_2 = pygame.image.load("Checkpoint_Flag_2.png")
        self.checkpoint_3 = pygame.image.load("Checkpoint_Flag_3.png")
        self.checkpoint_4 = pygame.image.load("Checkpoint_Flag_4.png")
        self.checkpoint_5 = pygame.image.load("Checkpoint_Flag_5.png")
        self.checkpoint_6 = pygame.image.load("Checkpoint_Flag_6.png")

        self.checkpointing = [self.checkpoint_1, self.checkpoint_1,
                              self.checkpoint_2, self.checkpoint_2,
                              self.checkpoint_3, self.checkpoint_3,
                              self.checkpoint_4, self.checkpoint_4,
                              self.checkpoint_5, self.checkpoint_5,
                              self.checkpoint_6, self.checkpoint_6]

    def CheckPoint(self):
        global checkpoints
        if not self.checkpoint_TF:
            if player_1.MakePlayerRect().colliderect(self.MakeRect(self.no_checkpoint)):
                self.checkpoint_TF = True
                checkpoints += 1

class EndGame(Object):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.end_no = pygame.image.load('End_No.png')
        self.end_no = pygame.transform.scale(self.end_no, (b_size * 2, b_size * 2))
        self.end_1 = pygame.image.load('End_1.png')
        self.end_1 = pygame.transform.scale(self.end_1, (b_size * 2, b_size * 2))
        self.end_2= pygame.image.load('End_2.png')
        self.end_2 = pygame.transform.scale(self.end_2, (b_size * 2, b_size * 2 - b_size // 10))
        self.end_3 = pygame.image.load('End_3.png')
        self.end_3 = pygame.transform.scale(self.end_3, (b_size * 2, b_size * 2 - b_size // 5))

        self.default = self.end_1

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def CheckPressed(self):
        if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
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
                if over_game_time - start_game_time < best_score:
                    best_score = over_game_time - start_game_time
                level = "menu"



class Snake(Object):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.side = "r"

        self.default = pygame.image.load("snake_1.png")
        self.default = pygame.transform.scale(self.default, (40, 20))
        self.snake_1 = pygame.image.load("snake_2.png")
        self.snake_1 = pygame.transform.scale(self.snake_1, (40, 20))
        self.snake_2 = pygame.image.load("snake_3.png")
        self.snake_2 = pygame.transform.scale(self.snake_2, (40, 20))
        self.snake_3 = pygame.image.load("snake_4.png")
        self.snake_3 = pygame.transform.scale(self.snake_3, (40, 20))

        self.going = [self.default, self.default, self.default, self.default, self.default, self.snake_1, self.snake_1, self.snake_1, self.snake_1, self.snake_1, self.snake_2, self.snake_2, self.snake_2, self.snake_2, self.snake_2, self.snake_3, self.snake_3, self.snake_3, self.snake_3, self.snake_3]

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def Move(self):
        # print(self.FallRight(self.MakeSelfRect()))
        if self.side == "r":
            for i in range(3):
                if not self.ObjectRight(self.MakeSelfRect()) and self.FallRight(self.MakeSelfRect()):
                    if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
                        self.side = "l"
                    else:
                        self.x_position += 1
                else:
                    self.side = "l"

        if self.side == "l":
            for i in range(3):
                if not self.ObjectLeft(self.MakeSelfRect()) and self.FallLeft(self.MakeSelfRect()):
                    if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
                        self.side = "r"
                    else:
                        self.x_position -= 1
                else:
                    self.side = "r"
                # if move_scene != 0 or self.MakeSelfRect().left != 0:
                # else:
                #     self.side = "r"

class Mushroom(Object):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.side = "r"

        self.default = pygame.image.load("mushroom_1.png")
        self.default = pygame.transform.scale(self.default, (45, 50))
        self.mushroom_1 = pygame.image.load("mushroom_2.png")
        self.mushroom_1 = pygame.transform.scale(self.mushroom_1, (45, 50))
        self.mushroom_2 = pygame.image.load("mushroom_3.png")
        self.mushroom_2 = pygame.transform.scale(self.mushroom_2, (45, 50))
        self.mushroom_3 = pygame.image.load("mushroom_4.png")
        self.mushroom_3 = pygame.transform.scale(self.mushroom_3, (45, 50))
        self.mushroom_4 = pygame.image.load("mushroom_5.png")
        self.mushroom_4 = pygame.transform.scale(self.mushroom_4, (45, 50))
        self.mushroom_5 = pygame.image.load("mushroom_6.png")
        self.mushroom_5 = pygame.transform.scale(self.mushroom_5, (45, 50))
        self.mushroom_6 = pygame.image.load("mushroom_7.png")
        self.mushroom_6 = pygame.transform.scale(self.mushroom_6, (45, 50))
        self.mushroom_7 = pygame.image.load("mushroom_8.png")
        self.mushroom_7 = pygame.transform.scale(self.mushroom_7, (45, 50))

        self.going = [self.default, self.default,
                        self.mushroom_1, self.mushroom_1,
                        self.mushroom_2, self.mushroom_2,
                        self.mushroom_3, self.mushroom_3,
                        self.mushroom_4, self.mushroom_4,
                        self.mushroom_5, self.mushroom_5,
                        self.mushroom_6, self.mushroom_6,
                        self.mushroom_7, self.mushroom_7,]

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def Move(self):
        if self.side == "r":
            for i in range(4):
                if not self.ObjectRight(self.MakeSelfRect()) and self.FallRight(self.MakeSelfRect()):
                    if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
                        self.side = "l"
                    else:
                        self.x_position += 1
                else:
                    self.side = "l"

        if self.side == "l":
            for i in range(4):
                if not self.ObjectLeft(self.MakeSelfRect()) and self.FallLeft(self.MakeSelfRect()):
                    if move_scene_x == track_width - 1300 and self.MakeSelfRect().right == 1300:
                        self.side = "r"
                    else:
                        self.x_position -= 1
                else:
                    self.side = "r"
                # if move_scene != 0 or self.MakeSelfRect().left != 0:
                # else:
                #     self.side = "r"

class Horse(Object):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.lives = 4

        self.size_x = b_size * 2
        self.size_y = b_size + b_size // 2

        self.side = "r"

        self.run_1 = pygame.image.load("horse_run_1.png")
        self.run_1 = pygame.transform.scale(self.run_1, (self.size_x, self.size_y)) #(186, 138)
        self.run_2 = pygame.image.load("horse_run_2.png")
        self.run_2 = pygame.transform.scale(self.run_2, (self.size_x, self.size_y))
        self.run_3 = pygame.image.load("horse_run_3.png")
        self.run_3 = pygame.transform.scale(self.run_3, (self.size_x, self.size_y))
        self.run_4 = pygame.image.load("horse_run_4.png")
        self.run_4 = pygame.transform.scale(self.run_4, (self.size_x, self.size_y))
        self.run_5 = pygame.image.load("horse_run_5.png")
        self.run_5 = pygame.transform.scale(self.run_5, (self.size_x, self.size_y))
        self.run_6 = pygame.image.load("horse_run_6.png")
        self.run_6 = pygame.transform.scale(self.run_6, (self.size_x, self.size_y))

        self.hit_1 = pygame.image.load("horse_hit_2.png")
        self.hit_1 = pygame.transform.scale(self.hit_1, (self.size_x, self.size_y))
        self.hit_2 = pygame.image.load("horse_hit_3.png")
        self.hit_2 = pygame.transform.scale(self.hit_2, (self.size_x, self.size_y))
        self.hit_3 = pygame.image.load("horse_hit_4.png")
        self.hit_3 = pygame.transform.scale(self.hit_3, (self.size_x + self.size_x // 3, self.size_y))
        self.hit_4 = pygame.image.load("horse_hit_5.png")
        self.hit_4 = pygame.transform.scale(self.hit_4, (self.size_x + self.size_x // 1.5, self.size_y))
        self.hit_5 = pygame.image.load("horse_hit_6.png")
        self.hit_5 = pygame.transform.scale(self.hit_5, (self.size_x + self.size_x // 10, self.size_y))

        self.default = self.run_1

        self.run = [self.run_1] * 3 + [self.run_2] * 3 + [self.run_3] * 3 + [self.run_4] * 3 + [self.run_5] * 3 + [self.run_6] * 3
        self.hit = [self.hit_1, self.hit_2, self.hit_3, self.hit_4, self.hit_5]

        self.default_to_die = False

    def CheckMode(self):
        if self.side == "r":
            if player_1.MakePlayerRect().left <= self.MakeSelfRect().right + b_size and player_1.MakePlayerRect().left >= self.MakeSelfRect().right and player_1.MakePlayerRect().top < self.MakeSelfRect().bottom and player_1.MakePlayerRect().bottom > self.MakeSelfRect().top:
                if self.default not in self.hit:
                    self.default = self.hit_1
            else:
                pass
                # self.mode = "run"

        elif self.side == "l":
            if player_1.MakePlayerRect().right >= self.MakeSelfRect().left - b_size and player_1.MakePlayerRect().right <= self.MakeSelfRect().left and player_1.MakePlayerRect().top < self.MakeSelfRect().bottom and player_1.MakePlayerRect().bottom > self.MakeSelfRect().top:
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

        self.lives = 5

        self.size_x = b_size * 1.5
        self.size_y = b_size * 2

        self.mode = "run"

        self.side = "l"

        self.run_1 = pygame.image.load("mum_run_1.png")
        self.run_1 = pygame.transform.rotozoom(self.run_1, 0, 3)
        self.run_2 = pygame.image.load("mum_run_2.png")
        self.run_2 = pygame.transform.rotozoom(self.run_2, 0, 3)
        self.run_3 = pygame.image.load("mum_run_3.png")
        self.run_3 = pygame.transform.rotozoom(self.run_3, 0, 3)
        self.run_4 = pygame.image.load("mum_run_4.png")
        self.run_4 = pygame.transform.rotozoom(self.run_4, 0, 3)
        self.run_5 = pygame.image.load("mum_run_5.png")
        self.run_5 = pygame.transform.rotozoom(self.run_5, 0, 3)
        self.run_6 = pygame.image.load("mum_run_6.png")
        self.run_6 = pygame.transform.rotozoom(self.run_6, 0, 3)

        self.hit_1 = pygame.image.load("mum_hit_1.png")
        self.hit_1 = pygame.transform.rotozoom(self.hit_1, 0, 3)
        self.hit_2 = pygame.image.load("mum_hit_2.png")
        self.hit_2 = pygame.transform.rotozoom(self.hit_2, 0, 3)
        self.hit_3 = pygame.image.load("mum_hit_3.png")
        self.hit_3 = pygame.transform.rotozoom(self.hit_3, 0, 3)
        self.hit_4 = pygame.image.load("mum_hit_4.png")
        self.hit_4 = pygame.transform.rotozoom(self.hit_4, 0, 3)
        self.hit_5 = pygame.image.load("mum_hit_5.png")
        self.hit_5 = pygame.transform.rotozoom(self.hit_5, 0, 3)

        self.stand_1 = pygame.image.load("mum_stand_1.png")
        self.stand_1 = pygame.transform.rotozoom(self.stand_1, 0, 3)
        self.stand_2 = pygame.image.load("mum_stand_2.png")
        self.stand_2 = pygame.transform.rotozoom(self.stand_2, 0, 3)

        self.default = self.run_1

        self.run = [self.run_1] * 3 + [self.run_2] * 3 + [self.run_3] * 3 + [self.run_4] * 3 + [self.run_5] * 3 + [self.run_6] * 3
        # + [self.run_3] * 3 + [self.run_4] * 3 + [self.run_5] * 3 + [self.run_6] * 3
        self.hit = [self.hit_1, self.hit_2, self.hit_3, self.hit_4, self.hit_5]

        self.default_to_die = False

    def CheckMode(self):
        if self.side == "r":
            if player_1.MakePlayerRect().left <= self.MakeSelfRect().right + 35 and player_1.MakePlayerRect().left >= self.MakeSelfRect().right and player_1.MakePlayerRect().top < self.MakeSelfRect().bottom and player_1.MakePlayerRect().bottom > self.MakeSelfRect().top:
                if self.default not in self.hit:
                    self.default = self.hit_1
            else:
                pass
                # self.mode = "run"

        elif self.side == "l":
            if player_1.MakePlayerRect().right >= self.MakeSelfRect().left - 35 and player_1.MakePlayerRect().right <= self.MakeSelfRect().left and player_1.MakePlayerRect().top < self.MakeSelfRect().bottom and player_1.MakePlayerRect().bottom > self.MakeSelfRect().top:
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


        self.default = pygame.image.load("Plat_Fly_1.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size // 10 * 4))
        self.fly_plat_1 = pygame.image.load("Plat_Fly_2.png")
        self.fly_plat_1 = pygame.transform.scale(self.fly_plat_1, (b_size, b_size // 10 * 4))
        self.fly_plat_2 = pygame.image.load("Plat_Fly_3.png")
        self.fly_plat_2 = pygame.transform.scale(self.fly_plat_2, (b_size, b_size // 10 * 4))
        self.fly_plat_3 = pygame.image.load("Plat_Fly_4.png")
        self.fly_plat_3 = pygame.transform.scale(self.fly_plat_3, (b_size, b_size // 10 * 4))

        self.going = [self.default, self.default, self.fly_plat_1, self.fly_plat_1,
                           self.fly_plat_2, self.fly_plat_2, self.fly_plat_3, self.fly_plat_3]

        self.default_2 = pygame.image.load("Banana.png")
        self.default_2 = pygame.transform.scale(self.default_2, (b_size // 3, b_size // 3))

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
                    if self.MakeSelfRect().bottom == player_1.MakePlayerRect().top and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                        fall_jump = -1
                    if self.direction == "u":
                        if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                            if player_1.ObjectUp(player_1.MakePlayerRect()):
                                self.direction = "d"
                                reset()
                    else:
                        if self.MakeSelfRect().bottom == player_1.MakePlayerRect().top and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                            self.direction = "u"
                            fall_jump = -1
                        if self.MakeSelfRect().bottom == player_1.MakePlayerRect().top and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                            if player_1.ObjectDown(player_1.MakePlayerRect()):
                                self.direction = "u"
                                reset()

                if self.fly == "RightLeft":
                    if self.direction == "r":
                        if self.MakeSelfRect().left + move_scene_x != self.position_2:
                            self.x_position += 1
                            if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                                player_1.MoveRight(1)
                                # player_1.x_position += 1
                        else:
                            self.direction = "l"

                    if self.direction == "l":
                        if self.MakeSelfRect().left + move_scene_x != self.position_1:
                            self.x_position -= 1
                            if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                                player_1.MoveLeft(1)
                                # player_1.x_position -= 1
                        else:
                            self.direction = "r"
                else:
                    if self.direction == "d":
                        if self.MakeSelfRect().bottom + move_scene_y != self.position_2:
                            if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                                player_1.Move_Up_Down(1)
                                fall_jump = 0
                            self.y_position += 1
                        else:
                            self.direction = "u"

                    if self.direction == "u":
                        if self.MakeSelfRect().bottom + move_scene_y != self.position_1:
                            if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
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

        self.jump_pad_1 = pygame.image.load("jump_pad_1.png")
        self.jump_pad_1 = pygame.transform.scale(self.jump_pad_1, (b_size, b_size / 2))

        self.jump_pad_2 = pygame.image.load("jump_pad_2.png")
        self.jump_pad_2 = pygame.transform.scale(self.jump_pad_2, (b_size, (b_size / 5) * 3))

        self.jump_pad_3 = pygame.image.load("jump_pad_3.png")
        self.jump_pad_3 = pygame.transform.scale(self.jump_pad_3, (b_size, b_size))

        self.jump_pad_4 = pygame.image.load("jump_pad_4.png")
        self.jump_pad_4 = pygame.transform.scale(self.jump_pad_4, (b_size, b_size * 1.1))

        self.jump_pad_5 = pygame.image.load("jump_pad_5.png")
        self.jump_pad_5 = pygame.transform.scale(self.jump_pad_5, (b_size, b_size * 1.1))

        self.default_2 = pygame.image.load("Apple.png")
        self.default_2 = pygame.transform.scale(self.default_2, (b_size // 3, b_size // 3))

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
            if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left and self.default == self.jump_pad_1:
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

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.y_position -= b_size - b_size / 5

        self.work = objects_on

        self.transparency = 125

        self.i = 50

        self.original = pygame.image.load("Plat_Thin_Wood.png")

        self.default = pygame.transform.scale(self.original, ( self.i, b_size / 5))

        self.default_2 = pygame.image.load("Cherry.png")
        self.default_2 = pygame.transform.scale(self.default_2, (b_size // 3, b_size // 3))

    def MakeSelfRect(self):
        return self.default.get_rect(bottomleft=(self.x_position - move_scene_x, self.y_position - move_scene_y))

    def MakeSelfRectFruit(self):
        return self.default_2.get_rect(bottomleft=(self.x_position - move_scene_x + b_size // 8, self.y_position - move_scene_y))

    def CheckWork(self):
        if self.work:
            self.default = pygame.transform.scale(self.original, (self.i, b_size / 5))
            if self.work:
                for i in range(5):
                    if not self.ObjectRight(self.MakeSelfRect()):
                        self.i += 1



class Spike(Object):
    """
    Class that represents ground and grass
    """

    def __init__(self, x_pos, y_pos, sz = 2):
        super().__init__(x_pos, y_pos)

        self.size = sz

        self.default = pygame.image.load("Spike.webp")
        self.default = pygame.transform.scale(self.default, (b_size / self.size, b_size / self.size))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

class Saw(Object):

    def __init__(self, x_pos, y_pos, sz):
        super().__init__(x_pos, y_pos)

        self.size = sz

        self.saw_1 = pygame.image.load("Saw_1.png")
        self.saw_1 = pygame.transform.scale(self.saw_1, (b_size * self.size , b_size * self.size))
        self.saw_2 = pygame.image.load("Saw_2.png")
        self.saw_2 = pygame.transform.scale(self.saw_2, (b_size * self.size , b_size * self.size))
        self.saw_3 = pygame.image.load("Saw_3.png")
        self.saw_3 = pygame.transform.scale(self.saw_3, (b_size * self.size , b_size * self.size))
        self.saw_4 = pygame.image.load("Saw_4.png")
        self.saw_4 = pygame.transform.scale(self.saw_4, (b_size * self.size , b_size * self.size))
        self.saw_5 = pygame.image.load("Saw_5.png")
        self.saw_5 = pygame.transform.scale(self.saw_5, (b_size * self.size , b_size * self.size))
        self.saw_6 = pygame.image.load("Saw_6.png")
        self.saw_6 = pygame.transform.scale(self.saw_6, (b_size * self.size , b_size * self.size))
        self.saw_7 = pygame.image.load("Saw_7.png")
        self.saw_7 = pygame.transform.scale(self.saw_7, (b_size * self.size , b_size * self.size))
        self.saw_8 = pygame.image.load("Saw_8.png")
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

        self.default = pygame.image.load("SpikedBall.png")
        self.default = pygame.transform.scale(self.default, (b_size * 1.5, b_size * 1.5))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def CheckFall(self):
        if not self.fall:
            if player_1.MakePlayerRect().right >= self.MakeSelfRect().left and not self.ObjectDown(self.MakeSelfRect()):
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

        self.delay = 1300
        self.delay_after = 3000

        self.start = 0
        self.over = 0

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def MakeSelfRectFire(self):
        return self.fire_1.get_rect(bottomleft=(self.x_position - move_scene_x, self.y_position - b_size - move_scene_y))

    def CheckOn(self):
        self.now = pygame.time.get_ticks()
        if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
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
            self.default = pygame.image.load("Apple.png")
        elif  self.name == "b":
            self.default = pygame.image.load("Banana.png")
        elif  self.name == "c":
            self.default = pygame.image.load("Cherry.png")

        self.default = pygame.transform.scale(self.default, (b_size / 3, b_size / 3))

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

        self.default = pygame.image.load("coin.png")
        self.default = pygame.transform.scale(self.default, (b_size / 2, b_size / 2))

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

        self.default = pygame.image.load("Box.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size))

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def CheckFall(self):
        if not self.ObjectDown(self.MakeSelfRect()):
            self.gravity_pull += 3
        else:
            self.gravity_pull = 0

        for i in range(self.gravity_pull):
            if not self.ObjectDown(self.MakeSelfRect()):
                self.y_position += 1



player_1 = Player(0, 0)
check_p_1 = Checkpoint(0, 0)


def blit():
    """Blits all the objects"""
    global player_1

    screen.blit(blue_sky, blue_sky_rect)

    for i in range(len(list_grs)):
        # 0 <= i.x_position >= 1300 and 0 >= i.y_position <= 700
        if list_grs[i].MakeSelfRect().left <= 1300 and list_grs[i].MakeSelfRect().right >= 0 and list_grs[i].MakeSelfRect().top <= 700 and list_grs[i].MakeSelfRect().bottom >= 0:
            if list_grounds_decide[i] == "grass":
                screen.blit(list_grs[i].grass, list_grs[i].MakeSelfRect())
            elif list_grounds_decide[i] == "ground":
                screen.blit(list_grs[i].default, list_grs[i].MakeSelfRect())

    for x in set(touch_objects) - set(list_grs) - set(fly_plats) - set(jump_pads) - set(expand_plats):
        screen.blit(x.default, x.MakeRect(x.default))

    for x in spikes + spiked_balls:
        screen.blit(x.default, x.MakeSelfRect())

    for x in saws:
        screen.blit(x.going[0], x.MakeSelfRect())
        x.going.append(x.going[0])
        x.going.pop(0)

    for x in fires:
        if x.default == x.stage_on:
            screen.blit(x.going[0], x.MakeSelfRectFire())
            x.going.append(x.going[0])
            x.going.pop(0)


    for x in start_games:
        if x.default == x.start_arrow:
            screen.blit(x.start_arrow, x.MakeSelfRect())

    for x in check_ps:
        if x.checkpoint_TF:
            screen.blit(x.checkpointing[0], x.MakeRect(x.checkpoint_1))
            x.checkpointing.append(x.checkpointing[0])
            x.checkpointing.pop(0)
        else:
            screen.blit(x.no_checkpoint, x.MakeRect(x.no_checkpoint))


    for x in snakes + mushrooms:
        if x.side == "l":
            screen.blit(x.going[0], x.MakeSelfRect())
        if x.side == "r":
            screen.blit(pygame.transform.flip(x.going[0], True, False), x.MakeSelfRect())
        x.going.append(x.going[0])
        x.going.pop(0)

    for x in horses + mummys:
        if x.side == "r":
            screen.blit(pygame.transform.flip(x.default, True, False),  x.MakeSelfRect())
        else:
            screen.blit(x.default, x.MakeSelfRect())


    for x in fly_plats:
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
        if x.work:
            x.default.set_alpha(255)
            screen.blit(x.default, x.MakeRect(x.default))
        else:
            x.default.set_alpha(x.transparency)
            screen.blit(x.default, x.MakeRect(x.default))
            screen.blit(x.default_2, x.MakeSelfRectFruit())

    for x in expand_plats:
        if x.work:
            x.default.set_alpha(255)
            screen.blit(x.default, x.MakeRect(x.default))
        else:
            x.default.set_alpha(x.transparency)
            screen.blit(x.default, x.MakeRect(x.default))
            screen.blit(x.default_2, x.MakeSelfRectFruit())


    if find_mode() == "stand":
        player_1.standing[0].set_alpha(player_1.transparency)
        if side == "r":
            screen.blit(player_1.standing[0], player_1.MakePlayerRect())
        else:
            screen.blit(pygame.transform.flip(player_1.standing[0], True, False), player_1.MakePlayerRect())
        player_1.standing.append(player_1.standing[0])
        player_1.standing.pop(0)

    elif find_mode() == "run":
        player_1.running[0].set_alpha(player_1.transparency)
        if side == "r":
            screen.blit(player_1.running[0], player_1.MakePlayerRect())
        else:
            screen.blit(pygame.transform.flip(player_1.running[0], True, False), player_1.MakePlayerRect())
        player_1.running.append(player_1.running[0])
        player_1.running.pop(0)

    elif find_mode() == "jump":
        player_1.jump.set_alpha(player_1.transparency)
        player_1.running = [player_1.run_1, player_1.run_2, player_1.run_3, player_1.run_4, player_1.run_5, player_1.run_6, player_1.run_7, player_1.run_8]
        if side == "r":
            screen.blit(player_1.jump, player_1.MakePlayerRect())
        else:
            screen.blit(pygame.transform.flip(player_1.jump, True, False), player_1.MakePlayerRect())

    elif find_mode() == "fall":
        player_1.fall.set_alpha(player_1.transparency)
        player_1.running = [player_1.run_1, player_1.run_2, player_1.run_3, player_1.run_4, player_1.run_5, player_1.run_6, player_1.run_7, player_1.run_8]
        if side == "r":
            screen.blit(player_1.fall, player_1.MakePlayerRect())
        else:
            screen.blit(pygame.transform.flip(player_1.fall, True, False), player_1.MakePlayerRect())

    elif find_mode() == "wall":
        player_1.wall_jump.set_alpha(player_1.transparency)
        player_1.running = [player_1.run_1, player_1.run_2, player_1.run_3, player_1.run_4, player_1.run_5, player_1.run_6, player_1.run_7, player_1.run_8]
        if side == "r":
            screen.blit(player_1.wall_jump, player_1.MakePlayerRect())
        else:
            screen.blit(pygame.transform.flip(player_1.wall_jump, True, False), player_1.MakePlayerRect())


    for x in fruits + coins:
        x.y_position = x.original_y + x.go[0]
        screen.blit(x.default, x.MakeSelfRect())
        x.go.append(x.go[0])
        x.go.pop(0)


    screen.blit(apple, apple_rect)
    screen.blit(banana, banana_rect)
    screen.blit(cherry, cherry_rect)
    screen.blit(coin, coin_rect)

    text = pygame.font.Font(None, 50)

    apples_count = text.render(f"{player_1.apples}", True, 'Black')
    apples_count_rect = apples_count.get_rect(topleft=(340, 5))
    screen.blit(apples_count, apples_count_rect)

    banana_count = text.render(f"{player_1.bananas}", True, 'Black')
    banana_count_rect = banana_count.get_rect(topleft=(490, 5))
    screen.blit(banana_count, banana_count_rect)

    cherry_count = text.render(f"{player_1.cherries}", True, 'Black')
    cherry_count_rect = cherry_count.get_rect(topleft=(640, 5))
    screen.blit(cherry_count, cherry_count_rect)

    coin_count = text.render(f"{player_1.coins}", True, 'Black')
    coin_count_rect = coin_count.get_rect(topleft=(890, 5))
    screen.blit(coin_count, coin_count_rect)

    screen.blit(go_back_button, go_back_button_rect)
    screen.blit(restart_button, restart_button_rect)

def keys_pressed():
    """What happens when keys are pressed"""
    global fall_jump, move_scene_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if find_mode() == "wall":
            fall_jump = 0
            if not player_1.ObjectDown(player_1.MakePlayerRect()):
                check_die()
                if player_1.MakePlayerRect().centery > 350:
                    player_1.y_position += 1
                elif move_scene_y == 0 and player_1.MakePlayerRect().centery <= 350 and player_1.MakePlayerRect().bottom != 0:
                    player_1.y_position += 1
                elif move_scene_y < 0:
                    move_scene_y += 1
        else:
            player_1.MoveRight()

    if keys[pygame.K_LEFT]:
        if find_mode() == "wall":
            fall_jump = 0
            if not player_1.ObjectDown(player_1.MakePlayerRect()):
                check_die()
                if player_1.MakePlayerRect().centery > 350:
                    player_1.y_position += 1
                elif move_scene_y == 0 and player_1.MakePlayerRect().centery <= 350 and player_1.MakePlayerRect().bottom != 0:
                    player_1.y_position += 1
                elif move_scene_y < 0:
                    move_scene_y += 1
        else:
            player_1.MoveLeft()

    if keys[pygame.K_UP] and player_1.ObjectDown(player_1.MakePlayerRect()):
        fall_jump = 28

    elif keys[pygame.K_UP] and not player_1.ObjectDown(player_1.MakePlayerRect()) and fall_jump == 0 and find_mode() == "wall":
        fall_jump = 17

def find_mode():
    global mode
    global side
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        side = "r"
        if player_1.ObjectDown(player_1.MakePlayerRect()):
            if player_1.ObjectRight(player_1.MakePlayerRect()):
                mode = "stand"
            else:
                mode = "run"
        if not player_1.ObjectDown(player_1.MakePlayerRect()) and player_1.ObjectRight(player_1.MakePlayerRect()):
            mode = "wall"
        if not player_1.ObjectDown(player_1.MakePlayerRect()) and not player_1.ObjectRight(player_1.MakePlayerRect()):
            if fall_jump >= 0:
                mode = "jump"
            else:
                mode = "fall"

        for x in boxes:
            if player_1.MakePlayerRect().right == x.MakeSelfRect().left and player_1.MakePlayerRect().bottom > x.MakeSelfRect().top and player_1.MakePlayerRect().top < x.MakeSelfRect().bottom:
                if not x.ObjectRight(x.MakeSelfRect()):
                    mode = "run"


    elif keys[pygame.K_LEFT]:
        side = "l"
        if player_1.ObjectDown(player_1.MakePlayerRect()):
            if player_1.ObjectLeft(player_1.MakePlayerRect()):
                mode = "stand"
            else:
                mode = "run"
        if not player_1.ObjectDown(player_1.MakePlayerRect()) and player_1.ObjectLeft(player_1.MakePlayerRect()):
            mode = "wall"
        if not player_1.ObjectDown(player_1.MakePlayerRect()) and not player_1.ObjectLeft(player_1.MakePlayerRect()):
            if fall_jump >= 0:
                mode = "jump"
            else:
                mode = "fall"

        for x in boxes:
            if player_1.MakePlayerRect().left == x.MakeSelfRect().right and player_1.MakePlayerRect().bottom > x.MakeSelfRect().top and player_1.MakePlayerRect().top < x.MakeSelfRect().bottom:
                if not x.ObjectLeft(x.MakeSelfRect()):
                    mode = "run"

    else:
        mode = "stand"

    if fall_jump > 0:
        mode = "jump"
    elif fall_jump < 0 and not player_1.ObjectLeft(player_1.MakePlayerRect()) and not player_1.ObjectRight(player_1.MakePlayerRect()):
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

    # variables
    # -------------------------
    start_game_time = pygame.time.get_ticks()
    fall_jump = 0
    move_scene_x = 0
    move_scene_y = 0
    mode = "fall"
    side = "r"
    checkpoints = 1

    # -------------------------

    list_grs = [Ground(1, 1),
                Ground(2, 1),
                Ground(3, 1),

                Ground(1, 2),
                Ground(2, 2),
                Ground(3, 2),

                Ground(4, 1),
                Ground(5, 1),
                Ground(6, 1),
                Ground(7, 1),
                Ground(8, 1),
                Ground(1, 1),
                Ground(9, 1),
                Ground(10, 1),
                Ground(11, 1),
                Ground(9, 2),
                Ground(10, 2),
                Ground(11, 2),
                Ground(10, 3),
                Ground(11, 3),
                Ground(11, 4),
                Ground(15, 2),
                Ground(16, 2),
                Ground(17, 2),
                Ground(15, 3),
                Ground(16, 3),
                Ground(15, 4),
                Ground(15, 1),
                Ground(16, 1),
                Ground(17, 1),
                Ground(18, 1),
                Ground(19, 1),
                Ground(20, 1),
                Ground(21, 1),
                Ground(21, 2),

                Ground(22, 1),
                Ground(22, 2),
                Ground(22, 3),

                Ground(23, 1),
                Ground(23, 2),
                Ground(23, 3),

                Ground(24, 1),
                Ground(24, 2),
                Ground(24, 3),

                Ground(25, 1),
                Ground(25, 2),
                Ground(25, 3),

                Ground(26, 1),
                Ground(26, 2),
                Ground(26, 3),

                Ground(26, 1),
                Ground(26, 2),

                Ground(27, 1),
                Ground(27, 2),

                Ground(28, 1),
                Ground(28, 2),

                Ground(29, 1),
                Ground(29, 2),

                Ground(30, 1),
                Ground(30, 2),

                Ground(31, 1),
                Ground(31, 2),
                Ground(31, 3),
                Ground(31, 4),

                Ground(32, 1),
                Ground(32, 2),
                Ground(32, 3),
                Ground(32, 4),

                Ground(33, 1),
                Ground(33, 2),
                Ground(33, 3),

                Ground(34, 1),
                Ground(34, 2),

                Ground(35, 1),
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

                Ground(50, 1),
                Ground(50, 2),

                Ground(51, 1),
                Ground(51, 2),

                Ground(52, 1),
                Ground(52, 2),
                Ground(52, 3),

                Ground(53, 1),

                Ground(54, 1),

                Ground(55, 1),

                Ground(56, 1),

                Ground(57, 1),

                Ground(58, 1),

                Ground(59, 1),
                Ground(59, 2),

                Ground(60, 1),
                Ground(60, 2),

                Ground(61, 1),
                Ground(61, 2),
                Ground(61, 3),
                Ground(61, 4),
                Ground(61, 5),
                Ground(61, 6),
                Ground(61, 7),

                Ground(62, 7),

                Ground(63, 7),

                Ground(64, 1),
                Ground(64, 2),
                Ground(64, 3),
                Ground(64, 4),
                Ground(64, 5),
                Ground(64, 6),
                Ground(64, 7),

                Ground(65, 1),

                Ground(66, 1),

                Ground(67, 1),

                Ground(68, 1),

                Ground(69, 1),

                Ground(70, 1),

                Ground(71, 1),
                Ground(71, 2),
                Ground(71, 3),
                Ground(71, 4),
                Ground(71, 5),
                Ground(71, 6),
                Ground(71, 7),
                Ground(71, 8),

                Ground(72, 1),
                Ground(72, 2),
                Ground(72, 3),
                Ground(72, 7),
                Ground(72, 8),

                Ground(73, 1),
                Ground(73, 2),
                Ground(73, 8),

                Ground(74, 1),

                Ground(75, 1),

                Ground(110, 1),

                Ground(111, 3),
                Ground(111, 2),
                Ground(111, 1),

                Ground(112, 4),
                Ground(112, 3),
                Ground(112, 2),
                Ground(112, 1),

                Ground(113, 5),
                Ground(113, 4),
                Ground(113, 3),
                Ground(113, 2),
                Ground(113, 1),

                Ground(114, 6),
                Ground(114, 5),
                Ground(114, 4),
                Ground(114, 3),
                Ground(114, 2),
                Ground(114, 1),

                Ground(115, 6),
                Ground(115, 5),
                Ground(115, 4),
                Ground(115, 3),
                Ground(115, 2),
                Ground(115, 1),

                Ground(116, 5),
                Ground(117, 5),
                Ground(118, 5),

                Ground(1, 5),
                ]

    for i in list_grs:
        No_Blocks_Down = False
        for x in list_grs:
            if i.MakeSelfRect().bottom == x.MakeSelfRect().top and i.MakeSelfRect().left == x.MakeSelfRect().left:
                No_Blocks_Down = False
        if No_Blocks_Down:
            for m in range((((700 - i.y_position) + b_size) // b_size)): #self.y_position = 700 - ((y_pos * b_size) - b_size)
                # break_out = False
                # for x in list_grs:
                #     if i.x_position == x.MakeSelfRect().left and 700 - ((m * b_size) - b_size) == x.MakeSelfRect().top + 5:
                #         break_out = True
                # if break_out:
                #     break
                list_grs.append(Ground(((i.x_position + b_size) // b_size), m)) # ((i.x_position + b_size) // b_size)

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


    plats = [SilverThickPlat(7, 8),
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
            ]

    list_blocks = [GoldBlock(40, 5),
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

                   SmallOrangeBlock(74, 8.5),
                   SmallOrangeBlock(73, 7.5),
                   SmallOrangeBlock(72, 6.5),
                   SmallOrangeBlock(72, 4),
                   SmallOrangeBlock(73, 3),
                   SmallOrangeBlock(74, 2),

                   SilverBlock(98, 18),
                   SilverBlock(107, 18),
                   ]


    player_1 = Player(2, 3)

    start_game_arrow = StartGame(1, 2, 1)
    start_game_stage = StartGame(1.4, 2, 2)
    start_games = []

    check_ps = [Checkpoint(73, 9)]

    end_game_1 = EndGame(15, 2)
    end_games = []

    fly_plats = [FlyPlat(17, 16, 25,"RightLeft"),
                 FlyPlat(44, 8, 54,"RightLeft"),
                 FlyPlat(78, 7, 2,"UpDown"),
                 FlyPlat(80, 8, 84,"RightLeft"),
                 FlyPlat(86, 11, 4, "UpDown"),
                 ]

    jump_pads = [JumpPad(11, 5),
                 JumpPad(47, 2),
                 JumpPad(59, 3),]

    expand_plats = [ExpandPlat(65, 3)]


    spikes = [Spike(21, 3),
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
              ]

    saws = [Saw(29.5, 1.5, 3),
            Saw(52.5, 0.5, 3),]

    spiked_balls = []#Siked_Ball(36, 7)]

    fires = [Fire(40, 2),
             Fire(41, 2),
             Fire(42, 2),
             Fire(43, 2),
             ]


    # jump_pad = apple, fly_plat = banana, expand_plat = cherry

    fruits = [Fruit(6, 9, "b"),
              Fruit(27, 3, "a"),
              Fruit(29, 14, "c"),
              Fruit(33, 4, "a"),
              Fruit(40, 6, "a"),
              Fruit(52, 7, "b"),
              Fruit(65, 4, "b"),
              Fruit(72, 9, "b"),
              Fruit(94, 19, "c"),
              ]

    coins = [Coin(1, 5),
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

    snakes = [Snake(25, 4),
              Snake(41, 6),
              Snake(51, 7),]

    mushrooms = [Mushroom(6, 2),
                 Mushroom(19, 2),
                 Mushroom(23, 4)]

    horse_1 = Horse(7, 2)
    horse_2 = Horse(15, 3)
    horses = []

    mummy_1 = Mummy(7, 2, 5, 8)
    mummys = []

    box_1 = Box(5, 4)
    boxes = []

    touch_objects = list_grs + plats + fires + list_blocks


    # touch_objects = [gr_1, gr_2, gr_3, gr_4, gr_5, gr_6, gr_7, gr_8, gr_9, gr_10, gr_11, gr_12, gr_13, gr_14, gr_15, gr_16, gr_17, gr_18,
    #                  brick_1, orange_b1, silver_b1, gold_b1, brown_b1, gold_thin_plat1, silver_thin_plat1,
    #                  wood_thin_plat1, gold_thick_plat1, silver_thick_plat1, brown_thick_plat1, orange_thick_plat1,
    #                  small_silver_b1, small_gold_b1, small_brown_b1, small_orange_b1, jump_pad_1, fire_1, fly_plat_1, start_game_stage, end_game_1,]

def reset():
    global move_scene_x
    global move_scene_y
    global player_1
    global fall_jump
    if checkpoints == 0:
        move_scene_x = 0
        move_scene_y = 0
        player_1.x_position = 75
        player_1.y_position = 550 - 1
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
        if player_1.MakePlayerRect().colliderect(x.MakeRect(x.default)):
            reset()

    for x in range(len(mushrooms)):
        try:
            player_1.MakePlayerRect().bottom == mushrooms[x].MakeSelfRect().top and player_1.MakePlayerRect().left < mushrooms[x].MakeSelfRect().right and player_1.MakePlayerRect().right > mushrooms[x].MakeSelfRect().left

        except:
            pass

        else:
            if player_1.MakePlayerRect().bottom == mushrooms[x].MakeSelfRect().top and player_1.MakePlayerRect().left < \
                    mushrooms[x].MakeSelfRect().right and player_1.MakePlayerRect().right > mushrooms[x].MakeSelfRect().left:
                fall_jump = 15
                mushrooms.pop(x)
            elif player_1.MakePlayerRect().colliderect(mushrooms[x].MakeRect(mushrooms[x].default)):
                reset()

    for x in spikes + saws + spiked_balls:
        if player_1.MakePlayerRect().colliderect(x.MakeSelfRect()):
            reset()

    for x in fires:
        if player_1.MakePlayerRect().colliderect(x.MakeSelfRectFire()) and x.default == x.stage_on:
            reset()

    for x in horses + mummys:
        if player_1.MakePlayerRect().colliderect(x.MakeSelfRect()): # and x.default == x.hit_4:
            reset()

    if player_1.MakePlayerRect().top > 700:
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




pygame.init()
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption('Wonderland Escape')

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

coin = pygame.image.load("coin.png")
coin = pygame.transform.scale(coin, (30, 30))
coin_rect = coin.get_rect(topleft=(850, 5))

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

        best_score_text = text.render(f"Best Score", True, 'Black')
        best_score_text_rect = best_score_text.get_rect(center=(650, 450))

        screen.blit(best_score_text, best_score_text_rect)

        best_score_num_text = text.render(f"{"0" if best_score == 1000000000 else best_score / 1000} s", True, 'Black')
        best_score_num_text_rect = best_score_num_text.get_rect(center=(650, 525))

        screen.blit(best_score_num_text, best_score_num_text_rect)

        pygame.display.update()
        clock.tick(70)

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