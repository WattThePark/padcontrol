# coding=utf-8

import rtmidi
import time
from threading import Thread


class Pad(Thread):
    """docstring for Pad"""

    def __init__(self):
        Thread.__init__(self)
        self.source = rtmidi.MidiIn()
        self.score = 0.0

    def run(self):
        """
        Run the mainloop. Aquire and save the data from the controller.
        """
        if self.source.get_port_count() > 0:
            # Connect to the good midi port
            for i in xrange(source.get_port_count()):
                if re.match("nano", source.get_port_name(i)):
                    self.source.open_port(i)
                else:
                    return

            self.loop = True
            compteur , acc , score = 0.0, 0.0 , 0.0

            toWatt = 7
            while(self.loop):
                time.sleep(0.01)
                data = self.source.get_message()
                compteur += 0.01
                if data:
                    acc += 1
                if compteur > 0.4:
                    self.score = self.score + acc - self.score

                    self.score = self.score * toWatt
                    acc , compteur = 0.0 , 0.0
        else:
            return

    def stop(self):
        """
        Stop the main loop
        """
        self.loop = False
