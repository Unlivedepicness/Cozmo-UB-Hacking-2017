import cozmo

from cozmo.util import degrees, speed_mmps, distance_mm, Pose


class World:
    walls = set()

    def create_objects(self, robot: cozmo.robot.Robot, position):
        for wall in self.walls:
            w_relative_y = wall[0] - position[0]
            w_relative_x = wall[1] - position[1]

            robot.world.create_custom_fixed_object(
                Pose(95 * w_relative_x, 95 * w_relative_y, 0, angle_z=degrees(0)),
                95, 95, 95,
                relative_to_robot=True)

    def create_wall(self, x, y):
        self.walls += (x, y)

    def create_bounds(self, width, height):
        for x in range(0, width):
            self.create_wall(x, 0)
            self.create_wall(x, width)

        for y in range(0, height):
            self.create_wall(0, y)
            self.create_wall(width, y)


world = World()
world.create_bounds(12, 12)
world.create_wall(2, 1)
world.create_wall(2, 2)
world.create_wall(2, 3)
world.create_wall(2, 4)
world.create_wall(2, 5)


def intent_solve_maze(robot: cozmo.robot.Robot):
    world.create_objects(robot, (2, 2))
    robot.go_to_pose(Pose(5 * 95, 5 * 95, 0, angle_z=degrees(0)), relative_to_robot=True).wait_for_completed()
    pass
