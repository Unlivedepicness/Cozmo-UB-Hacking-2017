import speech_recognition as sr
import cozmo
import re

r = sr.Recognizer()
intents = []


def load_intents():
    global intents

    r_utterance = re.compile('^(\w+) (.*)$')

    with open('utterances.txt') as file:
        utterances = file.read().split('\n')
        for utterance in utterances:
            match = r_utterance.match(utterance)
            intents.append({
                'intent': match.group(1),
                'text': match.group(2)
            })

    print('Loaded', intents)


def loose_match(words, expression, threshold=0.6):
    words = words.split(' ')
    expression = expression.split(' ')

    matched_words = 0
    for target in expression:
        if target in words:
            matched_words += 1

    return matched_words / len(expression) > threshold


def wait_for_any(valid_words):
    while True:
        print('Picking up text ...')
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=1, phrase_time_limit=3)

        print('Parsing text ...')
        try:
            text = str(r.recognize_google(audio)).lower()
            print('>', text)

            words = text.split(' ')

            for word in words:
                if word in valid_words:
                    return

        except sr.UnknownValueError:
            print('Cannot understand')
        except sr.RequestError as e:
            print('Service down', e)


def wait_for_speech(robot: cozmo.robot.Robot):
    found_command = False

    while not found_command:
        print('Recognizing ...')
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=1, phrase_time_limit=7)
        print('Done')

        try:
            text = str(r.recognize_google(audio)).lower()
            print('>', text)
            return text

        except sr.UnknownValueError:
            print('Cannot understand')
            robot.say_text('Speak clearly, you dummy!')
        except sr.RequestError as e:
            print('Service down', e)


def process_intent(text):
    thresholds = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]

    for threshold in thresholds:
        print('Trying with threshold', threshold)
        for intent in intents:
            if loose_match(words=text, expression=intent['text'], threshold=threshold):
                return intent['intent']
    return None
