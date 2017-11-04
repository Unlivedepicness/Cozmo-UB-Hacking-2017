import cozmo

import cozmo_speech_recognition as csr

from cleverwrap import CleverWrap
from cozmo import logger

CLEVERBOT_API_KEY = "CC59kXXxNA8GzoL1x51AyEFxMYg"


def intent_talk(robot: cozmo.robot.Robot):
    cb = CleverWrap(CLEVERBOT_API_KEY)
    robot.say_text('What do you want to talk about?').wait_for_completed()

    while True:
        speech = csr.wait_for_speech(robot)

        if csr.loose_matches_any(speech, ['bye', 'goodbye', 'good bye'], 1):
            robot.say_text('Goodbye').wait_for_completed()
            return

        reply = cb.say(speech)
        logger.info('Cleverbot says: %s' % reply)

        robot.say_text(reply).wait_for_completed()
