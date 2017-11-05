from cozmo import logger


# Callback for intents
intent_callbacks = {}


def register_intent(intent_name, callback):
    """
    Register an intent callback
    :param intent_name: Intent name (must be configured in `utterances.txt`)
    :param callback: Function that takes in a Cozmo robot object
    :return: None
    """
    logger.info('Intent registered: %s -> %s' % (intent_name, callback.__name__))
    intent_callbacks[intent_name] = callback


def dispatch(intent, robot):
    """
    Dispatch an intent
    :param intent: Intent name
    :param robot: Cozmo robot
    :return:
    """
    logger.info('Dispatching intent: %s' % intent)
    intent_callbacks[intent](robot)
