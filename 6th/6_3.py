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
        #temporary var's to store the original values
        temph = self.hours
        tempm = self.minutes
        temps = self.seconds

        #if the (seconds + 1) exceeds 59 it means we need to increase a minutes and start the seconds back from 0
        #and then (minutes + 1) will be checked that if it exceeds then minuetes will be set to 0 because it'll start up back from the new mintue, hence 0.
        # the (hours + 1) will be checked, and if it greater then 12 then the whole clock needs to be restarted to 0:0:0. hence all are set to 0
        # and if the (seconds + 1) does not exceed 59 then seconds will be increased by 1, and same for minutes and hours as well.
        #  
        if(temps + 1 > 59):#57 -> 58 -> 59 -> X
            self.seconds = 0
            if(tempm + 1> 59):
                self.minutes = 0
                if(temph + 1> 12):
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