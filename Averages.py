#Quinton Dean
#This is a simple GUI that computes the average of a class

from tkinter import*
class MyGUI:
    def __init__(self):
        window1 = Tk()
        window1.title("Score Caculations")
 
        frame1 = Frame(window1)
        frame2 = Frame(window1)
        frame1.pack(side = "left")
        frame2.pack(side = "right")
 
        assignLabel = Label(frame1, text = "Assignment")
        examLabel1 = Label(frame1, text = "First Exam")
        examLabel2 = Label(frame1, text = "Second Exam")
        particLabel = Label(frame1, text = "Class Participation")
        labLabel = Label(frame1, text = "Labs & Quizzes")
        examLabel3 = Label(frame1, text = "Final Exam")
 
 
        self.assignment = IntVar()
        self.exam1 = IntVar()
        self.exam2 = IntVar()
        self.participation = IntVar()
        self.lab = IntVar()
        self.exam3 = IntVar()
       
        assignEntry = Entry(frame1, textvariable = self.assignment, width = 5)
        examEntry1 = Entry(frame1, textvariable = self.exam1, width = 5)
        examEntry2 = Entry(frame1, textvariable = self.exam2, width = 5)
        particEntry = Entry(frame1, textvariable = self.participation, width = 5)
        labEntry = Entry(frame1, textvariable = self.lab, width = 5)
        examEntry3 = Entry(frame1, textvariable = self.exam3, width = 5)

        self.result = IntVar()
        displayEntry = Entry(frame2, textvariable = self.result)
       
 
        self.v1 = IntVar() 
        rbScore1 = Radiobutton(frame2, text = "Show Score 1", variable = self.v1, value = 1, command = self.checkButtonPress)
        rbScore2 = Radiobutton(frame2, text = "Show Score 2", variable = self.v1, value = 2, command = self.checkButtonPress)
 
        assignLabel.grid(row = 1, column = 1)
        assignEntry.grid(row = 1, column = 2)
        examLabel1.grid(row = 2, column = 1)
        examEntry1.grid(row = 2, column = 2)
        examLabel2.grid(row = 3, column = 1)
        examEntry2.grid(row = 3, column = 2)
        particLabel.grid(row = 4, column = 1)
        particEntry.grid(row = 4, column = 2)
        labLabel.grid(row = 5, column = 1)
        labEntry.grid(row = 5, column = 2)
        examLabel3.grid(row = 6, column = 1)
        examEntry3.grid(row = 6, column = 2)
 
        displayEntry.grid(row = 1, column = 1)
        rbScore1.grid(row = 4, column = 1)
        rbScore2.grid(row = 5, column = 1)
 
        window1.mainloop()

    def calculateScore1(self):
        a1 = float(self.assignment.get())
        e1 = float(self.exam1.get())
        e2 = float(self.exam2.get())
        p1 = float(self.participation.get())
        l1 = float(self.lab.get())
        e3 = float(self.exam3.get())

        Total = (a1*.2 + e1*.15 + e2*.15 + p1*.1 + l1*.2 + e3*.2)
        self.result.set(Total)
        return self.result

    def calculateScore2(self):
        a1 = float(self.assignment.get())
        e1 = float(self.exam1.get())
        e2 = float(self.exam2.get())
        p1 = float(self.participation.get())
        l1 = float(self.lab.get())
        e3 = float(self.exam3.get())

        Total = (a1*.2 + e1*.1 + e2*.15 + p1*.1 + l1*.2 + e3*.25)
        self.result.set(Total)
        return self.result

    def checkButtonPress(self):
        if self.v1.get() == 1:
            self.calculateScore1()
        else:
            self.calculateScore2()
            
 
MyGUI()
