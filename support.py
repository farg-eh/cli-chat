import time
import socket

# classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Timer:
    def __init__(self, duration, repeat=False, autostart=False, func=None):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.repeat = repeat
        self.func = func

        if autostart:
            self.activate()

    def __bool__(self):
        return self.active

    def activate(self):
        self.active = True
        self.start_time = time.time()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()

    def get_progress(self) -> float:
        """returns a value between 0 and 1 that shows the timers progress
        1 means duration finshed"""
        curr = time.time()
        return (curr - self.start_time)/ self.duration if self.active else 0

    def update(self):
        if self.active:
            if time.time() - self.start_time >= self.duration:
                if self.func and self.start_time != 0:
                    self.func()
                self.deactivate()



# functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def text(string, color):
    """color : 1 red, 2 blue, 3 yellow, 4 blue, 5 purple, 6 blue, 7 gray"""
    return (f"\033[{90 + color}m{string}\033[0m")


def get_my_ip():
    local_ip = None  # variable to store the result
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # a socket object
    try:
        # server doesn't have to be reachable
        s.connect(("10.0.0.1", 80))  #"10.0.0.1" is often used as a default gateway for routers
        local_ip = s.getsockname()[0]

    except Exception as e:
        print("Error: ", e)

    finally:
        s.close()
        return local_ip
