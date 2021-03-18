from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.displayText = "0"
        self.value1 = DoubleVar
        self.value1 = "None"
        self.value2 = DoubleVar
        self.value2 = "None"
        self.operator = StringVar
        self.result = DoubleVar
        self.answer = BooleanVar
        self.answer = False

        self.display = Label(self, text="0", font=("Courier", 44))
        self.display.grid(column=0, row=0, columnspan=4, sticky=E)




        self.add = Button(self, text="+", font=("Courier", 44), command=self.add)
        self.add.grid(column=3, row=4, sticky=E)

        self.sub = Button(self,text = "-", font=("Courier", 44), command = self.subtract)
        self.sub.grid(column=3, row=3, sticky=E)

        self.mult = Button(self, text="*", font=("Courier", 44), command= self.multiply)
        self.mult.grid(column=3, row=2, sticky=E)

        self.div = Button(self, text="/", font=("Courier", 44),  command= self.divide)
        self.div.grid(column=3, row=1, sticky=E)

        self.one = Button(self, text="1", font=("Courier", 44), command=self.numberOne)
        self.one.grid(column=0, row=3, sticky=E)

        self.two = Button(self, text="2", font=("Courier", 44), command=self.numberTwo)
        self.two.grid(column=1, row=3, sticky=E)

        self.three = Button(self, text="3", font=("Courier", 44), command=self.numberThree)
        self.three.grid(column=2, row=3, sticky=E)

        self.four = Button(self, text="4", font=("Courier", 44), command=self.numberFour)
        self.four.grid(column=0, row=2, sticky=E)

        self.five = Button(self, text="5", font=("Courier", 44), command=self.numberFive)
        self.five.grid(column=1, row=2, sticky=E)

        self.six = Button(self, text="6", font=("Courier", 44), command=self.numberSix)
        self.six.grid(column=2, row=2, sticky=E)

        self.seven = Button(self, text="7", font=("Courier", 44), command=self.numberSeven)
        self.seven.grid(column=0, row=1, sticky=E)

        self.eight = Button(self, text="8", font=("Courier", 44), command=self.numberEight)
        self.eight.grid(column=1, row=1, sticky=E)

        self.nine = Button(self, text="9", font=("Courier", 44), command=self.numberNine)
        self.nine.grid(column=2, row=1, sticky=E)

        self.zero = Button(self, text="0", font=("Courier", 44), command=self.numberZero)
        self.zero.grid(column=1, row=4, sticky=E)

        self.clear = Button(self, text="C", font=("Courier", 44), command=self.clear)
        self.clear.grid(column=0, row=4, sticky=E)

        self.equal = Button(self, text="=", font=("Courier", 44), command=self.equals)
        self.equal.grid(column=2, row=4, sticky=E)





    # NUMBER commands

    def numberOne(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "1"
        else:
            self.display["text"] += "1"

    def numberTwo(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "2"
        else:
            self.display["text"] += "2"

    def numberThree(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "3"
        else:
            self.display["text"] += "3"

    def numberFour(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "4"
        else:
            self.display["text"] += "4"

    def numberFive(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "5"
        else:
            self.display["text"] += "5"

    def numberSix(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "6"
        else:
            self.display["text"] += "6"

    def numberSeven(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "7"
        else:
            self.display["text"] += "7"

    def numberEight(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "8"
        else:
            self.display["text"] += "8"

    def numberNine(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "9"
        else:
            self.display["text"] += "9"

    def numberZero(self):
        if self.answer == True:
            self.display["text"] = "0"
        if self.display["text"] == "0":
            self.display["text"] = "0"
        else:
            self.display["text"] += "0"

    # Operator Commands
    def add(self):
        self.operator = '+'
        if self.value1 == "None" or self.answer == True:
            self.value1 = getdouble(self.display["text"])
            self.resetScreen()
        else:
            self.value2 = getdouble(self.display["text"])
            self.result = self.value1 + self.value2
            self.display["text"] = self.result
            self.update()
            self.answer = True

    def subtract(self):
        self.operator = '-'
        if self.value1 == "None" or self.answer == True:
            self.value1 = getdouble(self.display["text"])
            self.resetScreen()
        else:
            self.value2 = getdouble(self.display["text"])
            self.result = self.value1 - self.value2
            self.display["text"] = self.result
            self.update()
            self.answer = True

    def multiply(self):
        self.operator = '*'
        if self.value1 == "None" or self.answer == True:
            self.value1 = getdouble(self.display["text"])
            self.resetScreen()
        else:
            self.value2 = getdouble(self.display["text"])
            self.result = self.value1 * self.value2
            self.display["text"] = self.result
            self.update()
            self.answer = True

    def divide(self):
        self.operator = '/'
        if self.value1 == None:
            self.value1 = getdouble(self.display["Text"])
        else:
            if self.value1 == "None" or self.answer == True:
                self.value1 = getdouble(self.display["text"])
                self.resetScreen()
            else:
                self.value2 = getdouble(self.display["text"])
                self.result = self.value1 / self.value2
                self.display["text"] = self.result
                self.update()
                self.answer = True

    def equals(self):
        if self.value1 == "None":
            self.value1 = getdouble(self.display["text"])
        else:
            self.value2 = getdouble(self.display["text"])
            print("value 2 set")
            print(self.value2)
            print(self.operator)
            if self.operator == "+":
                self.result = self.value1 + self.value2
            elif self.operator == "-":
                self.result = self.value1 - self.value2
            elif self.operator == "*":
                self.result = self.value1 * self.value2
            elif self.operator == "/":
                self.result = self.value1 / self.value2
            self.operator = "None"
            self.value1 = self.result
            self.update()
            self.answer = True

    def resetScreen(self):
        self.display["text"] = "0"

    def clear(self):
        self.resetScreen()
        self.value1 = "None"
        self.value2 = "None"
        self.operator = "None"


    def update(self):
        self.display["text"] = self.result
        self.result = self.value1



def main():
    root = Tk()
    root.title("Calculator")
    root.geometry("350x500")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()

main()


