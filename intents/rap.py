import cozmo


lyrics = [
    "I need a double cheeseburger and hold the lettuce",
    "Don't be frontin' son no seeds on a bun",
    "We be up in this drive thru, Order for two",
    "I gots a craving for a number nine like my shoe",
    "We need some chicken up in here, In this dizzle",
    "For rizzle my nizzle, Extra salt on the frizzle",
    "Dr. Pepper my brother, Another for your mother",
    "Double double super size, And don't forget the fries!"
]


def intent_rap(robot: cozmo.robot.Robot):
    for line in lyrics:
        robot.say_text(
            text=line,
            duration_scalar=0.7).wait_for_completed()
