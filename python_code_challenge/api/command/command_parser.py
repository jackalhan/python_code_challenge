"""
Handles the work of validating and processing command input.
"""
import mmap
import os
import subprocess

import time

from python_code_challenge.api.command.business import create_command
from python_code_challenge.database.models import Command

app = None


def get_valid_commands(queue, filename):
    # TODO: efficiently evaluate commands
    validCommandList = []  # List prevents insertion order
    allCommandList = []
    isAllCommandLine = None
    with open(filename) as infile:
        map = mmap.mmap(infile.fileno(), 0, prot=mmap.PROT_READ)
        for line in iter(map.readline, ""):
            if line.strip() == '[COMMAND LIST]':
                isAllCommandLine = True
            elif line.strip() == '[VALID COMMANDS]':
                isAllCommandLine = False
            else:
                if line.strip() != '' :
                    if isAllCommandLine == True :
                        allCommandList.append(line.rstrip())
                    else:
                        validCommandList.append(line.rstrip())
    infile.close()

    allCommandList = removeDuplicatesInList(allCommandList)
    #queue = [x for x in allCommandList if x in validCommandList]
    for x in allCommandList :
        if x in validCommandList :
            queue.put(x)




def process_command_output(queue, fileName):
    # TODO: run the command and put its data in the db

    command_string = queue.get()
    length = len(command_string)
    duration = None
    output = None

    start = time.time()
    time.clock()
    cmd = subprocess.Popen(command_string, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid).communicate()[0]
    duration = time.time() - start
    print cmd

    # for line in cmd.stdout:
    #     output += str(line)

    command = Command(fileName, command_string, length, duration, output)
    create_command(command)

def uniqify(seq, idfun=None):
    seen = set()
    if idfun is None:
        for x in seq:
            if x in seen:
                continue
            seen.add(x)
            yield x
    else:
        for x in seq:
            x = idfun(x)
            if x in seen:
                continue
            seen.add(x)
            yield x


def removeDuplicatesInList(seq):
    # Order preserving
    return list(uniqify(seq))
