import os
import tkinter as tk
import time
from plyer import notification

tick = time.asctime(time.localtime(time.time()))

root = tk.Tk()
root.title('Close App')
root.iconbitmap('support.ico')
root.config(bg='#D9D8D7')
# root.wm_attributes('-transparentcolor','#4a7a8c')
root.geometry("400x120")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

Font = ("Comic Sans MS", 10, "bold")

label = tk.Label(root, text='Close App', bg='#D9D8D7')
label.configure(font=Font)
label.grid(column=0, row=0, sticky=tk.W, padx=5)


label = tk.Label(root, text=tick, width=29, pady=5, bg='#D9D8D7')
label.configure(font=Font)
label.place(relx=0.01, rely=0.85, anchor='sw')
# label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

entry = tk.Entry(root, bg='#D9D8D7', width=40)
entry.configure(font=Font)
entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

label_time = tk.Label(root, text='Timer' ,bg='#D9D8D7')
label_time.configure(font=Font)
label_time.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

entry1 = tk.Entry(root, bg='#D9D8D7', width=40)
entry1.configure(font=Font)
entry1.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
value = entry1.get()

print(value)

def closeFiled():
    try:
        os.system(f'TASKKILL /F /IM {entry.get()}.exe')
        entry.delete(0, tk.END)
    except Exception as e:
        print(e)


def countdown(ts):
    message = 'Close app has started'
    message1 = 'Apps will soon close'
    if ts == ts:
        notification.notify(title='Closing Apps', message=message, app_name='Close Apps', app_icon='support.ico',
                            timeout=5,
                            toast=False)
    while ts:
        mines, secs = divmod(ts, 60)
        timer = f'{mines:02d}:{secs:02d}'
        print(timer, end="\n")
        if ts <= 10:
            notification.notify(title='Closing Apps', message=message1, app_name='Close Apps', app_icon='support.ico',
                                timeout=10,
                                toast=False)
        time.sleep(1)
        ts -= 1
    closeFiled()


button = tk.Button(root,bg='#D9D8D7', text='Start', command=closeFiled(), compound=tk.CENTER, width=20 )
button.grid(column=1, row=2, sticky=tk.E, padx=5, ipady=5)

root.mainloop()
