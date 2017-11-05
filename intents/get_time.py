import cozmo
import re

from datetime import datetime


def _convert_num(num):
    nums = {
        0: 'oh',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty'
    }

    if num < 20:
        return nums[num]
    elif num % 10 == 0:
        return nums[num]

    tens = (num // 10) * 10
    ones = num % 10

    return nums[tens] + ' ' + nums[ones]


def _humanize(hours, mins):
    am = True

    if hours >= 12:
        am = False
        hours -= 12

    if hours == 0:
        if am:
            return "Midnight"
        else:
            return "Noon"

    hours = _convert_num(hours)

    if mins < 10:
        mins = _convert_num(0) + ' ' + _convert_num(mins)
    else:
        mins = _convert_num(mins)

    if am:
        ampm = "A M"
    else:
        ampm = "P M"

    return hours + ' ' + mins + ' ' + ampm


def intent_get_time(robot: cozmo.robot.Robot):
    m = re.search('(\d*):(\d*)', str(datetime.now()))
    hours = int(m.group(1))
    mins = int(m.group(2))

    robot.say_text('It is %s' % _humanize(hours, mins)).wait_for_completed()
