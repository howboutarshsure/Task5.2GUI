from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel
import sys
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # Red LED
GPIO.setup(13, GPIO.OUT)  # Blue LED
GPIO.setup(15, GPIO.OUT)  # Green LED

# Set up PWM for each LED pin
red_pwm = GPIO.PWM(11, 100)  # 100 Hz frequency
blue_pwm = GPIO.PWM(13, 100)
green_pwm = GPIO.PWM(15, 100)

# Start PWM with 0% duty cycle
red_pwm.start(0)
blue_pwm.start(0)
green_pwm.start(0)

def set_intensity(color, value):
    if color == "red":
        red_pwm.ChangeDutyCycle(value)
    elif color == "blue":
        blue_pwm.ChangeDutyCycle(value)
    elif color == "green":
        green_pwm.ChangeDutyCycle(value)

def ALL_OFF():
    red_pwm.ChangeDutyCycle(0)
    blue_pwm.ChangeDutyCycle(0)
    green_pwm.ChangeDutyCycle(0)

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 350, 300)
    win.setWindowTitle("LED Controller with GUI")

    red_slider = QSlider(QtCore.Qt.Horizontal, win)
    red_slider.setObjectName("red_slider")
    red_slider.setGeometry(100, 50, 150, 20)
    red_slider.setMinimum(0)
    red_slider.setMaximum(100)
    red_slider.valueChanged.connect(lambda value: set_intensity("red", value))

    red_label = QLabel("Red", win)
    red_label.setGeometry(20, 50, 70, 20)

    blue_slider = QSlider(QtCore.Qt.Horizontal, win)
    blue_slider.setObjectName("blue_slider")
    blue_slider.setGeometry(100, 100, 150, 20)
    blue_slider.setMinimum(0)
    blue_slider.setMaximum(100)
    blue_slider.valueChanged.connect(lambda value: set_intensity("blue", value))

    blue_label = QLabel("Blue", win)
    blue_label.setGeometry(20, 100, 70, 20)

    green_slider = QSlider(QtCore.Qt.Horizontal, win)
    green_slider.setObjectName("green_slider")
    green_slider.setGeometry(100, 150, 150, 20)
    green_slider.setMinimum(0)
    green_slider.setMaximum(100)
    green_slider.valueChanged.connect(lambda value: set_intensity("green", value))

    green_label = QLabel("Green", win)
    green_label.setGeometry(20, 150, 70, 20)

    win.show()
    win.closeEvent = lambda event: ALL_OFF()
    sys.exit(app.exec_())

window()
