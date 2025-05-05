from math import trunc

tape = "ABBACA" #A, B, C

currentState = "1" #1, 2, 3
currentPoint = "0"

def change(a, b):
    if a+b < 0: return 0;
    return a+b

class TuringMachine:
    def __init__(self):
        self.state = "1" #0, 1, 2
        self.point = 0
        self.tape = "ABC" #A, B, C

    def runA(self):
        print("A runned")
        if self.state == "0":
            return "stop"
        elif self.state == "1":
            self.point = change(self.point, 1)
        elif self.state == "2":
            return "stop"
        return "go"

    def runB(self):
        print("B runned")
        if self.state == "0":
            return "stop"
        elif self.state == "1":
            self.point = change(self.point, 1)
            self.state = "2"
        elif self.state == "2":
            return "stop"
        return "go"

    def runC(self):
        print("C runned")
        if self.state == "0":
            return "stop"
        elif self.state == "1":
            self.point = change(self.point, 1)
        elif self.state == "2":
            print("s")
            return "stop"
        return "go"

    def run(self):
        print(self.tape[0])
        while True:
            print(self.point)
            if self.tape[self.point] == "A":
                if self.runA() == "stop":
                    break
            elif self.tape[self.point] == "B":
                if self.runB() == "stop":
                    break
            elif self.tape[self.point] == "C":
                if self.runC() == "stop":
                    break

tr = TuringMachine()
tr.run()

