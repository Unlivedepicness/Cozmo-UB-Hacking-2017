import cozmo


def intent_pass_butter(robot: cozmo.robot.Robot):
    robot.move_lift(0)
    robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()

    robot.say_text('Oh my god').wait_for_completed()

    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
