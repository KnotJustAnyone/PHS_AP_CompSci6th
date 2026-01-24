def bubbleSort(list):
    pass
class Timer:
    def __init__(self, time: int):
        self.list = []
        for i in range(time):
            self.list+=[time-i]
print(Timer(10).list)