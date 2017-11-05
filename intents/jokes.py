import cozmo
import random


jokes = [
    [("yo mama so fat", 0.7), ("when I compute her mass with a recursive function", 0.7), ("i get a stack overflow", 1.5)],
    #[("yo mama so fat", 0.7), ("obi wan saw her and said", 0.7), ("that's no moon", 1.5)],
    #[("yo mama so fat", 0.7), ("schrodinger found her to be both inside and outside of the box", 1.0)],
    #[("yo mama so fat", 0.7), ("she can collapse a wave function by sitting on it", 1.0)],
    #[("yo mama so fat", 0.7), ("kurt godel used her to signify the set of all sets that contain themselves", 1.0)],
    #[("knock knock", 0.7), ("race condition", 0.7), ("who's there", 0.7)],
    #[("yo mama so fat", 0.7), ("the probability that she is in an arbitrary point in a room", 0.7), ("is one", 1.5)],
    #[("yo mama so fat", 0.7), ("she sat on a binary tree and flattened it to a linked list", 0.7), ("in constant time", 1.5)]
]


def intent_jokes(robot: cozmo.robot.Robot):
    joke = random.choice(jokes)
    for line in joke:
        robot.say_text(line[0], duration_scalar=line[1]).wait_for_completed()

    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabExcited).wait_for_completed()
