import cozmo
import asyncio

from cozmo.util import distance_mm, speed_mmps, degrees


def intent_pass_butter(robot: cozmo.robot.Robot):
    robot.set_lift_height(height=0.7).wait_for_completed()
    robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()

    robot.say_text('oh my god').wait_for_completed()

    robot.set_lift_height(height=0.0).wait_for_completed()
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cube = None

    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
    except asyncio.TimeoutError:
        robot.say_text('I cannot find the butter. I have failed my purpose.')
        robot.play_anim_trigger(cozmo.anim.Triggers.CubeMovedUpset).wait_for_completed()
    finally:
        look_around.stop()

    if cube:
        action = robot.dock_with_cube(cube, approach_angle=degrees(0), num_retries=3)
        action.wait_for_completed()

        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.say_text('oh my god', duration_scalar=1.8).wait_for_completed()