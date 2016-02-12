
from g1.arithmeticgenome import ArithmeticGenome
from g1.population import Population, PopulationAndSelectionConfig
from g1.multithreading import PrintThread, Task, TaskRunner, createAndStartPrintAndTaskQueues, goGentleIntoThatGoodNight

import random
import logging
# import cProfile, pstats
import datetime, time

##### 1) Map the concept space of possible developments !!! Expansion in abilities vs speed, multi server deployments?

##### Target interesting behaviours - synergistic relationships where both pop entities benefit?

##### 2) Ability to evolve 'masks' that control variability of the chromosome, such that the mask learns which parts of
##### the chromosome benefit from slower or more rapid change.as

##### 3) Include relative symbol frequency as evolveable parameters


### Setup
random.seed()

logFormat = '%(asctime)-15s %(message)s'
logging.basicConfig(format=logFormat)
systemLog = logging.getLogger(__name__)
systemLog.setLevel(logging.WARNING)

st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
dataLogFileName = 'data/Log0.333.' + st + ".tsv"

# Creates queues which facilitate multi-threaded execution of populations simultaneously, and safe multi-threaded logging
taskQueue, printQueue = createAndStartPrintAndTaskQueues(dataLogFileName, systemLog, threads=4)

# def problemTimesTwo(i):
#     return i * 2
#
# timesTwoTestSet = [2,16,99,1045,0.1]

def problem(dummmy):
    return 0.333

populationSize=60
iterations = 500

for dnaLength in range(10,51,5):
    for k in range(0,100):
        populationConfig = PopulationAndSelectionConfig(populationSize,0.0001, 0.33, 2, 0.16, 0.32, 0, 0.33, 1, 1, 1, 1, 0, 1, 0.25, 0.25, 0.4, 0.5, 1)
        genomeConfig = {"length" : dnaLength}
        t = Task(problem, ArithmeticGenome, genomeConfig, populationConfig, iterations)
        taskQueue.put(t)


# Wait for everything to finish, and close peacefully. Without this end of execution of the main threads will kill off all other threads that are probably still running
goGentleIntoThatGoodNight(taskQueue, printQueue)