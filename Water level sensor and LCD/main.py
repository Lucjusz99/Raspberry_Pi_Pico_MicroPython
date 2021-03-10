import machine
import utime
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
I2C_ADDR = 0x27 #adres wyświetlacza z pliku pico_i2c_lcd_test
I2C_NUM_ROWS = 2 #wiersze wyświetlacza
I2C_NUM_COLS = 16 #kolumny wyświetlacza

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
sensor_value=machine.ADC(28)

while True:
    reading=sensor_value.read_u16()
    print("Value: ", reading)
    utime.sleep(1)
    lcd.clear()
    lcd.move_to(0,0) 
    lcd.putstr('Water :')
    lcd.move_to(8,0)
    if reading < 25000:
        lcd.putstr('Low')
    else:
        if reading > 29000:
            lcd.putstr('High')
        else:
            lcd.putstr('Medium')
        
    

