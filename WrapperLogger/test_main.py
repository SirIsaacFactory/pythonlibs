################################################################################
# This software is released under the MIT License see LICENSE.txt
# Filename : test_main.py
# Overview : test script for WrapperLogger
# HowToUse : python test_main.py
#-------------------------------------------------------------------------------
# Author: Isaac Factory (sir.isaac.factory@icloud.com)
# Date: 2021/02/07
# Code version: v1.00
################################################################################
import os
import sys

from logging import DEBUG
from logging import INFO
from logging import WARNING
from logging import ERROR
from logging import CRITICAL

import WrapperLogger as wlogger


################################################################################
# Define variables
################################################################################
scriptpath = os.path.abspath(__file__)
scriptdir  = os.path.dirname(scriptpath)
logbase    = __file__ + ".log"
logfile    = os.path.join(scriptdir, logbase)
normal_end = 0
error_end  = 255
loglevel   = DEBUG


################################################################################
# Define displayArgs
################################################################################
def displayArgs(cmdOptions):
    logger = wlogger.DefineLogger(__name__)
    logger.debug("start")

    logger.info("The command-line options are as below:")
    for opt in cmdOptions:
        logger.info(opt)

    logger.info("end")


################################################################################
# Define main
################################################################################
def main():
    logger = wlogger.DefineLogger(__name__, loglevel)
    # logger = wlogger.CreateLogFile(logger, logfile, loglevel)
    # logger = wlogger.OpenLogFile(logger, logfile, loglevel)

    logger.debug("start")

    optCount = len(sys.argv) - 1
    if optCount == 0:
        logger.error("There are no command-line options.")
        return error_end
    else:
        logger.info("The number of command-line options is {0}.".format(optCount))

    cmdOptions = sys.argv[1:]
    displayArgs(cmdOptions)

    logger.debug("end")
    return normal_end

################################################################################
# Execute main
################################################################################
if __name__ == '__main__':
    ret = main()
    sys.exit(ret)
