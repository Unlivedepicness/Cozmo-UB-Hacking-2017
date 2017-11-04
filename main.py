import asyncio
import cozmo
import time
import cozmo_speech_recognition as csr

from cozmo.util import degrees, distance_mm, speed_mmps

activate_commands = ["cozmo", "cosmo", "cosimo", "kozmo", "kosmo", "kosimo", "osmo"]


def cozmo_init(robot: cozmo.robot.Robot):
    csr.wait_for_any(activate_commands)

    while True:
        robot.say_text('What is my purpose?').wait_for_completed()
        speech = csr.wait_for_speech(robot)
        words = speech.split(' ')
        if 'you' in words and 'pass' in words and 'butter' in words:
            robot.say_text('Oh my god').wait_for_completed()
        else:
            robot.say_text('I\'m sorry dave, I can\'t do that').wait_for_completed()


csr.load_intents()
print(csr.process_intent('u pass butter'))
# cozmo.run_program(cozmo_init, use_viewer=True, force_viewer_on_top=True)
