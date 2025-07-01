import pygame
import time

#Player size = x 50, y 60

# variables
# -------------------------
level = "level_1"
b_size = 100
p_size_x = 50
p_size_y = 60
track_width = 4000
fall_jump = 0
move_scene = 0
mode = "fall"
side = "r"
checkpoints = 0
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
        return surface.get_rect(bottomleft=(self.x_position - move_scene, self.y_position))


    def ObjectRight(self, surface):
        TF = False
        for i in touch_objects:
            if surface.right == i.MakeRect(i.default).left and surface.bottom > i.MakeRect(i.default).top and surface.top < i.MakeRect(i.default).bottom:
                TF = True
        return TF

    def ObjectLeft(self, surface):
        TF = False
        for i in touch_objects:
            if surface.left == i.MakeRect(i.default).right and surface.bottom > i.MakeRect(i.default).top and surface.top < i.MakeRect(i.default).bottom:
                TF = True
        return TF

    def ObjectUp(self, surface):
        TF = False
        for i in touch_objects:
            if surface.top == i.MakeRect(i.default).bottom and surface.left < i.MakeRect(i.default).right and surface.right > i.MakeRect(i.default).left:
                TF = True
        return TF

    def ObjectDown(self, surface, width = 0):
        TF = False
        for i in touch_objects:
            if surface.bottom == i.MakeRect(i.default).top and surface.left + width < i.MakeRect(i.default).right and surface.right + width > i.MakeRect(i.default).left:
                TF = True
        return TF


    # def PushOut(self, surface):
    #     y_push = 0
    #     for i in touch_objects:
    #         if surface.bottom > i.MakeRect(i.default).top and surface.top < i.MakeRect(i.default).bottom and surface.left < i.MakeRect(i.default).right and surface.right > i.MakeRect(i.default).left:
    #             y_push = i.MakeRect(i.default).top
    #     return y_push


    def FallRight(self, surface):
        FallRightTF = self.ObjectDown(surface, surface.width)
        return self.ObjectDown(surface, surface.width)

    def FallLeft(self, surface):
        # FallLeftTF = True
        # for i in touch_objects:
        #     if surface.bottom == i.MakeRect(i.default).top and surface.left - b_size < i.MakeRect(i.default).right and surface.right - b_size > i.MakeRect(i.default).left:
        #         FallLeftTF = False
        return self.ObjectDown(surface, -surface.width)


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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

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

        self.left_side_pos = self.x_position
        self.right_side_pos = self.x_position + b_size
        self.bottom_side_pos = self.y_position
        self.top_side_pos = self.y_position - b_size

        self.default = pygame.image.load("Plat_Thin_Wood.png")
        self.default = pygame.transform.scale(self.default, (b_size, b_size / 10))

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


