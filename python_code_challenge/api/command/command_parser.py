"""
Handles the work of validating and processing command input.
"""
import numpy as np
app = None

def get_valid_commands(queue, filename):
    # TODO: efficiently evaluate commands
    # with open(filename) as infile:
    #     map = mmap.mmap(infile.fileno(), 0, prot=mmap.PROT_READ)
    #     for line in iter(map.readline, ""):
    #         print line
    # infile.close()
    data = np.genfromtxt(filename, delimiter='\n', dtype=None,)
    allCommandItemIndicator = np.argwhere(data == '[COMMAND LIST]')
    validCommandItemIndicator = np.argwhere(data == '[VALID COMMANDS]')
    #condition = np.where((data > allCommandItemIndicator) )
    dataPart1 = data[[allCommandItemIndicator+1,validCommandItemIndicator-1]]
    #validCommandItemIndicator + 1:len(np.atleast_1d(data)
    #np.delete(data, allCommandItemIndicator)



    print dataPart1

   # queue.put(Command)


def process_command_output(queue):
    # TODO: run the command and put its data in the db
    command = queue.get()
