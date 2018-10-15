import rcpy
import rcpy.servo as servo
import rcpy.clock as clock
import rcpy.motor as motor
import time
#variables
#
#servo channel
s_channel = 1
#motor channel
m_channel_l = 2
m_channel_r = 3


# defaults
duty = 1.5
period = 0.02
d = 0.1
# set servo duty (only one option at a time)
srvo = servo.Servo(s_channel)
#left motor
mtr_l  = motor.Motor(m_channel_l)
#right motor
mtr_r = motor.Motor(m_channel_r)

#enables servo
servo.enable()
# start clock
clck.start()


while(1):
    motor.set(m_channel_l, 1)
    #srvo.set(d)
    time.sleep(.02)