class Player(Object):
    """
    Character that will move on screen
    """
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

        self.transparency = 0

        self.default = pygame.image.load("stand_1.png")
        self.default = pygame.transform.scale(self.default, (50, 60))

        self.stand_1 = pygame.image.load("stand_1.png")
        self.stand_1 = pygame.transform.scale(self.stand_1, (50, 60))
        self.stand_2 = pygame.image.load("stand_2.png")
        self.stand_2 = pygame.transform.scale(self.stand_2, (50, 60))
        self.standing = [self.stand_1 for _ in range(10)] + [self.stand_2 for _ in range(10)]

        self.run_1 = pygame.image.load("run_1.png")
        self.run_1 = pygame.transform.scale(self.run_1, (50, 60))
        self.run_2 = pygame.image.load("run_2.png")
        self.run_2 = pygame.transform.scale(self.run_2, (50, 60))
        self.run_3 = pygame.image.load("run_3.png")
        self.run_3 = pygame.transform.scale(self.run_3, (50, 60))
        self.run_4 = pygame.image.load("run_4.png")
        self.run_4 = pygame.transform.scale(self.run_4, (50, 60))
        self.run_5 = pygame.image.load("run_5.png")
        self.run_5 = pygame.transform.scale(self.run_5, (50, 60))
        self.run_6 = pygame.image.load("run_6.png")
        self.run_6 = pygame.transform.scale(self.run_6, (50, 60))
        self.run_7 = pygame.image.load("run_7.png")
        self.run_7 = pygame.transform.scale(self.run_7, (50, 60))
        self.run_8 = pygame.image.load("run_8.png")
        self.run_8 = pygame.transform.scale(self.run_8, (50, 60))
        self.running = [self.run_1, self.run_2, self.run_3, self.run_4, self.run_5, self.run_6, self.run_7, self.run_8]

        self.jump = pygame.image.load("jump.png")
        self.jump = pygame.transform.scale(self.jump, (50, 60))

        self.wall_jump = pygame.image.load("wall_jump.png")
        self.wall_jump = pygame.transform.scale(self.wall_jump, (50, 60))

        self.fall = pygame.image.load("fall.png")
        self.fall = pygame.transform.scale(self.fall, (50, 60))

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


    def MoveRight(self, num = 5):
        """Moves to the right"""
        for i in range(num):
            global move_scene
            if not self.ObjectRight(self.MakePlayerRect()):
                if self.MakePlayerRect().centerx < 650:  #move_scene == 0 and
                    self.x_position += 1
                elif move_scene == track_width - 1300 and self.MakePlayerRect().centerx >= 650 and self.MakePlayerRect().right != 1300:
                    self.x_position += 1
                elif move_scene < track_width - 1300:
                    move_scene += 1

    def MoveLeft(self, num = 5):
        """Moves to the left"""
        for i in range(num):
            global move_scene
            if not self.ObjectLeft(self.MakePlayerRect()):
                if move_scene == 700 and self.MakePlayerRect().centerx > 650:
                    self.x_position -= 1
                elif move_scene == 0 and self.MakePlayerRect().centerx <= 650 and self.MakePlayerRect().left != 0:
                    self.x_position -= 1
                elif move_scene > 0:
                    move_scene -= 1


    def Minus_Fall_Jump_Speed(self, num):
        """
        Changes the y position of player
        :param num: fall_jump
        :return: None
        """
        global mode
        for i in range(abs(num)):
            if num < 0:
                if not self.ObjectDown(self.MakePlayerRect()):
                    check_die()
                    player_1.y_position += 1
            elif num > 0:
                if not self.ObjectUp(self.MakePlayerRect()):
                    player_1.y_position -= 1


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

        self.snaking = [self.default, self.default, self.default, self.default, self.default, self.snake_1, self.snake_1, self.snake_1, self.snake_1, self.snake_1, self.snake_2, self.snake_2, self.snake_2, self.snake_2, self.snake_2, self.snake_3, self.snake_3, self.snake_3, self.snake_3, self.snake_3]

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def Move(self):
        # print(self.FallRight(self.MakeSelfRect()))
        if self.side == "r":
            for i in range(3):
                if not self.ObjectRight(self.MakeSelfRect()) and self.FallRight(self.MakeSelfRect()):
                    if move_scene == track_width - 1300 and self.MakeSelfRect().right == 1300:
                        self.side = "l"
                    else:
                        self.x_position += 1
                else:
                    self.side = "l"

        if self.side == "l":
            for i in range(3):
                if not self.ObjectLeft(self.MakeSelfRect()) and self.FallLeft(self.MakeSelfRect()):
                    if move_scene == track_width - 1300 and self.MakeSelfRect().right == 1300:
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

        self.mushrooming = [self.default, self.default,
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
                    if move_scene == track_width - 1300 and self.MakeSelfRect().right == 1300:
                        self.side = "l"
                    else:
                        self.x_position += 1
                else:
                    self.side = "l"

        if self.side == "l":
            for i in range(4):
                if not self.ObjectLeft(self.MakeSelfRect()) and self.FallLeft(self.MakeSelfRect()):
                    if move_scene == track_width - 1300 and self.MakeSelfRect().right == 1300:
                        self.side = "r"
                    else:
                        self.x_position -= 1
                else:
                    self.side = "r"
                # if move_scene != 0 or self.MakeSelfRect().left != 0:
                # else:
                #     self.side = "r"


class FlyPlat(Object):
    def __init__(self, x_pos, y_pos, pos_1, pos_2, fly):
        super().__init__(x_pos, y_pos)

        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.fly = fly

        if fly == "RightLeft":
            # self.fly_pos = (fly_pos * b_size) - b_size
            self.direction = "r"
        else:
            # self.fly_pos = 700 - ((fly_pos * b_size) - b_size)
            self.direction = "d"


        self.default = pygame.image.load("Plat_Fly_1.png")
        self.default = pygame.transform.scale(self.default, (b_size, 30))
        self.fly_plat_1 = pygame.image.load("Plat_Fly_2.png")
        self.fly_plat_1 = pygame.transform.scale(self.fly_plat_1, (b_size, 30))
        self.fly_plat_2 = pygame.image.load("Plat_Fly_3.png")
        self.fly_plat_2 = pygame.transform.scale(self.fly_plat_2, (b_size, 30))
        self.fly_plat_3 = pygame.image.load("Plat_Fly_4.png")
        self.fly_plat_3 = pygame.transform.scale(self.fly_plat_3, (b_size, 30))

        self.FlyPlating = [self.default, self.default, self.fly_plat_1, self.fly_plat_1,
                           self.fly_plat_2, self.fly_plat_2, self.fly_plat_3, self.fly_plat_3]

    def MakeSelfRect(self):
        return self.MakeRect(self.default)

    def Move(self, num = 5):
        global fall_jump
        for x in range(num):
            if self.fly == "UpDown":
                if self.direction == "u":
                    if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                        if player_1.ObjectUp(player_1.MakePlayerRect()):
                            self.direction = "d"
                            reset()
                else:
                    if self.MakeSelfRect().bottom == player_1.MakePlayerRect().top and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                        self.direction = "u"
                    if self.MakeSelfRect().bottom == player_1.MakePlayerRect().top and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                        if player_1.ObjectDown(player_1.MakePlayerRect()):
                            self.direction = "u"
                            reset()


            if self.fly == "RightLeft":
                if self.direction == "r":
                    if self.MakeSelfRect().left + move_scene != self.pos_2:
                        self.x_position += 1
                        if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                            player_1.MoveRight(1)
                            # player_1.x_position += 1
                    else:
                        self.direction = "l"

                if self.direction == "l":
                    if self.MakeSelfRect().left + move_scene != self.pos_1:
                        self.x_position -= 1
                        if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                            player_1.MoveLeft(1)
                            # player_1.x_position -= 1
                    else:
                        self.direction = "r"
            else:
                if self.direction == "d":
                    if self.MakeSelfRect().bottom != self.pos_2:
                        if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                            player_1.y_position += 1
                            fall_jump = 0
                        self.y_position += 1
                    else:
                        self.direction = "u"

                if self.direction == "u":
                    if self.MakeSelfRect().bottom != self.pos_1:
                        if self.MakeSelfRect().top == player_1.MakePlayerRect().bottom and self.MakeSelfRect().left < player_1.MakePlayerRect().right and self.MakeSelfRect().right > player_1.MakePlayerRect().left:
                            player_1.y_position -= 1
                            fall_jump = 0
                        self.y_position -= 1
                    else:
                        self.direction = "d"


player_1 = Player(0, 0)
check_p_1 = Checkpoint(0, 0)


def blit():
    """Blits all the objects"""
    global player_1

    screen.blit(blue_sky, blue_sky_rect)

    for i in list_grs:
        grass_TF = True
        for x in list_grs:
            if i.MakeSelfRect().top == x.MakeSelfRect().bottom and i.MakeSelfRect().left == x.MakeSelfRect().left:
                grass_TF = False
        if grass_TF:
            screen.blit(i.grass, i.MakeSelfRect())
        else:
            screen.blit(i.default, i.MakeSelfRect())

    for x in set(touch_objects) - set(list_grs) - set(fly_plats):
        screen.blit(x.default, x.MakeRect(x.default))


    if check_p_1.checkpoint_TF:
        screen.blit(check_p_1.checkpointing[0], check_p_1.MakeRect(check_p_1.checkpoint_1))
        check_p_1.checkpointing.append(check_p_1.checkpointing[0])
        check_p_1.checkpointing.pop(0)
    else:
        screen.blit(check_p_1.no_checkpoint, check_p_1.MakeRect(check_p_1.no_checkpoint))

    for x in snakes:
        if x.side == "l":
            screen.blit(x.snaking[0], x.MakeSelfRect())
        if x.side == "r":
            screen.blit(pygame.transform.flip(x.snaking[0], True, False), x.MakeSelfRect())
        x.snaking.append(x.snaking[0])
        x.snaking.pop(0)

    for x in mushrooms:
        if x.side == "l":
            screen.blit(x.mushrooming[0], x.MakeSelfRect())
        if x.side == "r":
            screen.blit(pygame.transform.flip(x.mushrooming[0], True, False), x.MakeSelfRect())
        x.mushrooming.append(x.mushrooming[0])
        x.mushrooming.pop(0)

    for x in fly_plats:
        screen.blit(x.FlyPlating[0], x.MakeSelfRect())
        x.FlyPlating.append(x.FlyPlating[0])
        x.FlyPlating.pop(0)


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


    screen.blit(go_back_button, go_back_button_rect)
    screen.blit(restart_button, restart_button_rect)

def keys_pressed():
    """What happens when keys are pressed"""
    global fall_jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if find_mode() == "wall":
            fall_jump = 0
            player_1.y_position += 1
        else:
            player_1.MoveRight()
    if keys[pygame.K_LEFT]:
        if find_mode() == "wall":
            fall_jump = 0
            player_1.y_position += 1
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

    else:
        mode = "stand"

    if fall_jump > 0:
        mode = "jump"
    elif fall_jump < 0 and not player_1.ObjectLeft(player_1.MakePlayerRect()) and not player_1.ObjectRight(player_1.MakePlayerRect()):
        mode = "fall"

    return mode

def start_play():
    global checkpoints
    global fall_jump
    global move_scene
    global mode
    global side
    global check_p_1
    global player_1
    global snakes
    global mushrooms
    global fly_plats
    global list_grs
    global touch_objects

    # variables
    # -------------------------
    fall_jump = 0
    move_scene = 0
    mode = "fall"
    side = "r"
    checkpoints = 0

    # -------------------------

    gr_1 = Ground(1, 1)
    gr_2 = Ground(2, 1)
    gr_3 = Ground(3, 1)
    gr_4 = Ground(4, 1)
    gr_5 = Ground(5, 1)
    gr_6 = Ground(6, 1)
    gr_7 = Ground(7, 1)
    gr_8 = Ground(8, 1)
    gr_9 = Ground(9, 1)
    gr_10 = Ground(10, 2)
    gr_11 = Ground(11, 2)
    gr_12 = Ground(12, 2)
    gr_13 = Ground(13, 2)
    gr_14 = Ground(14, 2)
    gr_15 = Ground(10, 1)
    gr_16 = Ground(15, 1)
    gr_17 = Ground(16, 1)
    gr_18 = Ground(17, 1)
    list_grs = [gr_1, gr_2, gr_3, gr_4, gr_5, gr_6, gr_7, gr_8, gr_9, gr_10, gr_11, gr_12, gr_13, gr_14, gr_15, gr_16, gr_17, gr_18]


    brick_1 = BrickBlock(2, 4)

    orange_b1 = OrangeBlock(3, 4)

    silver_b1 = SilverBlock(4, 4)

    gold_b1 = GoldBlock(5, 4)

    brown_b1 = BrownBlock(6, 4)



    gold_thin_plat1 = GoldThinPlat(7, 4)

    silver_thin_plat1 = SilverThinPlat(8, 4)

    wood_thin_plat1 = WoodThinPlat(9, 5)



    gold_thick_plat1 = GoldThickPlat(10, 5)

    silver_thick_plat1 = SilverThickPlat(11, 5)

    orange_thick_plat1 = OrangeThickPlat(12, 5)

    brown_thick_plat1 = BrownThickPlat(13, 5)



    small_silver_b1 = SmallSilverBlock(14, 5)

    small_gold_b1 = SmallGoldBlock(14, 5.5)
    small_gold_b2 = SmallGoldBlock(4, 6.5)

    small_orange_b1 = SmallOrangeBlock(14.5, 5)

    small_brown_b1 = SmallBrownBlock(15, 5)


    player_1 = Player(2, 2)

    check_p_1 = Checkpoint(12, 3)

    snake_1 = Snake(4, 2)
    snake_2 = Snake(7, 2)
    snake_3 = Snake(10, 3)
    snakes = [snake_1, snake_2, snake_3]

    mushroom_1 = Mushroom(7, 2)
    mushroom_2 = Mushroom(12, 3)
    mushrooms = [mushroom_1, mushroom_2]

    fly_plat_1 = FlyPlat(3, 6, 100, 600,"RightLeft")
    fly_plat_2 = FlyPlat(1, 3, 100, 600,"UpDown")
    fly_plats = [fly_plat_1, fly_plat_2]

    touch_objects = [gr_1, gr_2, gr_3, gr_4, gr_5, gr_6, gr_7, gr_8, gr_9, gr_10, gr_11, gr_12, gr_13, gr_14, gr_15, gr_16, gr_17, gr_18,
                     brick_1, orange_b1, silver_b1, gold_b1, brown_b1, gold_thin_plat1, silver_thin_plat1,
                     wood_thin_plat1, gold_thick_plat1, silver_thick_plat1, brown_thick_plat1, orange_thick_plat1,
                     small_silver_b1, small_gold_b1, small_brown_b1, small_orange_b1, fly_plat_1, fly_plat_2, small_gold_b2]

def reset():
    global move_scene
    global player_1
    global fall_jump
    if checkpoints == 0:
        move_scene = 0
        player_1.x_position = 50
        player_1.y_position = 600 - 1
    if checkpoints == 1:
        move_scene = 560
        player_1.x_position = 650 - p_size_x / 2
        player_1.y_position = 500 - 1
    fall_jump = 0
    player_1.transparency = 0

def check_die():
    global fall_jump
    global mushrooms

    # for x in snakes:
    #     if player_1.MakePlayerRect().colliderect(x.MakeRect(x.default)):
    #         reset()

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
            # elif player_1.MakePlayerRect().colliderect(mushrooms[x].MakeRect(mushrooms[x].default)):
            #     reset()

    if player_1.y_position > 700:
        reset()


pygame.init()
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption('Mario_2.0')

blue_sky = pygame.image.load("Blue_Sky.webp")
blue_sky = pygame.transform.rotozoom(blue_sky, 0, 6)
blue_sky_rect = blue_sky.get_rect(center=(100, 100))

orange_bck = pygame.image.load("Orange_Colour.png")
orange_bck = pygame.transform.rotozoom(orange_bck, 0, 1.5)
orange_bck_rect = orange_bck.get_rect(topleft=(0, 0))

play_button = pygame.image.load("Play_Button.png")
play_button = pygame.transform.rotozoom(play_button, 0, 0.1)
play_button_rect = play_button.get_rect(center=(650, 300))

go_back_button = pygame.image.load("Go_Back.png")
go_back_button = pygame.transform.rotozoom(go_back_button, 0, 0.1)
go_back_button_rect = play_button.get_rect(topright=(1674, 0))

restart_button = pygame.image.load("Restart.png")
restart_button = pygame.transform.rotozoom(restart_button, 0, 0.05)
restart_button_rect = play_button.get_rect(topleft=(0, 0))

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
        pygame.display.update()
        clock.tick(70)

    while level == "level_1":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_back_button_rect.collidepoint(event.pos):
                    level = "menu"
                if restart_button_rect.collidepoint(event.pos):
                    start_play()

        for x in snakes:
            x.Move()
        for x in mushrooms:
            x.Move()
        for x in fly_plats:
            x.Move()

        keys_pressed()
        check_p_1.CheckPoint()
        player_1.Change_Fall_Jump()
        player_1.Transparency()
        check_die()
        blit()

        pygame.display.update()
        clock.tick(70)