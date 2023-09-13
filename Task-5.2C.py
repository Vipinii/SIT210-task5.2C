from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)

## LED PINS
red_Led = LED(16)
blue_Led = LED(20)
green_Led = LED(21)

## GUI ##
win = Tk()
win.title("LED Control")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight='bold')

# Dictionary to map button names to colors
button_colors = {
    'Red LED': 'red',
    'Blue LED': 'blue',
    'Green LED': 'green',
}

## EVENT ##
def toggle_led(led, led_var):
    if led_var.get() == 1:
        led.on()
    else:
        led.off()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

## WIDGETS ##
led_frame = Frame(win)
led_frame.grid(row=0, column=0)

# Function to create oval buttons with text and set text color
def create_oval_button(parent_frame, text, text_color, led_var, led, row, column):
    oval_button = Radiobutton(
        parent_frame,
        text=text,
        font=myFont,
        variable=led_var,
        value=1,
        command=lambda: toggle_led(led, led_var),
        bg=button_colors[text],
        fg=text_color,
        selectcolor='white',  # Color when selected
        indicatoron=False,    # Remove the indicator circle
    )
    oval_button.grid(row=row, column=column, padx=10, pady=5, ipadx=10, ipady=5)

create_oval_button(led_frame, 'Red LED', 'white', red_led_var, red_Led, 0, 0)
create_oval_button(led_frame, 'Blue LED', 'white', blue_led_var, blue_Led, 1, 0)
create_oval_button(led_frame, 'Green LED', 'white', green_led_var, green_Led, 2, 0)

exit_button = Button(win, text='EXIT', font=myFont, command=close, bg='red', fg='white', height=1, width=6)
exit_button.grid(row=1, column=0)

win.mainloop()
