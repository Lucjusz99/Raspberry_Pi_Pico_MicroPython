from machine import Pin #import potrzebnych funkcji i bibliotek
from utime import sleep
import _thread

#przypisanie wszystkich LED do odpowiednich pinów
led_r=Pin(15, Pin.OUT)
led_y=Pin(14, Pin.OUT)
led_g=Pin(13, Pin.OUT)
led_r_p=Pin(11, Pin.OUT)
led_y_p=Pin(10, Pin.OUT)
led_g_p=Pin(9, Pin.OUT)
#przypisanie buzzera i przycisku
button=Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer=Pin(12, Pin.OUT)

#wygaszanie wszystkich LEDów
led_r.value(0)
led_y.value(0)
led_g.value(0)
led_r_p.value(0)
led_y_p.value(0)
led_g_p.value(0)

global button_pressed #definicja zmiennej stanu przycisku
button_pressed=False

def button_reader_thread(): #wątek służący do sprawdzania czy przycisk został wciśnięty
    global button_pressed
    while True:
        if button.value()==1:
            button_pressed=True #zmienna przyjmuje wartość true gdy przycisk został wciśnięty
        sleep(0.01)
_thread.start_new_thread(button_reader_thread, ())

while True: #nieskończona pętla
    if button_pressed==True: #jeśli przycisk został wciśnięty:
        led_g.value(1) #sekwencja LEDów i brzęczka
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
        global button_pressed #zmienna "button_pressed" negowana po sekwencji
        button_pressed=False
    led_g.value(1) #LEDy świecące się gdy przycisk nie został wciśnięty
    led_r_p.value(1)
