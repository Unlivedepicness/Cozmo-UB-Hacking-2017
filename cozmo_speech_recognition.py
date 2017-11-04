import speech_recognition as sr
import cozmo
import re

from cozmo import logger

r = sr.Recognizer()
intents = []


def load_intents():
    global intents

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
    words = words.split(' ')
    expression = expression.split(' ')

    matched_words = 0
    for target in expression:
        if target in words:
            matched_words += 1

    return matched_words / len(expression) >= threshold


def loose_matches_any(words, expressions, threshold=0.6):
    for expression in expressions:
        if loose_match(words, expression, threshold):
            return True

    return False


def _listen(timeout, phrase_time_limit):
    logger.info('Starting audio listening, timeout = %d, phrase_time_limit = %d' % (timeout, phrase_time_limit))

    with sr.Microphone() as source:
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

    logger.info('Recognizing audio ...')

    try:
        text = str(r.recognize_google(audio)).lower()
        logger.info('Words: %s' % text)
        return text
    except sr.UnknownValueError:
        logger.info('Failed to recognize any words')
    except sr.RequestError:
        logger.error('Service down')

    return None


def wait_for_any(valid_words):
    while True:
        words = _listen(timeout=1, phrase_time_limit=3)

        if words is None:
            continue

        words = words.split(' ')

        for word in words:
            if word in valid_words:
                return


def wait_for_speech(robot: cozmo.robot.Robot):
    while True:
        words = _listen(timeout=1, phrase_time_limit=3)

        if words is None:
            robot.say_text('Speak clearly, you dummy!').wait_for_completed()
        else:
            return words


def process_intent(text):
    thresholds = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]

    logger.info('Matching text to intent: %s' % text)
    for threshold in thresholds:
        logger.info('Trying intent matching with threshold = %f' % threshold)
        for intent in intents:
            if loose_match(words=text, expression=intent['text'], threshold=threshold):
                return intent['intents']

    return None
