import cozmo
import cozmo_speech_recognition as csr
from weather import *


weather = Weather()


def intent_get_weather(robot: cozmo.robot.Robot):
    global weather

    # get location
    robot.say_text('Where?').wait_for_completed()

    loc = csr.wait_for_speech(robot)

    location = weather.lookup_by_location(loc)

    if location is not None:
        condition = location.condition()
    else:
        robot.say_text('That is not a place on Earth').wait_for_completed()
        return

    robot.say_text("currently in " + loc + condition['text']).wait_for_completed()

    forecasts = location.forecast()

    robot.say_text("today in " + loc + " the weather is").wait_for_completed()
    robot.say_text(forecasts[0].text()).wait_for_completed()
    robot.say_text("with a high of " + forecasts[0].high()).wait_for_completed()
    robot.say_text("and a low of " + forecasts[0].low()).wait_for_completed()

    robot.say_text("tomorrow the weather is").wait_for_completed()
    robot.say_text(forecasts[1].text()).wait_for_completed()
    robot.say_text("with a high of " + forecasts[1].high()).wait_for_completed()
    robot.say_text("and a low of " + forecasts[1].low()).wait_for_completed()
