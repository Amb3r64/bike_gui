import tkinter
import time
root = tkinter.Tk()
clock = tkinter.Label(root, font=('times', 20, 'bold'), bg='green')
clock.grid(row=0, column=0)


def tick():
    clock_time = time.strftime('%H:%M:%S')
    clock.config(text=clock_time)
    clock.after(200, tick)
tick()
root.mainloop()