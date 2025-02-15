import tkinter as ui
import time


window=ui.Tk()
window.configure(bg="#000000")
window.geometry("500x200")

timelabel=ui.Label(
    text="00:00:00",
    font=("Arial",40),
    bg="#000000",
    fg="#ffffff"
)
timelabel.pack(pady=20)

datelabel=ui.Label(
    text="DayName , MonthName day, Year",
    font=("Arial",20),
    bg="#000000",
    fg="#ffffff"
)
datelabel.pack(pady=20)

def updateTime():
    hour=time.strftime("%I")
    min=time.strftime("%M")
    sec=time.strftime("%S")
    AMorPM=time.strftime("%p")
    timetext=f"{hour}:{min}:{sec} {AMorPM}"
    timelabel.config(text=timetext)
    timelabel.after(1000,updateTime)

def updateDate():
    dayName=time.strftime("%A")
    monthName=time.strftime("%B")
    day=time.strftime("%d")
    year=time.strftime("%Y")
    datetext=f"{dayName}, {monthName} {day}, {year}"
    datelabel.config(text=datetext)
    #datelabel.after(1000,updateDate)

updateDate()
updateTime()
window.mainloop()
