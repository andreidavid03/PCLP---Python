from mindstorms import MSHub, Motor, MotorPair, ColorSensor

from mindstorms.control import wait_for_seconds

hub = MSHub()
motor_pair = MotorPair('B', 'A')
pen_motor = Motor('C')


motor_pair.set_default_speed(35)
pen_motor.run_to_position(165, 'shortest path')

color_sensor = ColorSensor('E')


def citeste_pozitie ():
    culori = ['blue', 'red', 'green']

    rand = None
    coloana = None

    while True:
        rand = color_sensor.get_color()
        if rand in culori:
            #print ("Rand = ", rand)
            break
    wait_for_seconds(3)
    while True:
        coloana = color_sensor.get_color()
        if coloana in culori:
            #print ("Coloana  =", coloana)
            break
    wait_for_seconds(3)
    
    return [culori.index(rand)+1, culori.index(coloana)+1]

while True:
    print (citeste_pozitie())



 
 
