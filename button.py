import counter as ctr
class Button:
  def __init__(self, counter : ctr.Counter, bank):
    self.counter=counter
    self.bank=bank
    self.state="off"
  def on_pressed(self):
    print("click")
    self.counter.count+=1
    if self.state=="off":
      self.state="on"
x=ctr.Counter(0)
print(x.count)
y=Button(x,0)
y.on_pressed()
print(x.count)