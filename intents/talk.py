import cozmo

import cozmo_speech_recognition as csr

from cleverwrap import CleverWrap

CLEVERBOT_API_KEY = "CC59kXXxNA8GzoL1x51AyEFxMYg"


def intent_hello_world(robot: cozmo.robot.Robot):
    cb = CleverWrap(CLEVERBOT_API_KEY)

    while True:
        speech = csr.wait_for_speech(robot)

        if csr.loose_match(speech, 'bye', 1):
            robot.say_text('Goodbye').wait_for_completed()
            return

        reply = cb.say(speech)
        robot.say_text(reply).wait_for_completed()
