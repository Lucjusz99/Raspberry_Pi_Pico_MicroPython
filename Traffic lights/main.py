from machine import Pin
from utime import sleep
import _thread

led=Pin(25, Pin.OUT)
led_r=Pin(15, Pin.OUT)
led_y=Pin(14, Pin.OUT)
led_g=Pin(13, Pin.OUT)
button=Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer=Pin(12, Pin.OUT)
led_r_p=Pin(11, Pin.OUT)
led_y_p=Pin(10, Pin.OUT)
led_g_p=Pin(9, Pin.OUT)

led_r.value(0)
led_y.value(0)
led_g.value(0)
led_r_p.value(0)
led_y_p.value(0)
led_g_p.value(0)

global button_pressed
button_pressed=False

def button_reader_thread():
    global button_pressed
    while True:
        if button.value()==1:
            button_pressed=True
        sleep(0.01)
_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed==True:
        led_g.value(1)
        led_r_p.value(1)
        sleep(2)
        led_g.value(0)
        led_y.value(1)
        led_y_p.value(1)
        sleep(2)
        led_r_p.value(0)
        led_y_p.value(0)
        led_g_p.value(1)
        led_y.value(0)
        led_r.value(1)
        for i in range(10):
            buzzer.value(1)
            sleep(0.2)
            buzzer.value(0)
            sleep(0.2)
        led_g_p.value(0)
        led_y.value(1)
        led_y_p.value(1)
        sleep(2)
        led_r.value(0)
        led_y.value(0)
        led_g.value(1)
        led_r_p.value(1)
        led_y_p.value(0)
        sleep(2)
        global button_pressed
        button_pressed=False
    led_g.value(1)
    led_r_p.value(1)
