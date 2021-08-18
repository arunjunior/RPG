#Random Password Generator

import sys

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

import main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("449x435+442+141")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(width = False,height = False)
        top.title("Random Password Generator")
        top.configure(background="#2bcbba")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.089, rely=0.115, height=40, width=128)
        self.Label1.configure(background="#2bcbba")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI Light} -size 11 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''Password Length''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.49, rely=0.115, height=30, relwidth=0.276)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.049, rely=0.244, height=40, width=160)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#2bcbba")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Segoe UI Light} -size 11 -weight bold")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Spcl Character count''')

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.49, rely=0.253, height=30, relwidth=0.276)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.Label1_1_1 = tk.Label(top)
        self.Label1_1_1.place(relx=0.098, rely=0.391, height=40, width=127)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(activeforeground="black")
        self.Label1_1_1.configure(background="#2bcbba")
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(font="-family {Segoe UI Light} -size 11 -weight bold")
        self.Label1_1_1.configure(foreground="#000000")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''Number count''')

        self.Entry1_1_1 = tk.Entry(top)
        self.Entry1_1_1.place(relx=0.49, rely=0.391, height=30, relwidth=0.276)
        self.Entry1_1_1.configure(background="white")
        self.Entry1_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1.configure(foreground="#000000")
        self.Entry1_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_1.configure(highlightcolor="black")
        self.Entry1_1_1.configure(insertbackground="black")
        self.Entry1_1_1.configure(selectbackground="blue")
        self.Entry1_1_1.configure(selectforeground="white")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.468, rely=0.529, height=24, width=47)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Create''')
        self.Button1.configure(command=main_support.C.Password)

        self.Label1_1_1_1_1 = tk.Label(top)#Password Label
        self.Label1_1_1_1_1.place(relx=0.334, rely=0.598, height=40, width=153)
        self.Label1_1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1_1.configure(activeforeground="black")
        self.Label1_1_1_1_1.configure(background="#2bcbba")
        self.Label1_1_1_1_1.configure(cursor="fleur")
        self.Label1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1_1.configure(font="-family {Segoe UI Light} -size 11")
        self.Label1_1_1_1_1.configure(foreground="#000000")
        self.Label1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1_1.configure(highlightcolor="black")
        

        self.Label1_1_1_2 = tk.Label(top)
        self.Label1_1_1_2.place(relx=0.089, rely=0.736, height=50, width=93)
        self.Label1_1_1_2.configure(activebackground="#f9f9f9")
        self.Label1_1_1_2.configure(activeforeground="black")
        self.Label1_1_1_2.configure(background="#2bcbba")
        self.Label1_1_1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_2.configure(font="-family {Segoe UI Light} -size 11 -weight bold")
        self.Label1_1_1_2.configure(foreground="#000000")
        self.Label1_1_1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_2.configure(highlightcolor="black")
        self.Label1_1_1_2.configure(text='''Mail ID''')

        self.Entry1_1_1_1 = tk.Entry(top)
        self.Entry1_1_1_1.place(relx=0.334, rely=0.759, height=30
                , relwidth=0.388)
        self.Entry1_1_1_1.configure(background="white")
        self.Entry1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1_1.configure(foreground="#000000")
        self.Entry1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_1_1.configure(highlightcolor="black")
        self.Entry1_1_1_1.configure(insertbackground="black")
        self.Entry1_1_1_1.configure(selectbackground="blue")
        self.Entry1_1_1_1.configure(selectforeground="white")

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.468, rely=0.874, height=24, width=47)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Send''')
        self.Button2.configure(command=main_support.C.Mail)
        
        self.Label1_1_1_1_1_1 = tk.Label(top)
        self.Label1_1_1_1_1_1.place(relx=0.468, rely=0.069, height=20, width=93)
        self.Label1_1_1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1_1_1.configure(activeforeground="black")
        self.Label1_1_1_1_1_1.configure(background="#2bcbba")
        self.Label1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1_1_1.configure(font="-family {Segoe UI Light} -size 8")
        self.Label1_1_1_1_1_1.configure(foreground="#000000")
        self.Label1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1_1_1.configure(highlightcolor="black")
        self.Label1_1_1_1_1_1.configure(text='''8-16characters''')

        self.Label1_1_1_1_1_1_1 = tk.Label(top)
        self.Label1_1_1_1_1_1_1.place(relx=0.49, rely=0.207, height=20, width=93)

        self.Label1_1_1_1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1_1_1_1.configure(activeforeground="black")
        self.Label1_1_1_1_1_1_1.configure(background="#2bcbba")
        self.Label1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1_1_1_1.configure(font="-family {Segoe UI Light} -size 8")
        self.Label1_1_1_1_1_1_1.configure(foreground="#000000")
        self.Label1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Label1_1_1_1_1_1_1.configure(text='''min one character''')

        self.Label1_1_1_1_1_1_2 = tk.Label(top)
        self.Label1_1_1_1_1_1_2.place(relx=0.49, rely=0.345, height=20
                , width=103)
        self.Label1_1_1_1_1_1_2.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1_1_1_2.configure(activeforeground="black")
        self.Label1_1_1_1_1_1_2.configure(background="#2bcbba")
        self.Label1_1_1_1_1_1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1_1_1_2.configure(font="-family {Segoe UI Light} -size 8")
        self.Label1_1_1_1_1_1_2.configure(foreground="#000000")
        self.Label1_1_1_1_1_1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1_1_1_2.configure(highlightcolor="black")
        self.Label1_1_1_1_1_1_2.configure(text='''use min one number''')

        
        self.Label1_1_1_1_1_1_3 = tk.Label(top)
        self.Label1_1_1_1_1_1_3.place(relx=0.78, rely=0.138, height=20, width=53)

        self.Label1_1_1_1_1_1_3.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1_1_1_3.configure(activeforeground="black")
        self.Label1_1_1_1_1_1_3.configure(background="#2bcbba")
        self.Label1_1_1_1_1_1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1_1_1_3.configure(font="-family {Segoe UI Light} -size 9 -weight bold")
        self.Label1_1_1_1_1_1_3.configure(foreground="#ff0000")
        self.Label1_1_1_1_1_1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1_1_1_3.configure(highlightcolor="black")
        #self.Label1_1_1_1_1_1_3.configure(text='''*Invalid''')

        self.Label1_1_1_1_1_1_3_1 = tk.Label(top)
        self.Label1_1_1_1_1_1_3_1.place(relx=0.78, rely=0.276, height=20
                , width=53)
        self.Label1_1_1_1_1_1_3_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1_1_1_3_1.configure(activeforeground="black")
        self.Label1_1_1_1_1_1_3_1.configure(background="#2bcbba")
        self.Label1_1_1_1_1_1_3_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1_1_1_3_1.configure(font="-family {Segoe UI Light} -size 9 -weight bold")
        self.Label1_1_1_1_1_1_3_1.configure(foreground="#ff0000")
        self.Label1_1_1_1_1_1_3_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1_1_1_3_1.configure(highlightcolor="black")
        #self.Label1_1_1_1_1_1_3_1.configure(text='''*Invalid''')

        self.Label1_1_1_1_1_1_3_2 = tk.Label(top)
        self.Label1_1_1_1_1_1_3_2.place(relx=0.78, rely=0.414, height=20
                , width=53)
        self.Label1_1_1_1_1_1_3_2.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1_1_1_3_2.configure(activeforeground="black")
        self.Label1_1_1_1_1_1_3_2.configure(background="#2bcbba")
        self.Label1_1_1_1_1_1_3_2.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1_1_1_3_2.configure(font="-family {Segoe UI Light} -size 9 -weight bold")
        self.Label1_1_1_1_1_1_3_2.configure(foreground="#ff0000")
        self.Label1_1_1_1_1_1_3_2.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1_1_1_3_2.configure(highlightcolor="black")
        #self.Label1_1_1_1_1_1_3_2.configure(text='''*Invalid''')

        self.Label1_1_1_1_1_1_3_3 = tk.Label(top)
        self.Label1_1_1_1_1_1_3_3.place(relx=0.735, rely=0.782, height=20
                , width=53)
        self.Label1_1_1_1_1_1_3_3.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1_1_1_3_3.configure(activeforeground="black")
        self.Label1_1_1_1_1_1_3_3.configure(background="#2bcbba")
        self.Label1_1_1_1_1_1_3_3.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1_1_1_3_3.configure(font="-family {Segoe UI Light} -size 9 -weight bold")
        self.Label1_1_1_1_1_1_3_3.configure(foreground="#ff0000")
        self.Label1_1_1_1_1_1_3_3.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1_1_1_3_3.configure(highlightcolor="black")
        #self.Label1_1_1_1_1_1_3_3.configure(text='''*Invalid''')

if __name__ == '__main__':
    vp_start_gui()





