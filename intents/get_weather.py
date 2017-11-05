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
    # print("currently " + condition['text'])

    forecasts = location.forecast()

    robot.say_text("today in " + loc + " the weather is").wait_for_completed()
    # print("today in " + loc + " the weather is")
    robot.say_text(forecasts[0].text()).wait_for_completed()
    # print(forecasts[0].text())
    robot.say_text("with a high of " + forecasts[0].high()).wait_for_completed()
    # print("with a high of " + forecasts[0].high())
    robot.say_text("and a low of " + forecasts[0].low()).wait_for_completed()
    # print("and a low of " + forecasts[0].low())


    robot.say_text("tomorrow the weather is").wait_for_completed()
    # print("tomorrow the weather is")
    robot.say_text(forecasts[1].text()).wait_for_completed()
    # print(forecasts[1].text())
    robot.say_text("with a high of " + forecasts[1].high()).wait_for_completed()
    # print("with a high of " + forecasts[1].high())
    robot.say_text("and a low of " + forecasts[1].low()).wait_for_completed()
    # print("and a low of " + forecasts[1].low())

    return
