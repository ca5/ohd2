from firmata import *
import time


class ArduinoWrapper:
    __arduino = None
    
    def __init__(self):
        self.connect()

    def connect(self):
        #self.__arduino = Arduino(5,baudrate=57600) # 3 for COM4
        #self.__arduino = Arduino('/dev/cu.usbmodemfd121',baudrate=57600) 
        self.__arduino = Arduino('/dev/cu.usbmodemfd121') 

    def init_pin(self, num):
        print "init pin: %s" %str(num)
        self.__arduino.pin_mode(num,firmata.OUTPUT)
        self.__arduino.delay(2)
        print "init done" 

    def update_pin(self, num, status):
        if status:
            print "update pin: %s -> ON" %str(num)
            self.__arduino.digital_write(num,firmata.HIGH)
            self.sleep(2)
        else:
            print "update pin: %s -> OFF" %str(num)
            self.__arduino.digital_write(num,firmata.LOW)
            self.sleep(2)
        print "update done" 

    def sleep(self, num):
        return self.__arduino.delay(num)

        



def test():
    #arduino = Arduino('/dev/cu.usbmodemfd121',baudrate=57600) # 3 for COM4
    #arduino.pin_mode(13,firmata.OUTPUT)
    #arduino.delay(2)
    #
    #arduino.digital_write(13,firmata.HIGH)
    #arduino.delay(3)
    #arduino.digital_write(13,firmata.LOW)
    #arduino.delay(3)

    arduino = ArduinoWrapper()
    arduino.init_pin(13)
    arduino.sleep(3)
    arduino.update_pin(13, True)
    arduino.update_pin(13, False)
    arduino.update_pin(13, True)
    arduino.update_pin(13, False)




if __name__ == '__main__':
    test()
