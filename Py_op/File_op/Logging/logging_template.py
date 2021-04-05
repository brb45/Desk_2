import logging

def basic_logging(msg, format = '%(asctime)s %(name)s - %(levelname)s - %(message)s', level = logging.INFO):
    logging.basicConfig(format=format, level=level)
    return logging.info(msg)

def read_json(json_file):
    basic_logging('Reading begins')
    # data = pandas.read_json(json_file, lines=True)
    basic_logging('Reading ends')
    # return data.notnull()

json_file = "file.txt"

read_json((json_file))
# 2021-04-02 21:47:40,676 root - INFO - Reading begins
# 2021-04-02 21:47:40,677 root - INFO - Reading ends