import tkinter as tk
import webbrowser
from time import *
import datetime
import threading

wk = tk.Tk()
wk.title("Remind me")

time_list = []
url_list = []

def open_site():
    wait = 1
    try:
        while(wait == 1): 
            if len(time_list) >= 1: 
                for index, remind_time in enumerate(time_list):
                    now = datetime.datetime.now()
                    wait_time = datetime.datetime(*remind_time) - now
                    wait_seconds = int(wait_time.total_seconds())
                    if wait_seconds <= 0:
                        webbrowser.open_new_tab(url_list[index])
                        time_list.remove(time_list[index])
                        url_list.remove(url_list[index])
                        print(time_list)
                        print(url_list)
    except Exception as ex:
        print(ex)

t = threading.Thread(target=open_site)        
        
def add_time():
    date_str = date_entry.get()
    time_str = time_entry.get()
    url = url_entry.get()
    try:
        year, month, day = map(int, date_str.split("/"))
        hour, minute = map(int, time_str.split(":"))
        remind_time = (year, month, day, hour, minute)
        time_list.append(remind_time)
        url_list.append(url)
        print(f"Added time: {remind_time}")
    except ValueError:
        print("Invalid date or time format")
        

       
url_label = tk.Label(wk, text="URL:")
url_entry = tk.Entry(wk)
url_label.pack()
url_entry.pack()


# 시간 선택 창
time_label = tk.Label(wk, text="Remind Time:")
time_label.pack()

date_label = tk.Label(text="Date (YYYY/MM/DD)")
date_label.pack()
date_entry = tk.Entry(width=20)
date_entry.pack()

time_label = tk.Label(text="Time (HH:MM)")
time_label.pack()
time_entry = tk.Entry(width=20)
time_entry.pack()

add_button = tk.Button(text="Add Time", command=add_time)
add_button.pack()

t.start()
wk.mainloop()    
t.join()
print("program exit")