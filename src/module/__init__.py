from pyfirmata import Arduino, util
import time

DEFAULT_COMPORT = '/dev/cu.usbmodemfd121'

class ArduinoWrapper:
    __arduino = None
    
    def __init__(self, com=None):
        self.connect(com)

    def connect(self, com=None):
        if com != None:
            self.__arduino = Arduino(com) 
        else:
            self.__arduino = Arduino(DEFAULT_COMPORT) 

    def update_pin(self, num, status):
        if status:
            print "update pin: %s -> ON" %str(num)
            return self.__arduino.digital[num].write(1)
        else:
            print "update pin: %s -> OFF" %str(num)
            return self.__arduino.digital[num].write(0)

    def get_pin(self, status):
            return self.__arduino.get_pin(status)
        



def test():
    arduino = ArduinoWrapper()
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
