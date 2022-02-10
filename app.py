from tkinter import *
from tkinter import ttk
import platform, subprocess


root = Tk()
root.title('GUI')
root.geometry('400x150')


#def intervalClick(pevent):
    #Label(root, text=menuInterval.get()).pack()

optionInterval = [
    '100', '200', '300', '400', '500'
]

optionPort = [
    '1', '2', '3', '4', '5'
]

#Port text and drop box
textPort = Label(root, text = 'select port:')
textPort.place(x=10, y=0)

menuPort = ttk.Combobox(root, value=optionPort)
menuPort.current(0)
menuPort.place(x=10,y=20)


#Confrimation button for confirming settings
confirmButton = Button(root, text='confirm', width=10)
confirmButton.place(x=180, y=18)


#Interval text and drop box
textInterval = Label(root, text = 'select Interval:')
textInterval.place(x=10, y=50)

menuInterval = ttk.Combobox(root, value=optionInterval)
menuInterval.current(0)
#menuInterval.bind('<<ComboboxSelected>>', intervalClick)
menuInterval.place(x=10,y=70)


#print CPU name
def get_processor_info():
    if platform.system() == "Windows":
        name = subprocess.check_output(['wmic','cpu','get','name']).strip()
        return name
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl', "-n", "machdep.cpu.brand_string"]).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        return subprocess.check_output(command, shell=True).strip()
    return ""

bytes_data = []
a = get_processor_info()
for i in a:
    bytes_data.append(i)

b = "".join(map(chr, bytes_data[45:]))

textCpuName = Label(root, text = f'{b} :')
textCpuName.place(x=10, y=100)

root.mainloop()
