from module import *
import time

a = ArduinoWrapper()
pin2 = a.get_pin('d:2:o')
pin3 = a.get_pin('d:3:p')
a.update_pin(13, True)
print 'write 1'
pin2.write(1)
pin3.write(1.0)
time.sleep(2)
print 'write 0'
pin2.write(0)
pin3.write(0.0)
a.update_pin(13, False)
