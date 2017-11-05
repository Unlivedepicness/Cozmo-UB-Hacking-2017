import cozmo


def create_response_intent(response):
    """
    Create an intent that simply speaks a predefined sentence
    :param response: Response to say when called
    :return: An intent that speaks the specified response
    """

    def intent_response(robot: cozmo.robot.Robot):
        robot.say_text(response).wait_for_completed()

    return intent_response
