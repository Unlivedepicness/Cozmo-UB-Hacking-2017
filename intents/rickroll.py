import cozmo
import time

lyrics = [
    ("Never gonna", 0.0), ("give you", 0.5), ("up", "0.3")
]


def intent_rickroll(robot: cozmo.robot.Robot):
    for line in lyrics:
        robot.say_text(line[0], voice_pitch=line[1]).wait_for_completed()
