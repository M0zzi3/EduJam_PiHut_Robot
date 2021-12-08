import RPi.GPIO as GPIO
import time


class Motor:

    def __init__(self, pin_motor_forwards, pin_motor_backwards):
        self.pin_forward = pin_motor_forwards
        self.pin_backward = pin_motor_backwards
        self.frequency = 20
        self.stop = 0

        GPIO.setup(self.pin_forward, GPIO.OUT)
        GPIO.setup(self.pin_backward, GPIO.OUT)

        self.pwm_motor_forward = GPIO.PWM(self.pin_forward, self.frequency)
        self.pwm_motor_backward = GPIO.PWM(self.pin_backward, self.frequency)

        self.pwm_motor_forward.start(self.stop)
        self.pwm_motor_backward.start(self.stop)

        print("Motor initialised on pins : " + str(self.pin_forward) + " " + str(self.pin_backward))

    def stop_motor(self):
        self.pwm_motor_forward.ChangeDutyCycle(self.stop)
        self.pwm_motor_backward.ChangeDutyCycle(self.stop)

    def forward(self,speed):
        self.pwm_motor_forward.ChangeDutyCycle(speed)
        self.pwm_motor_backward.ChangeDutyCycle(self.stop)

    def backward(self,speed):
        self.pwm_motor_forward.ChangeDutyCycle(self.stop)
        self.pwm_motor_backward.ChangeDutyCycle(speed)


class Robot:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        print("test")
        print("test2")
        self.motor1 = Motor(7,8)
        self.motor2 = Motor(9,10)

        self.color_sensor = 25
        GPIO.setup(self.color_sensor, GPIO.IN)

        self.pinTrigger = 17
        self.pinEcho = 18
        GPIO.setup(self.pinTrigger, GPIO.OUT)
        GPIO.setup(self.pinEcho, GPIO.IN)



    def go_forward(self):
        self.motor1.forward(20)
        self.motor2.forward(70)

    def go_backward(self):
        self.motor1.backward(30)
        self.motor2.backward(50)

    def stop(self):
        self.motor1.stop_motor()
        self.motor2.stop_motor()



    def check_color(self):
        if GPIO.input(self.color_sensor) == 0:
            return "black"
        else:
            return "white"


    def check_distance(self):
        global stop_time
        GPIO.output(self.pinTrigger, False)

        time.sleep(0.5)

        GPIO.output(self.pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(self.pinTrigger, False)

        start_time = time.time()

        while GPIO.input(self.pinEcho) == 0:
            start_time = time.time()

        while GPIO.input(self.pinEcho) == 1:
            stop_time = time.time()

            if stop_time-start_time >= 0.04:
                print("Object to close")
                stop_time = start_time
                break


        distance = ((stop_time - start_time) * 34326)/2

        return distance







    def execute(self, comand):
        if comand == "W":
            self.go_forward()

        if comand == "S":
            self.go_backward()

        if comand == "stop":
            self.stop()

        if comand == "Color":
            print("Color that sensor sees : "+ self.check_color())

        if comand == "Distance":
            print("Distance : "+ str(self.check_distance()) +"cm")


