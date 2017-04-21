# PWM_Reading
Use raspberry pi 3B to read pwm value,based on the pigpio library's python module（Python 2.7.13）.The accuracy is about +/- 10us.
The pwm wave comes from a model aircraft's 12Bits 9Channel receiver,produced by Shenzhen WFLY Technology Development Co.,Ltd.And in my program I only  read 6 channals.
This module uses the services of the C pigpio library. pigpio must be running on the Pi(s) whose GPIO are to be manipulated. 
The normal way to start pigpio is as a daemon (during system start). 

sudo pigpiod 

Your Python program must import pigpio and create one or more instances of the pigpio.pi class. This class gives access to a specified Pi's GPIO. 
###############################################################################################################################
I'm only a beginner  in programming so my codes may be not that...... elegant,anyway,it works perfecely on my Pi.
Have to say this program not only written by me,instead,I wrote it based on Joan's code  in https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=63509
，you can find Joan's code in Joan'code.py.Joan is the author of the pigpio library.
I creat this project in hoping that other beginners can learn to use this awesome library easier.Especially for Chinese learners,for I couldn't find much Chinese material in the internet. 
################################################################################################################################
利用树莓派3B来读取多路pwm波,误差约正负10us左右，pwm波的来源是深圳市天地飞公司生产的12位九通道接收机，然而我只需要读取六个通道所以就只写了六个通道的了。(Python 2.7.13)
这个程序需要用到一个叫做pigpio的python库函数，我未能找到很多关于这个库函数的中文资料（以前勉强能找到一个中文教程，现在突然找不到了，以后找到了再补充在这里）
在你安装了这个库函数之后，使用之前记得要先让程序运行，即输入
sudo pigpiod


pigpio这个库函数在pwm方面非常好用，尤其是提供python接口使得这个库函数的学习成本极低，但是这个库函数的中文资料极少(我唯一能在网络上找到的中文资料是关于C语言的)，同时github上也比较难找到这个库在这个方面的应用所以我根据找来的资料写了一个pwm解析程序（主要是根据我在https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=63509处找到的代码，你们可以在Joan's code看到这些代码），希望看到这个的中国学习者能少走一些弯路
