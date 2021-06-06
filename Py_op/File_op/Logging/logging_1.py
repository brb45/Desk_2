import logging
"""
# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")
"""
"""
logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except Exception:
    log.exception("Error!")
"""
import logging
# from log_parse import otherMod2
import os

# logging levels
# DEBUG < INFO < WARNING < ERROR < CRITICAL
# ----------------------------------------------------------------------
def main():
    #logger setup
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.DEBUG)

    # create the logging file handler
    fh = logging.FileHandler("logging_1_1.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    # running logger
    ## write to file
    logger.error("Program started")
    # result = otherMod2.add(7, 8)
    logger.info("Done!")

    x=10
    y = 100
    logger = logging.getLogger("example")
    # print-out in stdout
    logger.warning("added %s and %s to get %s" % (x, y, x + y))


if __name__ == "__main__":
    main()
    logging.error("This is a test")
# 2019-04-25 18:04:09,623 - exampleApp - INFO - Program started
# 2019-04-25 18:04:09,623 - exampleApp.otherMod2.add - INFO - added 7 and 8 to get 15
# 2019-04-25 18:04:09,623 - exampleApp - INFO - Done!