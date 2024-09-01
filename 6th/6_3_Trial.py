class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def setClock(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def displayClock(self):
        print(self.hours, ":", self.minutes, ":", self.seconds)

    def tick(self):
        
        temps = self.seconds
        tempm = self.minutes
        temph = self.hours

        if(temps + 1 > 59):
            self.seconds = 0
            if(tempm + 1 > 59):
                self.minutes = 0
                if(temph + 1 > 12):
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

c1 = Clock(10,2,57)
c1.displayClock()



c1.tick()
c1.tick()
c1.tick()
c1.displayClock()
