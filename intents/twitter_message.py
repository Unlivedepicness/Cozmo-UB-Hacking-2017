import cozmo
import asyncio
import time
import twitter

import cozmo_speech_recognition as csr

from cozmo import logger

api = twitter.Api(consumer_key='SDTOWyiHRbUKAO0rBXKo8a9ZQ',
                  consumer_secret='dKuoPH0nRwXNRQcdlRteAJl4k8tWTmEdbdkg9FtARNpL6MnvJq',
                  access_token_key='926935306124910592-6Enz2UQ97BiVDD7F7skfrrtGgX6aWL3',
                  access_token_secret='khfC8uEZBPy2LYzQg82xZ2wd8dzxNUPFFKI40Jw8j5D97')


def intent_twitter_message(robot: cozmo.robot.Robot):
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    robot.say_text('Stand in front of me').wait_for_completed()

    try:
        robot.world.wait_for_observed_face(timeout=5)

        logger.info('Face found')

        robot.say_text('three').wait_for_completed()
        time.sleep(0.1)
        robot.say_text('two').wait_for_completed()
        time.sleep(0.1)
        robot.say_text('one').wait_for_completed()
        time.sleep(0.1)
        robot.say_text('Say cheese!').wait_for_completed()

        logger.info('Taking picture ...')

        latest_image = robot.world.latest_image
        latest_image.raw_image.convert('L').save('picture.png')

        robot.say_text('What should I put in the tweet?').wait_for_completed()
        speech = csr.wait_for_speech(robot)

        robot.say_text('I will tweet ' + speech).wait_for_completed()

        tweet = '@UBHacking ' + speech

        logger.info('Tweeting: %s' % tweet)

        api.PostMedia(tweet, 'picture.png')

    except asyncio.TimeoutError:
        robot.say_text('I can\'t find you')
