import counter as ctr
import button as btn
upCounter = ctr.Counter(0)
upButton = btn.Button(upCounter,17)
downCounter = ctr.Counter(0)
downButton = btn.Button(downCounter,17)
def play():
    print("^\nv")
    while True:
        direction=input()
        if direction == "^":
            upButton.on_pressed()
        elif direction == "v":
            downButton.on_pressed()
        else:
            print("Not a valid direction")
play()
