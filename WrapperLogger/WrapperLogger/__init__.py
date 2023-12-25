################################################################################
# This software is released under the MIT License. See LICENSE.txt
# Package name : WrapperLogger
# Overview : Dispay log/Write log to file.
# HowToUse : Import
#              when Wrapper is located in the current folder
#              import WrapperLogger as wlogger
#            Initialize
#              logger = wlogger.DefineLogger(__name__, loglevel)
#            if you need a log file:
#                clear log file before write
#                  logger = logger = wlogger.CreateLogFile(logger, logfile, loglevel)
#                not clear log file before write
#                  logger = logger = wlogger.OpenLogFile(logger, logfile, loglevel)
#            Log output
#              logger.debug("debug level message")
#              logger.info("info level message")
#              logger.warning("warning level message")
#              logger.error("error level message")
#              logger.critical("critical level message")
#-------------------------------------------------------------------------------
# Author: pythonyaki (154766771+pythonyaki@users.noreply.github.com)
# Repository: https://github.com/pythonyaki/SirIsaacFactory-pythonlibs-fork
# Date: 2023/12/24
# Code version: v1.00
################################################################################
import os
import inspect

from logging import DEBUG
from logging import INFO
from logging import WARNING
from logging import ERROR
from logging import CRITICAL
from logging import getLogger
from logging import StreamHandler
from logging import FileHandler
from logging import Formatter


################################################################################
# Define variables
################################################################################
loggers = {}
_DEFAULT_LEVEL = ERROR


################################################################################
# DefineLogger
################################################################################
def DefineLogger(name=None, loglevel=_DEFAULT_LEVEL):
    global loggers
    if name == None:
        name = __name__

    if loggers.get(name):
        return loggers.get(name)

    streamhandler   = StreamHandler()
    formatter = Formatter(
        "%(asctime)s, "
        "%(levelname)s, "
        "{0}, "
        "%(filename)s, "
        "%(funcName)s, "
        "%(lineno)s, "
        "%(message)s".format(name)
    )

    streamhandler.setFormatter(formatter)
    logger = getLogger(name)
    logger.setLevel(loglevel)
    logger.addHandler(streamhandler)

    loggers[name] = logger
    return logger


################################################################################
# Create logfile
################################################################################
def CreateLogFile(logger, logpath, loglevel=_DEFAULT_LEVEL):

    # Check if log directory exists
    logdir = os.path.dirname(logpath)
    if not os.path.isdir(logdir):
        raise Exception("log directory({0}) doesn't exist.".format(logdir))

    name = logger.name

    # Configure file handler
    formatter = Formatter(
        "%(asctime)s, "
        "%(levelname)s, "
        "{0}, "
        "%(filename)s, "
        "%(funcName)s, "
        "%(lineno)s, "
        "%(message)s".format(name)
    )
    filehandler = FileHandler(logpath, mode="w")
    filehandler.setLevel(loglevel)
    filehandler.formatter = formatter
    logger.addHandler(filehandler)

    loggers[name] = logger
    return logger

################################################################################
# Open logfile
################################################################################
def OpenLogFile(logger, logpath, loglevel=_DEFAULT_LEVEL):

    # Check if log directory exists
    logdir = os.path.dirname(logpath)
    if not os.path.isdir(logdir):
        raise Exception("log directory({0}) doesn't exist.".format(logdir))

    name = logger.name

    # Configure file handler
    formatter = Formatter(
        "%(asctime)s, "
        "%(levelname)s, "
        "{0}, "
        "%(filename)s, "
        "%(funcName)s, "
        "%(lineno)s, "
        "%(message)s".format(name)
    )
    filehandler = FileHandler(logpath, mode="a")
    filehandler.setLevel(loglevel)
    filehandler.formatter = formatter
    logger.addHandler(filehandler)

    loggers[name] = logger
    return logger
