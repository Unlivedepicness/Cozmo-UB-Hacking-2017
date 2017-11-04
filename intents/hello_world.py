import cozmo


def intent_hello_world(robot: cozmo.robot.Robot):
    robot.say_text('Hello world').wait_for_completed()
