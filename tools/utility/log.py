import logging


def get_logger(name, file_name_path='yang.log'):
    """Create formated logger with name of file yang.log
        Arguments:
            :param file_name_path: filename and path where to save logs.
            :param name :  (str) Set name of the logger.
            :return a logger with the specified name.
    """
    FORMAT = '%(asctime)-15s %(levelname)-8s %(name)5s => %(message)s - %(lineno)d'
    DATEFMT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(datefmt=DATEFMT, format=FORMAT, filename=file_name_path, level=logging.INFO)
    return logging.getLogger(name)
