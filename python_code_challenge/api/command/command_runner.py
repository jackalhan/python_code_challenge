import os
import subprocess as sub
import threading

class RunCmd(threading.Thread):
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        self.p = sub.Popen(self.cmd, stdout=sub.PIPE, shell=True, preexec_fn=os.setsid)
        self.p.wait()

    def execute(self):
        self.start()
        self.join(self.timeout)
        isTerminated = False
        if self.is_alive():
            self.p.terminate()      #use self.p.kill() if process needs a kill -9
            self.join()
            isTerminated = True

        return self.p.communicate()[0], isTerminated
