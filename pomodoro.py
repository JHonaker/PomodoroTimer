# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 09:42:59 2014

@author: John Honaker
"""

import os 
import time
import winsound


class Pomodoro:
    
    # States for the Pomodoro
    PAUSED = 0
    WORKING = 1
    BREAK = 2
    FINISHED = 3

    def __init__(self, working_time, break_time):
        self.working_time = working_time
        self.break_time = break_time        

        self.return_state = None        
        
        self.set_state(Pomodoro.WORKING)
        
    def start(self):
        self.state = Pomodoro.WORKING
        
    def toggle_pause(self):
        if self.state == Pomodoro.PAUSED:
            self.state = self.return_state
        else:
            self.return_state = self.state
            self.state = Pomodoro.PAUSED
        
    def tick(self):
        if self.state == Pomodoro.WORKING or self.state == Pomodoro.BREAK:
            if self.seconds == 0:
                if self.minutes == 0:
                    if self.hours == 0:
                        if self.state == Pomodoro.WORKING:
                            self.set_state(Pomodoro.BREAK)
                            winsound.Beep(450, 750)
                        elif self.state == Pomodoro.BREAK:
                            self.state = Pomodoro.FINISHED
                            winsound.Beep(450, 750)
                    else:
                        self.hours -= 1
                        self.minutes = 59
                        self.seconds = 59
                else:
                    self.minutes -= 1
                    self.seconds = 59
            else:
                self.seconds -= 1
                
    def set_state(self, state):
        state_time = None
        if state == Pomodoro.BREAK:
            state_time = self.break_time
        elif state == Pomodoro.WORKING:
            state_time = self.working_time
            
        self.hours = state_time["hours"]
        self.minutes = state_time["minutes"]
        self.seconds = state_time["seconds"]
        
        self.state = state
        
    def display(self):
        print self.state
        if (self.state == Pomodoro.PAUSED):
            print ('Paused')
        elif self.state == Pomodoro.WORKING:
            print "Working Interval"
            print self.hours, "Hours", self.minutes, "Minutes", self.seconds, "Seconds"
        elif self.state == Pomodoro.BREAK:
            print "Break Interval"
            print self.hours, "Hours", self.minutes, "Minutes", self.seconds, "Seconds"
        elif self.state == Pomodoro.FINISHED:
            print "Finished!"
        else: 
            print "Unknown State:", self.state
        
        
def main():
    pom = Pomodoro({"hours" : 0, "minutes": 25, "seconds" : 0},
                   {"hours" : 0, "minutes" : 5,  "seconds" : 0})

    # Haven't implemented pause function yet. Not really needed though.
    # It kind of defeats the purpose.    
    
    while pom.state != Pomodoro.FINISHED:
        os.system('cls')
        pom.display()
        time.sleep(1)
        pom.tick()
    pom.display()

if __name__ == "__main__":
    main()