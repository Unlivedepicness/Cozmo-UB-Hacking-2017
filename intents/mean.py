import cozmo


def intent_mean(robot: cozmo.robot.Robot):
    robot.set_lift_height(height=0.7).wait_for_completed()
    robot.say_text('up yours').wait_for_completed()
    robot.set_lift_height(height=0.0).wait_for_completed()
