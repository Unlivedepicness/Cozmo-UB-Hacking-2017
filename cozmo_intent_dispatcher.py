from cozmo import logger

intent_callbacks = {}


def register_intent(intent_name, callback):
    logger.info('Intent registered: %s -> %s' % (intent_name, callback.__name__))
    intent_callbacks[intent_name] = callback


def dispatch(intent, robot):
    logger.info('Dispatching intent: %s' % intent)
    intent_callbacks[intent](robot)
