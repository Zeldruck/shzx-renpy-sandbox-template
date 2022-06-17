init python:
    class Daytime(object):

        dayTimeNames = ["Morning", "Noon", "Afternoon", "Evening", "Night"]

        """docstring for Daytime"""
        def __init__(self):
            super(Daytime, self).__init__()
            
            self.totalDays = 0
            self.daytime = 0

            #if date == None:
            #    self.date = Date(1, 1, 0)
            #else:
            #    self.date = date

        def PassTime(self):
            self.daytime += 1

            if self.daytime >= len(Daytime.dayTimeNames):
                self.daytime = 0
                self.totalDays += 1

        def JumpTime(self, jumpTo):
            self.daytime = jumpTo

            if self.daytime >= len(Daytime.dayTimeNames):
                self.daytime = 0
                self.totalDays += 1

        def GetDaytimeName(self):
            return Daytime.dayTimeNames[self.daytime]


    class Date:
        def __init__(self, day, month, year):
            self.seed = random.randint(0, 1)

            self.day = day
            self.month = month
            self.year = year

        def TrueDateValue(self):
            monthDiff = self.month - 12
            if monthDiff > 0:
                rest = monthDiff / 12 - int(monthDiff / 12)

                self.year += int(monthDiff / 12) + 1
                self.month = int(rest * 12)


            if month == 2:
                dayDiff = self.day - 28

                if dayDiff > 0:
                    rest = dayDiff / 28
            #else:

                
        def AddDate(self, day, month):
            self.day += day
            self.month += month

            self.TrueDateValue()


        def GetDate(self):
            if self.day < 10:
                day = "0" + self.day

            if self.month < 10:
                month = "0" + self.month

            return str(day + "/" + month + "/" + self.year)
            