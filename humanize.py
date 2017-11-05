def humanize_number(num):
    """
    Convert a given number to text
    :param num: Number to convert
    :return: Number as a string of words
    """

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
        # Take care of single digits and teens
        return nums[num]
    elif num % 10 == 0:
        # Take care of exact multiples of ten
        return nums[num]

    tens = (num // 10) * 10
    ones = num % 10

    return nums[tens] + ' ' + nums[ones]


def humanize_time(hours, mins):
    """
    Convert a given time to a string of text
    :param hours: Hour
    :param mins: Minute
    :return: A string of text representing the given time
    """

    am = True

    # No military time
    if hours >= 12:
        am = False
        hours -= 12

    # Special cases for midnight and noon
    if hours == 0:
        if am:
            return "Midnight"
        else:
            return "Noon"

    hours = humanize_number(hours)

    if mins < 10:
        # Take care of single digits, to produce strings such as "oh four" (04)
        mins = humanize_number(0) + ' ' + humanize_number(mins)
    else:
        mins = humanize_number(mins)

    if am:
        ampm = "A M"
    else:
        ampm = "P M"

    return hours + ' ' + mins + ' ' + ampm