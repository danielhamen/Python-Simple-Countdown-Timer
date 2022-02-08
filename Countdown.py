class TimeConversion:
    def __init__(self, SourceValue, SourceUnit, EndUnit):
        """
        Source/End Units:
            "Hr" : "Hour",
            "Min" : "Minute",
            "Sec" : "Second"
        """

        self.SourceValue = float(SourceValue)
        self.SourceUnit = str(SourceUnit).lower()
        self.EndUnit = str(EndUnit).lower()
        self.EndValue = 0.0

    def Convert(self):
        Conversions = {
            "hr" : {
                "min" : "*60",
                "sec" : "*3600",
            },

            "min" : {
                "hr" : "/60",
                "sec" : "*60",
            },

            "sec" : {
                "hr" : "/3600",
                "min" : "/60"
            }
        }

        Base = Conversions.get(str(self.SourceUnit))
        Eq = Base.get(str(self.EndUnit))

        Equation = str(self.SourceValue) + Eq
        ANS = eval(Equation)

        self.EndValue = ANS

def PlaySound(Loops,Sound=r"AlarmFinished.mp3"):
    from playsound import playsound

    i = 0

    while i < Loops:
        playsound(Sound)
        i += 1


def Countdown(Time, TimeUnit="MIN", Intervals=1, OnFinish="PlaySound(4)", LineEnd="\r"):
    import time

    AcceptableUnits = ["hr", "min", "sec"]

    TimeUnit = str(TimeUnit).lower()
    
    if TimeUnit not in AcceptableUnits:
        raise ValueError(f"TimeUnit: \"{TimeUnit}\" is not known. Known units are: \"HR\", \"MIN\", \"SEC\"")
    
    if str(TimeUnit) != "sec":
        Convert = TimeConversion(Time, str(TimeUnit), "SEC")
        Convert.Convert()

        Time = Convert.EndValue
    
    Finished = False
    
    while Finished is False:
        Time_ = time.strftime('%H:%M:%S', time.gmtime(Time))
        print(Time_, end=LineEnd)
        if str(Time_) == "00:00:00":
            Finished = True
        else:
            Time -= 1
        time.sleep(float(Intervals))
    
    exec(OnFinish)
    Exit = input("Your timer is Done! Type\n\n\"0\" To snooze\n\"1\" To exit\n\n>>> ")

    if str(Exit) == "1":
        exit()
    
    elif str(Exit) == "0":
        Countdown(9, "MIN")

    else:
        raise ValueError
