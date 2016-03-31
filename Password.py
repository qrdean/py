#Quinton Dean
#This is a simple GUI to tell how strong a password is

from tkinter import*
class MyGUI:
    def __init__(self):
        window1 = Tk()
        window1.title("Password Confirmer")
 
        frame1 = Frame(window1)
        frame1.pack()
       
        passLabel1 = Label(frame1, text = "Enter Password")
        self.name1 = StringVar()
        passEntry1 = Entry(frame1, textvariable = self.name1, show = '*')
 
        passLabel2 = Label(frame1, text = "Enter Password")
        self.name2 = StringVar()
        passEntry2 = Entry(frame1, textvariable = self.name2, show = '*')
 
        saveButton = Button(frame1, text = "Save", command = self.processCheck_saveButton)
 
        self.result = StringVar()
        self.result.set("")
        resultMessage = Message(frame1, textvariable = self.result)
 
        passLabel1.grid(row = 1, column = 1)
        passEntry1.grid(row = 1, column = 2)
        passLabel2.grid(row = 2, column = 1)
        passEntry2.grid(row = 2, column = 2)
        saveButton.grid(row = 3, column = 3)
        resultMessage.grid(row = 4, column = 1)
       
        window1.mainloop()
 
    def parseChecker(self, p1, s1):
        statement = False
        for i in range(0, len(s1)):
            for j in range(0, len(p1)):
                if s1[i] == p1[j]:
                    statement = True
                    return statement
           
            
    def processCheck_saveButton(self):
        strength = ['', 'Weak', 'Acceptable', 'Strong', 'SuperStrong']
        score = 0
        s1 = self.name1.get()
        s2 = self.name2.get()
        if len(s1) >= 8:
            if s1 == s2:
                if self.parseChecker('abcdefghijklmnopqrstuvwxyz', s1):
                    score = score + 1
                if self.parseChecker('.[!@#$%^&*()_~-]=+/\<>,', s1):
                    score = score + 1
                if self.parseChecker('ABCDEFGHIJKLMNOPQRSTUVWXYZ', s1):
                    score = score + 1
                if self.parseChecker('0123456789', s1):
                    score = score + 1
 
                self.result.set(strength[score])
                return self.result
            else:
                self.result.set("Passwords_don't_match")
                return self.result
               
        else:
            self.result.set("Password_too_short")
            return self.result
               
        
MyGUI()
