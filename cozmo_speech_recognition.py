import speech_recognition as sr
import cozmo
import re

from cozmo import logger

r = sr.Recognizer()
intents = []


def load_intents():
    """
    Load configured intents from `utterances.txt`
    :return: None
    """
    global intents

    # Format: <IntentName> <speech utterance>
    r_utterance = re.compile('^(\w+) (.*)$')

    logger.info('Loading utterances ...')

    with open('utterances.txt') as file:
        utterances = file.read().split('\n')
        for utterance in utterances:
            match = r_utterance.match(utterance)
            intents.append({
                'intents': match.group(1),
                'text': match.group(2)
            })

    logger.info('Loaded %d utterance(s)' % len(intents))


def loose_match(words, expression, threshold=0.6):
    """
    Attempt to loosely match some speech to a target expression with a given threshold
    :param words: The words that are being tested (string)
    :param expression: The expression that is being tested against
    :param threshold: The percentage of how similar the words should be (from 0.0 to 1.0)
    :return: If the words and expression loosely match
    """
    words = words.split(' ')
    expression = expression.split(' ')

    matched_words = 0
    for target in expression:
        if target in words:
            matched_words += 1

    return matched_words / len(expression) >= threshold


def loose_matches_any(words, expressions, threshold=0.6):
    """
    Loosely match some speech to any of the given expressions
    :param words: The words that are being tested (string)
    :param expressions: A list of expressions being tested against
    :param threshold: The percentage of how similar the words should be (from 0.0 to 1.0)
    :return:
    """
    for expression in expressions:
        if loose_match(words, expression, threshold):
            return True

    return False


def _listen(timeout, phrase_time_limit):
    """
    Listen for speech input until some is found
    :param timeout: The timeout for listening
    :param phrase_time_limit: The max length of the phrase
    :return: The detected speech
    """
    logger.info('Starting audio listening, timeout = %d, phrase_time_limit = %d' % (timeout, phrase_time_limit))

    # Grab some audio from the microphone
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

    logger.info('Recognizing audio ...')

    try:
        # Use google to parse the audio, ensure the resulting string is all lowercase, and remove apostrophes
        text = str(r.recognize_google(audio)).lower().replace('\'', '')
        logger.info('Words: %s' % text)
        return text
    except sr.UnknownValueError:
        logger.info('Failed to recognize any words')
    except sr.RequestError:
        logger.error('Service down')

    # There was an exception, return None
    return None


def wait_for_any(valid_words):
    """
    Wait until the speech input contains any of the inputted words
    :param valid_words: Words to check for
    :return: None
    """
    while True:
        # Grab some user speech
        words = _listen(timeout=1, phrase_time_limit=3)

        # If nothing was found, try again
        if words is None:
            continue

        # Split the user speech into words
        words = words.split(' ')

        # Check each of the words to see if it matches the target words
        for word in words:
            if word in valid_words:
                return


def wait_for_speech(robot: cozmo.robot.Robot):
    """
    Wait for valid user speech
    :param robot: Cozmo robot
    :return: Speech text
    """
    while True:
        # Enable backpack lights to signify listening
        robot.set_all_backpack_lights(cozmo.lights.blue_light)

        # Grab user speech
        words = _listen(timeout=1, phrase_time_limit=3)

        # Disable backpack lights during processing
        robot.set_backpack_lights_off()

        if words is None:
            robot.say_text('Speak clearly, you dummy!').wait_for_completed()
        else:
            return words


def process_intent(text):
    """
    Attempt to process what the intent of a given text is
    :param text: Text to process
    :return: Intent name, if any
    """

    # Thresholds to check
    thresholds = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]

    logger.info('Matching text to intent: %s' % text)

    # For each threshold (starting at 100% match to 50% match)
    for threshold in thresholds:
        logger.info('Trying intent matching with threshold = %f' % threshold)

        # For each known intent
        for intent in intents:

            # Check to see if the text loosely matches the intent's utterance with the current threshold
            if loose_match(words=text, expression=intent['text'], threshold=threshold):
                return intent['intents']

    return None
