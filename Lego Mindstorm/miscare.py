from mindstorms import MSHub, Motor, MotorPair

hub = MSHub()
motor_pair = MotorPair('B', 'A')
pen_motor = Motor('C')

motor_pair.set_default_speed(15)
pen_motor.run_to_position(165, 'shortest path')

def desen_patrat():
    for _ in range(4):
        pen_motor.run_for_degrees(90)

        # This sets the length of the line.
        motor_pair.move(3, 'cm')       #modificam lungime
        pen_motor.run_for_degrees(-90)
        motor_pair.move(190, 'degrees')

        # This controls how much Tricky turns between each line.
        motor_pair.move(180, 'degrees', steering=-100)
        motor_pair.move(-190, 'degrees')


def desen_triunghi():
    for _ in range(3):
        pen_motor.run_for_degrees(90)

        # This sets the length of the line.
        motor_pair.move(3, 'cm')    #modificam lungime
        pen_motor.run_for_degrees(-90)
        motor_pair.move(190, 'degrees')

        # This controls how much Tricky turns between each line.
        motor_pair.move(240, 'degrees', steering=-100)
        motor_pair.move(-190, 'degrees')


def go_to(x,y):
    #presupun ca pleaca din centru (0,0)
    #x pozitiv in dreapta
    #y pozitiv in sus
    #robot pozitionat in sus
    motor_pair.move(y+8, 'cm')
    motor_pair.move(180, 'degrees', steering=-100)
    motor_pair.move(-1*(x+8), 'cm')
        
    



coordonate = {"11": (-7.5,10.5), "12": (1.5,10.5), "13": (10.5,10.5),
              "21": (-7.5,1.5),  "22": (1.5,1.5),  "23": (10.5,1.5),
              "31": (-7.5,-7.5), "32": (1.5,-7.5), "33": (10.5,-7.5)}


#pen_motor.run_for_degrees(90)
go_to(15,15)

#pen_motor.run_for_degrees(-90)
