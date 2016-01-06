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
        print self.source.get_port_count()
        if self.source.get_port_count() > 0:
            print "inside"
            self.loop = True
            self.source.open_port(1)
            compteur = 0.0
            acc = 0.0
            score = 0
            while(self.loop):
                time.sleep(0.01)
                data = self.source.get_message()
                compteur += 0.01
                if data:
                    acc += 1
                if compteur > 0.4:
                    self.score = self.score + acc - self.score
                    # Transformation en Watt
                    self.score = self.score * 7
                    acc = 0.0
                    compteur = 0.0
                    # print score

        else:
            return

    def stop(self):
        self.loop = False
