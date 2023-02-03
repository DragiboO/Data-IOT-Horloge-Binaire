from machine import Pin, PWM, ADC
import network
import urequests
import utime
import ujson

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'Julien'
password = 'jujudra0'
wlan.connect(ssid, password)
url = "http://192.168.43.23:3000/"

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

def binaryRead(binary, out1 = 0, out2 = 0, out3 = 0, out4 = 0):

    led1 = {}
    led2 = {}
    led3 = {}
    led4 = {}

    if out1 != 0:
        led1 = Pin(out1, mode=Pin.OUT)
    if out2 != 0:
        led2 = Pin(out2, mode=Pin.OUT)
    if out3 != 0:
        led3 = Pin(out3, mode=Pin.OUT)
    if out4 != 0:
        led4 = Pin(out4, mode=Pin.OUT)

    if out1 != 0:
        if int(binary[0]) != led1.value():
            led1.toggle()

    if out2 != 0:
        if int(binary[1]) != led2.value():
            led2.toggle()

    if out3 != 0:
        if int(binary[2]) != led3.value():
            led3.toggle()

    if out4 != 0:
        if int(binary[3]) != led4.value():
            led4.toggle()

while not wlan.isconnected():
    utime.sleep(1)
    print("pas co")
print("co")

while(True):

    try:
        r = urequests.get(url)
        data = r.json()["time"]
        r.close()

        datas = data.replace(':',' ')
        dataf = datas.split()

        for i in range(3):
            dataf[i] = int(dataf[i])
        
        dataf[0] += 1

        if dataf[3] == 'PM':
            dataf[0] += 12
        
        datass = []

        for i in range(3):
            dozen = dataf[i] // 10
            unit = dataf[i] % 10
            datass.extend((dozen, unit))

        for i in range(6):
            datass[i] = bin(datass[i])[2:]

        for i in range(6):
            while len(datass[i]) < 4:
                datass[i] = ''.join(('0', datass[i]))

        binaryRead(datass[0], 0, 0, 6, 7)
        binaryRead(datass[1], 8, 9, 10, 11)
        binaryRead(datass[2], 0, 12, 13, 14)
        binaryRead(datass[3], 15, 28, 27, 26)
        binaryRead(datass[4], 0, 22, 21, 20)
        binaryRead(datass[5], 19, 18, 17, 16)

        utime.sleep(0.5)
    except Exception as e:
        print(e)