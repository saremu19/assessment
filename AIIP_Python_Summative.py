# Import random module to use the random method => generates numbers between 0 and 1
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

    report.write('Readings for sensor {}'.format(sensor) + str(sensorData))
    report.write("\n")


    sensor=sensor+1



def checkerror(errorthreshold):
    import random as rand

    sensorerror = 1

    while sensorerror <= 32:
        sensorerrorData = []
        for j in range(16):
            sensorerrorDatanumber = rand.random()
            #if sensorerrorDatanumber(j) > errorthreshold:
                #sensorerrorDatanumber[reading] = 'err'
            sensorerrorData.append(sensorerrorDatanumber)

            print(sensorerrorData)

        errorReport = open("SensorError1.txt", "w")
        errorReport.write("Reading with error from sensor {}".format(sensorerror) + str(sensorerrorData))
        errorReport.write("\n")

        sensorerror = sensorerror + 1


checkerror(float(0.5000000))