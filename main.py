import cozmo
import cozmo_speech_recognition as csr
import cozmo_intent_dispatcher as cid

# Load intents
from intents.pass_butter import intent_pass_butter
from intents.hello_world import intent_hello_world

# Words that trigger a command to begin
activate_commands = ["cozmo", "cosmo", "cosimo", "kozmo", "kosmo", "kosimo", "osmo"]


def cozmo_setup_intents():
    cid.register_intent('PassButterIntent', intent_pass_butter)
    cid.register_intent('HelloWorldIntent', intent_hello_world)


def cozmo_init(robot: cozmo.robot.Robot):
    # Reset to default position
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    csr.load_intents()
    cozmo_setup_intents()

    while True:

        # Wait for activate command
        csr.wait_for_any(activate_commands)
        robot.say_text('What is my purpose?').wait_for_completed()

        # Try to receive a valid command
        while True:
            speech = csr.wait_for_speech(robot)

            intent = csr.process_intent(speech)

            if intent is not None:
                cid.dispatch(intent, robot)
                break
            else:
                robot.say_text('What?').wait_for_completed()


cozmo.run_program(cozmo_init)
