import logging


def get_logger(name):
    """Create formated logger with name of file yang.log
        Arguments:
            :param name :  (str) Set name of the logger.
            :return a logger with the specified name.
    """
    FORMAT = '%(asctime)-15s %(levelname)-8s %(name)5s => %(message)s - %(lineno)d'
    DATEFMT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(datefmt=DATEFMT, format=FORMAT, filename='yang.log', level=logging.INFO)
    return logging.getLogger(name)
