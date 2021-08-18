#Random Password Support File
import sys
import main
import random


List_ABC = ['A','B','C','D','E','F','G','H','I','K','J','L','M'
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#List of alphabets

List_abc = ['a','b','c','d','e','f','g','h','i','k','j','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']#list of alphabets

List_num = ['0','1','2','3','4','5','6','7','8','9']#List of numbers

List_spc = ['~','!','@','#','$','%','^','&','*','_']#List of Special characters

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

class Generator():
    password1 = ""
    # Function to convert
    def listToString(self,s):
            
            # initialize an empty string
            str1 = ""
            
            # traverse in the string
            for ele in s:
                    str1 += ele
            
            # return string
            return str1
    def thief(self,w):
        password1=setattr(Generator,'password1',w)
        
    def Password(self):
        Total_count = int(w.Entry1.get())
        Spcl_count = int(w.Entry1_1.get())
        Num_count = int(w.Entry1_1_1.get())
        flag1=True
        flag2=True
        flag3=True
        if (Total_count>=8 and Total_count<=16):
            w.Label1_1_1_1_1_1_3.configure(text=''' ''')
        else:
            flag1 = False
            w.Label1_1_1_1_1_1_3.configure(text='''*Invalid''')
        if (Spcl_count<1):
            flag2 = False
            w.Label1_1_1_1_1_1_3_1.configure(text='''*Invalid''')
        else:
            w.Label1_1_1_1_1_1_3_1.configure(text=''' ''')
        if (Num_count<1):
            flag3 = False
            w.Label1_1_1_1_1_1_3_2.configure(text='''*Invalid''')
        else:
            w.Label1_1_1_1_1_1_3_2.configure(text=''' ''')
            
        if (Total_count==(Num_count+Spcl_count) or Total_count==Num_count or Total_count==Spcl_count):
            flag2 = False
            flag3 = False
            w.Label1_1_1_1_1_1_3_1.configure(text='''*Invalid''')
            w.Label1_1_1_1_1_1_3_2.configure(text='''*Invalid''')
        else:
            flag2 = True
            flag3 = True
            w.Label1_1_1_1_1_1_3_1.configure(text=''' ''')
            w.Label1_1_1_1_1_1_3_2.configure(text=''' ''')
        

        if(flag1==True and flag2==True and flag3==True):
                         
            abc_count = Total_count-(Num_count+Spcl_count)
            if(abc_count == 0):
                if(Num_count>Spcl_count):
                    Num_count=Num_count-2
                    abc_count = abc_count+1
                else:
                    Spcl_count = Spcl_count-2
                    abc_count = abc_count+1
                

            password = [] #Empty list for password
            
            
            password.append(random.choice(List_ABC))

            for i in range(abc_count-1):
                password.append(random.choice(List_abc))

            for i in range(Num_count):
                password.append(random.choice(List_num))

            for i in range(Spcl_count):
                password.append(random.choice(List_spc))

            random.shuffle(password)
            
            password1 = self.listToString(password)
            self.thief(password1)
            
            w.Label1_1_1_1_1.configure(text=password1)
            
   
    def Mail(self):
            import smtplib, ssl

            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "testing@gmail.com"  # Enter your address
            receiver_email = w.Entry1_1_1_1.get()  # Enter receiver address
            password = "Abcdef@123"
            key = getattr(Generator,'password1')
            message = """\
            Subject: Random Password Generator


            your password is {password}"""

            context = ssl.create_default_context()
            try:
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message.format(password=key))
            except:
                w.Label1_1_1_1_1_1_3_3.configure(text='''*Invalid''')
C = Generator()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import main
    main.vp_start_gui()




