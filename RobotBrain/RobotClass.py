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

    def forward(self, speed):
        self.pwm_motor_forward.ChangeDutyCycle(speed)
        self.pwm_motor_backward.ChangeDutyCycle(self.stop)

    def backward(self, speed):
        self.pwm_motor_forward.ChangeDutyCycle(self.stop)
        self.pwm_motor_backward.ChangeDutyCycle(speed)


class Robot:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.motor1 = Motor(7, 8)
        self.motor2 = Motor(9, 10)
        self.gears = [20, 40, 60, 80,100]
        self.g = 0

        self.color_sensor = 25
        GPIO.setup(self.color_sensor, GPIO.IN)

        self.pinTrigger = 17
        self.pinEcho = 18
        GPIO.setup(self.pinTrigger, GPIO.OUT)
        GPIO.setup(self.pinEcho, GPIO.IN)

        self.manual_commands = {
            'forward': self.go_forward,
            'backward': self.go_backward,
            'color': self.check_color,
            'distance': self.check_distance,
            'stop': self.stop,
            'gear_up': self.gear_up,
            'gear_down': self.gear_down,
            'right': self.turn_right,
            'left': self.turn_left
        }

    def go_forward(self):
        self.motor1.forward(self.gears[self.g])
        self.motor2.forward(self.gears[self.g])

    def go_backward(self):
        self.motor1.backward(self.gears[self.g])
        self.motor2.backward(self.gears[self.g])

    def turn_right(self):
        self.motor2.forward(self.gears[self.g])
        self.motor1.backward(self.gears[self.g]-10)

    def turn_left(self):
        self.motor1.forward(self.gears[self.g])
        self.motor2.backward(self.gears[self.g]-10)

    def stop(self):
        self.motor1.stop_motor()
        self.motor2.stop_motor()

    def gear_up(self):
        if self.g < len(self.gears)-1:
            self.g += 1

            print('Gear set to : ' + str(self.g+1))

    def gear_down(self):
        if self.g > 0:
            self.g -= 1

            print('Gear set to : ' + str(self.g+1))

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

            if stop_time - start_time >= 0.04:
                print("Object to close")
                stop_time = start_time
                break

        distance = ((stop_time - start_time) * 34326) / 2

        return distance
