import cozmo

from cozmo.util import degrees, speed_mmps, distance_mm, Pose


class World:
    walls = []

    def create_objects(self, robot: cozmo.robot.Robot, position):
        print(self.walls)
        for wall in self.walls:
            w_relative_y = wall[0] - position[0]
            w_relative_x = wall[1] - position[1]

            robot.world.create_custom_fixed_object(
                Pose(95 * w_relative_x, 95 * w_relative_y, 0, angle_z=degrees(0)),
                95, 95, 95,
                relative_to_robot=True)

    def create_wall(self, x, y):
        self.walls.append((x, y))

    def create_bounds(self, width, height):
        for x in range(0, width):
            self.create_wall(x, 0)
            self.create_wall(x, width)

        for y in range(0, height):
            self.create_wall(0, y)
            self.create_wall(width, y)

        self.walls = list(set(self.walls))

    def __str__(self):
        s = ''
        for x in range(0, 12):
            for y in range(0, 12):
                if (x, y) in self.walls:
                    s += '*'
                else:
                    s += '.'
            s += '\n'
        return s


world = World()

world.create_wall(4, 1)
world.create_wall(4, 2)
world.create_wall(4, 3)
world.create_wall(4, 4)
world.create_wall(4, 5)
world.create_wall(4, 6)
world.create_wall(4, 7)
world.create_wall(4, 8)
world.create_wall(4, 9)
world.create_wall(4, 10)


def intent_solve_maze(robot: cozmo.robot.Robot):
    print(str(world))
    world.create_objects(robot, (2, 2))
    robot.go_to_pose(Pose(2 * 95, 2 * 95, 0, angle_z=degrees(0)), relative_to_robot=True).wait_for_completed()
    pass
