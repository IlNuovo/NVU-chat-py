from configure import Configurator
from GUI import gui
from tkinter import END
import CComms as CComms
import threading





    

def receive_and_show (new : str):
    if g.gui_ready:
        strin = ''
        print(new)
        lock.acquire()
        last.append(new)
        print(last.pop(-1))
        for i in range(len(last)):
            strin += last[i] + '\n'
        lock.release()
        g.root.after(0, lambda: g.upd(strin))
    else:
        lock.acquire()
        last.append(new)
        lock.release()


def function (event=None):
    if not(g.writing_message.get() == ''):
        #print(g.writing_message.get())
        global last, conn
        conn.send_msg(g.writing_message.get())
        strin = ''
        lock.acquire()
        last.append('  you: ' + g.writing_message.get())
        for i in range(len(last)):
            strin += last[i] + '\n'
        lock.release()
        g.upd(strin)
        g.message_entry.delete(0, END)
        g.text_widget.see("end")

config = Configurator()
conf_file = './conf.json'

if config.exists(conf_file):
    print('extracting data from configuration')
    data = config.extract_conf(conf_file)
else:
    print('creating a default configuration')
    config.create_conf(conf_file)

print('pre-load complete, starting application')

g = gui(function)
g.root.after(0, g.mark_gui_ready)
lock = threading.Lock()

conn = CComms.MultiService(6000, srv=data['server'], link = receive_and_show)
last = conn.sender.recv_log




if conn:



    g.root.mainloop()
    conn.sender.running = False