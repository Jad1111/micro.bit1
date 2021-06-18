rom microbit import *
import music
#music.play(music.BIRTHDAY)

arr_right = Image("00000:00090:00099:00090:00000")
arr_up = Image("00900:09990:00000:00000:00000")
arr_left = Image("00000:09000:99000:09000:00000")
arr_down = Image("00000:00000:00000:09990:00900")
level=Image("00000:00900:09990:00900:00000")


while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    if x > y and x > (-y) and x > 20:
            display.show(arr_right)
    elif y > x and y > (-x) and y > 20:
        display.show(arr_down)
    elif x < y and x < (-y) and x < -20:
        display.show(arr_left)
    elif y < x and y < (-x) and y < -20:
        display.show(arr_up)
    elif x > -20 and x < 20 and y > -20 and y < 20:
        display.show(level)
        
#while True:
#    if pin0.is_touched():
#        display.show(Image.HAPPY)
