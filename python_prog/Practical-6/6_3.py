# c) Create a class clock having 3 init parameters – hours, minutes and
#               seconds. Write following methods:
#           a. setClock – to set the time
#           b. displayTime – to show current time
#           c. tick – increase the time by one second

class Clock:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def settime(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def displaytime(self):
        print("Hours:",self.hours,"Minutes:",self.minutes,"Seconds:",self.seconds)
    def tick(self):
        temph = self.hours
        tempm=self.minutes
        temps=self.seconds
        if (temps +1 > 59):
            self.seconds = 0
            if (tempm +1 > 59):
                self.minutes = 0
                if(temph +1 > 12):
                    self.hours =0
                    self.minutes=0
                    self.seconds=0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

c1 = Clock(10,2,59)
c1.displaytime()
c1.tick()
c1.tick()
c1.tick()
c1.displaytime()