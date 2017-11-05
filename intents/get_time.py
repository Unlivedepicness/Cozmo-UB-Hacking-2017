import cozmo
import re
import humanize

from datetime import datetime


ask_count = 0


def intent_get_time(robot: cozmo.robot.Robot):
    global ask_count

    ask_count += 1

    if ask_count % 3 == 0:
        robot.say_text('Time to get a watch dummy').wait_for_completed()
        return

    m = re.search('(\d*):(\d*)', str(datetime.now()))

    hours = int(m.group(1))
    mins = int(m.group(2))

    robot.say_text('It is %s' % humanize.humanize_time(hours, mins)).wait_for_completed()
