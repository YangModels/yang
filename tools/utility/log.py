import logging


def get_logger(name):
    FORMAT = '%(asctime)-15s %(levelname)-8s %(name)5s => %(message)s - %(lineno)d'
    DATEFMT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(datefmt=DATEFMT, format=FORMAT, filename='yang.log', level=logging.INFO)
    return logging.getLogger(name)
