# Import random module to use the random method => generates numbers between 0 and 1
# Import datetime to include date and time stamp on the randomly generated numbers
import datetime

import random as rand

# Create a list to hold all the generated sensor data
global sensor
sensor=1
sensorReading32=[]
# Open a file to hold the generated data from each sensor
report = open("SensorData.txt", "w")
# Loop for 32 arrays of sensors
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
# Write the generated sensor data to the initially opened
    report.write('Readings for sensor {}'.format(sensor) + str(sensorData)+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    report.write("\n")


    sensor=sensor+1


# Write a function to generate new data from the sensors
# The function will identify errors in the generated data
# The error is defined by a threshold value called errorvalue below which the function will report error
def checkerror(errorvalue):
    import random as rand
    import datetime

    global sensorerror

    sensorerror = 1
    sensorerrordata32 = []
    # open files to hold the sensors data with string errors
    errorReport = open("SensorsData2.txt", "w")
    newerrorreport = open('CorruptedSensorData.txt', 'w')
    logreport=open('Error_Log_Report.txt', 'w+')

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
        for item in sensorerrordata:
            if item < errorvalue:
                item = 'err'
            errordata.append(item)
        sensorerrordata = errordata

        print(sensorerrordata)

        if "err" in sensorerrordata:
            print("Error Data found in sensor {}".format(sensorerror), file=logreport)
        else:
            print("No error in sensor {}".format(sensorerror), file=logreport)

        newerrorreport.write(
            "Reading Errors from sensor {}".format(sensorerror) + str(sensorerrordata) + str(datetime.datetime.now()))
        newerrorreport.write("\n")
        newerrorreport.write("\n")



        sensorerror = sensorerror + 1

# The sensor will print string error whenever a value less than 0.01 if generated
# Call the function
checkerror(0.01)

