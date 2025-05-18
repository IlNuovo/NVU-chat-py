from configure import Configurator
from GUI import gui
from tkinter import END
import Comms

config = Configurator()
conf_file = './conf.json'

if config.exists(conf_file):
    print('extracting data from configuration')
    data = config.extract_conf(conf_file)
else:
    print('creating a default configuration')
    config.create_conf(conf_file)

print('pre-load complete, starting application')

conn = Comms.MultiService(6000, srv='localhost')
last = conn.sender.recv_log
def function (event=None):
    if not(g.writing_message.get() == ''):
        #print(g.writing_message.get())
        global last, conn
        conn.send_msg(g.writing_message.get())
        last.append(g.writing_message.get())
        strin = ''
        for i in range(len(last)):
            strin += 'you: ' + last[i] + '\n'
        g.upd(strin)
        g.message_entry.delete(0, END)
        g.text_widget.see("end")


g = gui(function)


g.root.mainloop()