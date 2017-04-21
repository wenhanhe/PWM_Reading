import pigpio
import time
import os
import sys
pi = pigpio.pi()
save=[1,1610,1500,1575,1525,1425,1015]
set = 1
tick_0=[None,None,None,None,None,None,None]
tick_1=[None,None,None,None,None,None,None]
temp_read= [[1500 for col in range(21)] for row in range(7)]
count=[1,0,0,0,0,0,0]
def in_callback(argu,gpio,level,tick):
    if level == 0:
        tick_0[argu] = tick
        if tick_1[argu] is not None:
            diff = pigpio.tickDiff(tick_1[argu], tick)
            temp_read[argu][count[argu]] = diff
            count[argu]+=1
            if  count[argu]==20:
                sum_temp_read=0
                a=0
                for i in range(20):
                    sum_temp_read+=temp_read[argu][a]
                    a+=1
                save[argu]=sum_temp_read/20
                count[argu]=0
    else:
        tick_1[argu] = tick
def mycallback1(gpio, level, tick):
    if level == 0:
        tick_0[1] = tick
        if tick_1[1] is not None:
            diff = pigpio.tickDiff(tick_1[1], tick)
            temp_read[1][count[1]] = diff
            count[1] += 1
            if count[1]==20:
                sum_temp_read = 0
                a = 0
                for i in range(20):
                    sum_temp_read += temp_read[1][a]
                    a += 1
                save[1] = sum_temp_read / 20
                count[1] = 0
            fp = file('/var/send.tem', 'w')
            print>> fp, "a%04db%04dc%04dd%04de%04df%04d" % (save[1],save[2],save[3],save[4],save[5],save[6])
            fp.close()
    else:
        tick_1[1] = tick
def mycallback2(gpio, level, tick):
    in_callback(2, gpio, level, tick)
def mycallback3(gpio, level, tick):
    in_callback(3, gpio, level, tick)
def mycallback4(gpio, level, tick):
    in_callback(4, gpio, level, tick)
def mycallback5(gpio, level, tick):
    in_callback(5, gpio, level, tick)
def mycallback6(gpio, level, tick):
    in_callback(6, gpio, level, tick)

if __name__=="__main__":

    cb1 = pi.callback(4, pigpio.EITHER_EDGE, mycallback1)
    cb2 = pi.callback(17, pigpio.EITHER_EDGE, mycallback2)
    cb3 = pi.callback(27, pigpio.EITHER_EDGE, mycallback3)
    cb4 = pi.callback(22, pigpio.EITHER_EDGE, mycallback4)
    cb5 = pi.callback(10, pigpio.EITHER_EDGE, mycallback5)
    cb6 = pi.callback(9, pigpio.EITHER_EDGE, mycallback6)
    set = eval(raw_input("If you want to cancel please type 1 and press enter"))
    if set == 1:
        cb1.cancel()
        cb2.cancel()  # cancel callback
        cb3.cancel()
        cb4.cancel()
        cb5.cancel()
        cb6.cancel()
    else:
        cb1.cancel()
        cb2.cancel()  # cancel callback
        cb3.cancel()
        cb4.cancel()
        cb5.cancel()
        cb6.cancel()


