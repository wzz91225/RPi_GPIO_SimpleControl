# coding:utf-8

import time
from RPi import GPIO



class GPIO_Control():
    PWM_N = 6
    PWM_Pin = [12, 13, 16, 18, 20, 21]
    fre = []
    dc = []
    pwm = []

    def __init__(self, fre_list, dc_list):
        self.fre = fre_list[:]
        self.dc = dc_list[:]

        GPIO.setmode(GPIO.BCM)
        for i in range(self.PWM_N):
            GPIO.setup(self.PWM_Pin[i], GPIO.OUT)
            self.pwm.append(GPIO.PWM(self.PWM_Pin[i], self.fre[i]))
            self.pwm[i].start(self.dc[i])

    def ChangeAllDutyCycle(self, dc_new_list):
        self.dc = dc_new_list[:]
        for i in range(self.PWM_N):
            self.pwm[i].ChangeDutyCycle(self.dc[i])

    def ChangeDutyCycle(self, channel, dc_new):
        self.dc[channel] = dc_new
        self.pwm[channel].ChangeDutyCycle(self.dc[channel])

    def ChangeAllFrequency(self, fre_new_list):
        self.fre = fre_new_list[:]
        for i in range(self.PWM_N):
            self.pwm[i].ChangeFrequency(self.fre[i])

    def ChangeFrequency(self, channel, fre_new):
        self.fre[channel] = fre_new
        self.pwm[channel].ChangeFrequency(self.fre[channel])



if __name__ == "__main__":
    f = GPIO_Control([100, 80, 60, 50, 33, 13], [50, 25, 75, 33, 45, 66])
