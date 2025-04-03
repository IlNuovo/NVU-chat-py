from tkinter import ttk
from tkinter import Tk
from tkinter import Button, Entry, Label, Canvas, Scrollbar, Frame, Text
from tkinter import StringVar
from tkinter import X
from tkinter import BOTH

from tkinter import END

from typing import Callable


class gui:

    def nothing ():
        pass

    
    def __init__ (Self, send_f : Callable = nothing):
        Self.root = Tk()
        Self.root.title('NVU chat (python version)')
        Self.root.attributes('-fullscreen', True)
        Self.root.bind('<Escape>', Self.exit)
        Self.return_function = send_f
        Self.root.bind('<Return>', send_f)


        button = Button(Self.root, text = 'send', command=send_f, background='black', foreground='white', width=15,height=2, borderwidth=0)
        button.pack(fill = X,side="bottom")
        
        
        Self.writing_message = StringVar()
        Self.message_entry = Entry(Self.root, textvariable=Self.writing_message, width = 50)
        Self.message_entry.pack(fill=X,side="bottom")
        Self.message_entry.focus()

        label = Label(text='press <Escape> to quit')
        label.pack()

        canvas_frame = Frame(Self.root)
        canvas_frame.pack(fill="both", expand=True)

        scrollbar = Scrollbar(canvas_frame)
        scrollbar.pack(side="right", fill="y")


        Self.text_widget = Text(canvas_frame, wrap="word", height=10, width=40)
        Self.text_widget.pack(side="left", fill="both", expand=True)


        Self.text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=Self.text_widget.yview)

        long_text = ""
        Self.text_widget.insert("1.0", long_text)


        #Self.chat = Label(text_frame, text='to configure')
        #Self.chat.pack()
        #
        #text_frame.update_idletasks()
        #canvas.config(scrollregion=canvas.bbox("all"))

    
    def exit(Self, event=None):
        # Esci dalla modalità a schermo intero
        Self.root.quit()
    
    def upd (Self, newStr : str):
        Self.text_widget.delete('1.0',"end")
        Self.text_widget.insert("1.0", newStr)


#  NOTE importanti:
#
# Puoi chiudere la finestra con <Escape>
#
#   ESEMPIO:
last = []
def f (event=None):
    if not(g.writing_message.get() == ''):
        print(g.writing_message.get())
        global last 
        last.append(g.writing_message.get())
        strin = ''
        for i in range(len(last)):
            strin += 'you: ' + last[i]+ '\n'
        g.upd(strin)
        g.message_entry.delete(0, END)
        g.text_widget.see("end")


g = gui(f)


g.root.mainloop()
#
#print ('last message was:', last)