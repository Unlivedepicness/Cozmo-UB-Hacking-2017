import cozmo
import cozmo_speech_recognition as csr
import cozmo_intent_dispatcher as cid
import cozmo.anim

# Load intents
from intents.pass_butter import intent_pass_butter
from intents.get_time import intent_get_time
from intents.talk import intent_talk
from intents.twitter_message import intent_twitter_message
from intents.rickroll import intent_rickroll
from intents.solve_maze import intent_solve_maze
from intents.jokes import intent_jokes
from intents.get_weather import intent_get_weather

from intents.response import create_response_intent

# Words that trigger a command to begin
activate_commands = ["cozmo", "cosmo", "cosimo", "kozmo", "kosmo", "kosimo", "osmo"]


def cozmo_setup_intents():
    """
    Setup intent callbacks
    Intents are configured int `utterances.txt`
    :return: None
    """
    cid.register_intent('PassButterIntent',     intent_pass_butter)
    cid.register_intent('HelloWorldIntent',     create_response_intent('Hello, world!'))
    cid.register_intent('TimeIntent',           intent_get_time)
    cid.register_intent('TalkIntent',           intent_talk)
    cid.register_intent('TakePictureIntent',    intent_twitter_message)
    cid.register_intent('RickRollIntent',       intent_rickroll)
    cid.register_intent('StarCraftIntent',      create_response_intent('In the rear with the gear'))
    cid.register_intent('MeanIntent',           intent_mean)
    cid.register_intent('ComplimentIntent',     create_response_intent('I love you too'))
    cid.register_intent('GoodBoyIntent',        create_response_intent(['Me. I am a good boy.', 'Are you proud of me?']))
    cid.register_intent('JokeIntent',           intent_jokes)
    cid.register_intent('PushToMasterIntent',   create_response_intent('You get a minus one'))
    cid.register_intent('DidYouKnowIntent',     create_response_intent(['Did you know I don\'t care', 'No', 'Of course I am all knowing']))
    cid.register_intent('WeatherIntent',        intent_get_weather)


def cozmo_init(robot: cozmo.robot.Robot):
    """
    Main entry point
    :param robot: Populated by Cozmo SDK
    :return: None
    """

    # Reset to default position
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    # Load the intents for the speech recognition
    csr.load_intents()

    # Load the intent callbacks
    cozmo_setup_intents()

    while True:

        # Enable built-in freeplay while waiting for a voice command
        robot.start_freeplay_behaviors()
        csr.wait_for_any(robot, activate_commands)
        robot.stop_freeplay_behaviors()

        robot.say_text('What is my purpose?').wait_for_completed()

        # Try to receive a valid command
        while True:
            # Grab user speech input
            speech = csr.wait_for_speech(robot)

            # Attempt to process the user intent
            intent = csr.process_intent(speech)

            if intent is not None:
                # An intent was found, dispatch it then go back to idle mode
                cid.dispatch(intent, robot)
                break
            else:
                robot.say_text('What?').wait_for_completed()


cozmo.run_program(cozmo_init, use_viewer=True)
# cozmo.run_program(intent_solve_maze, use_viewer=True)
