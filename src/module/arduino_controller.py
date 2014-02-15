from pyfirmata import Arduino, util
import time


class ArduinoController:
    __arduino = None
    
    def __init__(self):
        self.connect()

    def connect(self):
        self.__arduino = Arduino('/dev/cu.usbmodemfd121') 

    def update_pin(self, num, status):
        if status:
            print "update pin: %s -> ON" %str(num)
            self.__arduino.digital[num].write(1)
        else:
            print "update pin: %s -> OFF" %str(num)
            self.__arduino.digital[num].write(0)
        



def test():
    arduino = ArduinoController()
    time.sleep(1)
    arduino.update_pin(13, True)
    time.sleep(1)
    arduino.update_pin(13, False)
    time.sleep(1)
    arduino.update_pin(13, True)
    time.sleep(1)
    arduino.update_pin(13, False)

if __name__ == '__main__':
    test()
