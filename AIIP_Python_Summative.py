# Import random module to use the random method => generates numbers between 0 and 1
from random import randrange
import datetime

import random as rand

# Create a list to hold all the generated sensor data
global sensor
sensor=1
sensorReading32=[]

report = open("sensorfile.txt", "w")

while sensor<=32:

    sensorData = []

# Generate a list of 16 random numbers using a for loop
    for i in range(16):
        # Create a variable to hold each number generated
            sensorDataNumber = rand.random()
        # Append that number to the sensorData list
            sensorData.append(sensorDataNumber)

            print(sensorData)
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    report.write('Readings for sensor {}'.format(sensor) + str(sensorData)+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    report.write("\n")


    sensor=sensor+1



def checkerror(errorvalue):
    import random as rand
    import datetime

    global sensorerror

    sensorerror = 1
    sensorerrordata32 = []

    errorReport = open("SensorError2.txt", "w")
    newerrorreport = open('Errorreadings2.txt', 'w')

    while sensorerror <= 32:

        sensorerrordata = []

        for j in range(16):
            sensorerrordatanumber = rand.random()

            sensorerrordata.append(sensorerrordatanumber)

            print(sensorerrordata)
            # print("\n")

        errorReport.write("Reading with error from sensor {}".format(sensorerror) + str(sensorerrordata) + str(
            datetime.datetime.now()))
        errorReport.write("\n")
        errorReport.write("\n")

        errordata = []
        for erroritem in sensorerrordata:
            if erroritem < errorvalue:
                erroritem = 'SenError'
            errordata.append(erroritem)
        sensorerrordata = errordata

        newerrorreport.write(
            "Reading Errors from sensor {}".format(sensorerror) + str(sensorerrordata) + str(datetime.datetime.now()))
        newerrorreport.write("\n")
        newerrorreport.write("\n")

        sensorerror = sensorerror + 1


checkerror(0.1)

