import tkinter
import time
import datetime


def get_time(clock_label):
    current_time = time.strftime("%H:%M:%S")
    current_date = str(datetime.datetime.today())
    clock_date = "{} {}".format(current_date[:10], current_time)
    clock_label.config(text=clock_date)

    def get_time_r():
        get_time(clock_label)
    clock_label.after(1000, get_time_r)


def start_timer(timer_label, start_time):
    now_time = datetime.datetime.now()
    delta = now_time - start_time
    adjusted_delta = divmod(delta.days * 86400 + delta.seconds, 60)
    l = []
    for i in adjusted_delta:
        l.append(i)
    second = l[1]
    minute = l[0]
    time_text = "00:{1}:{0}".format(second, minute)
    timer_label.config(text=time_text)

    def update_time():
        start_timer(timer_label, start_time)
    timer_label.after(1000, update_time)


def stop_timer(timer_label):
    timer_label.config(text='00:00:00')


class MainApp:

    def __init__(self, mainwindow):

        self.mainWindow = mainwindow

        # creating a screen with 320x480 resolution, white background
        mainwindow.geometry("480x320+0+0")
        mainwindow.configure(background='white')

        # clock/date
        time_frame = tkinter.Frame(mainwindow, width=240, height=40)
        time_frame.grid(row=0, column=0, columnspan=3, sticky='nw')

        clock = tkinter.Label(time_frame, text="", font=('Calibri', 10, 'bold'))
        clock.grid(row=0, column=0, pady=(0, 30), sticky='nw')

        get_time(clock)

        # username
        username_frame = tkinter.Frame(mainwindow, width=240, height=40)
        username_frame.grid(row=0, column=3, columnspan=3, sticky='ne')

        username_label = tkinter.Label(username_frame, text="UserName",  font=('Calibri', 10, 'bold'))
        username_label.grid(row=0, column=5, pady=(0, 30), sticky='ne')

        # speed counter
        speed_frame = tkinter.Frame(mainwindow, width=240, height=160, bg='red')
        speed_frame.grid(row=1, column=0, columnspan=2)

        speed_macro_label = tkinter.Label(speed_frame, text="0.", font=('Calibri', 40, 'bold'))
        speed_macro_label.grid(row=1, column=0, sticky="e")

        speed_micro_label = tkinter.Label(speed_frame, text="00", font=('Calibri', 20, 'bold'))
        speed_micro_label.grid(row=1, column=1, sticky="w")

        # distance counter
        distance_frame = tkinter.Frame(mainwindow, width=240, height=160, bg='cyan')
        distance_frame.grid(row=1, column=2, columnspan=3)

        dist_macro_label = tkinter.Label(speed_frame, text="0.", font=('Calibri', 40, 'bold'))
        dist_macro_label.grid(row=1, column=2, sticky="e")

        dist_micro_label = tkinter.Label(speed_frame, text="00", font=('Calibri', 20, 'bold'))
        dist_micro_label.grid(row=1, column=3, sticky="w")

        # start/stop distance/speed buttons
        start_button_frame = tkinter.Frame(mainwindow, width=160, height=200)
        start_button_frame.grid(row=1, column=4, columnspan=2, rowspan=2)

        start_stop_speed_dist_btn = tkinter.Button(start_button_frame, text="Go", font=('Calibri', 20, 'bold'))
        start_stop_speed_dist_btn.grid(row=1, column=4, columnspan=2, rowspan=2, padx=10, pady=10, sticky='nsew')

        # units labels
        speed_units_frame = tkinter.Frame(mainwindow, width=160, height=40)
        speed_units_frame.grid(row=2, column=0, columnspan=2)

        speed_units_label = tkinter.Label(speed_units_frame, text="mi/hr")
        speed_units_label.grid(row=2, column=0, columnspan=2, sticky='ew')

        dist_units_frame = tkinter.Frame(mainwindow, width=160, height=40)
        dist_units_frame.grid(row=2, column=2, columnspan=2)

        dist_units_label = tkinter.Label(speed_units_frame, text="mi")
        dist_units_label.grid(row=2, column=2, columnspan=2, sticky='ew')

        # timer
        timer_frame = tkinter.Frame(mainwindow, width=480, height=40, bg='yellow')
        timer_frame.grid(row=3, column=0, columnspan=6)

        timer_label = tkinter.Label(timer_frame, text='00:00:00', font=('Calibri', 10, 'bold'), bg='white')
        timer_label.grid(row=3, column=1, columnspan=2, sticky='nsew')
        #
        # def starttime():
        #     start_time = datetime.datetime.now()
        #     start_timer(timer_label, start_time)

        # start button (maybe combine these two?
        start_stop_btn = tkinter.Button(timer_frame, text='Start/Stop', font=('Calibri', 10, 'bold'), bg='red')
        start_stop_btn.grid(row=3, column=4, padx=3)

        # def stop():
        #     start_time = datetime.datetime.now()
        #     stop_timer(timer_label, start_time)
        #
        # # stop button
        # stop_btn = tkinter.Button(timer_frame, text='Stop', font=('Calibri', 10, 'bold'), bg='red', command=stop)
        # stop_btn.grid(row=1, column=2, padx=3)

        # conversion
        convert_frame = tkinter.Frame(mainwindow, width=240, height=40, bg='black')
        convert_frame.grid(row=4, column=0)

        # settings
        settings_frame = tkinter.Frame(mainwindow, width=240, height=40, bg='magenta')
        settings_frame.grid(row=4, column=6)


if __name__ == "__main__":

    root = tkinter.Tk()
    root.title("Bike App")
    my_app = MainApp(root)
    root.mainloop()
