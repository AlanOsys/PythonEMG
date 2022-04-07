import serial
import matplotlib.pyplot as plt
import keyboard  # using module keyboard
serial_port ='COM10'
baud_rate = 9600
counter = 1
f = open("data.txt", "a")
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline()
    line = line.decode("utf-8")
    line = ((int)(line[:2])/1023)*5
    
    print(line)
    line = (str)(line)
    counter+=1
    #if counter % 2 == 0:
    f.write(line)
    f.write('\n')
    
    
    if keyboard.is_pressed('q'):
        break

f.close()

#print(lines)


fr = open("data.txt", "r")
lines = fr.readlines()
plt.plot(lines)
plt.show()
fr.close()
