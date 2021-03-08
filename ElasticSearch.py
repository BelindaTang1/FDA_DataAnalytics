from datetime import date , datetime, time
import pandas as pd
import pytz

date_format = "%Y/%m/%d"

a =  pd.DataFrame({"a" : [1,2,3], "b": [2,3,4], "c": [3,4,5]})
print(a["b"][0])
d0 = datetime.strptime("2020/2/21", date_format)
d1 = datetime.strptime("2021/2/21", date_format)
delta = d1 - d0
print(delta.days)

class sayHello(object):
    def __init__(self, word):
        self.word = word
    
    def speak(self):
        print(self.word)

if __name__ == "__main__":
    object1 = sayHello("joey")
    object1.speak()
    today = date.today()
    print(today)
    now = time.max
    print(datetime.now())
    EST = pytz.timezone('America/New_York')
    ny_time = datetime.now(EST)
    print(ny_time)