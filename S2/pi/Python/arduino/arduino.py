import serial
from serial import Serial


def read_data_from_arduino():
    #configuration for acessing arduino COM3 9600
    portName = "COM3"
    ser = serial.Serial(portName, 9600, timeout=2)
    #ser.flush()
    #ser.read_until()
    #for i in range(1,13):
    #    data = ser.readline()
    #    print(data)
    data = ser.readline()
    f = open("arduino_read.txt", "wb")
    f.write(data)
    f.close()


if __name__ == '__main__':
    read_data_from_arduino()