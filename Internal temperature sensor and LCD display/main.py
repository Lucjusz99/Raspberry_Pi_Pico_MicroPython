import utime #import potrzebnych funkcji i bibliotek
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
I2C_ADDR     = 0x27 #adres wyświetlacza z pliku pico_i2c_lcd_test
I2C_NUM_ROWS = 2 #wiersze wyświetlacza
I2C_NUM_COLS = 16 #kolumny wyświetlacza

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
adc = machine.ADC(4) #definicja wewnętrznego czujnika temp
conversion_factor = 3.3 / (65535) #przelicznik
while True:
    reading = adc.read_u16() * conversion_factor
    temperature = 25 - (reading - 0.706)/0.001721 #przelicznik wskazania czujnika na temperaturę w stopniach C
    t=round(temperature, 1) #zaokrąglanie do 1 miejsca po ,
    print("Temperature: {}".format(t)) #wypisywanie temperatury w shellu
    utime.sleep(1)
    lcd.clear() #czyszczenie wyświetlacza
    lcd.move_to(0,0) 
    lcd.putstr('Temp :') #Wypisywanie napisu "Temp :" od początku wyświetlacza 1 rzędu wyświetlacza
    lcd.move_to(7,0)
    lcd.putstr(str(t)+" C") #wypisywanie wartości temperatury + "C" od 7 pola 1 rzędu wyświetlacza
    
