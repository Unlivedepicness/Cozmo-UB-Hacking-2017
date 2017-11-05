import cozmo

lyrics = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you"
]


def intent_rickroll(robot: cozmo.robot.Robot):
    for line in lyrics:
        robot.say_text(
            text=line,
            duration_scalar=0.7).wait_for_completed()
