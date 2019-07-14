import boto3
import time
import json
import datetime
from random import randint




print "*************************************"

print "Activating turbines...\n"
print " "
time.sleep(1)
print "Starting to sent telemetry  to Kinesis Firehose...\n"
print "*************************************"

firehose_client=boto3.client('firehose', region_name='us-east-1') #Select the correct region 

anomaly_counter = 0
while True:
    time.sleep (1)
    #global control
    anomaly_counter = anomaly_counter+1
    #randomly generating data....
    timestamp = str (datetime.datetime.now())
    turbine_id = randint(1,10)
    wind_speed = randint(55,85)
    RPM_blade = randint(60,85)
    oil_temperature = randint(20,50)
    oil_level = randint(1,25)
    vibration_frequency = randint(2,15)
    pressure = randint(30,85)
    wind_direction = randint(1,8)    

    temp = randint(50,85)
    humid = randint(50,70)

    if anomaly_counter == 80:
        turbine_id = 1
        wind_speed = 1
        RPM_blade = 1
        oil_temperature = 1
        oil_level = 1
        vibration_frequency = 1
        pressure = 1
        wind_direction = 1   

        temp = 1
        humid = 1
        anomaly_counter = 0


    location = str(randint(1,100))
    print "Counter: " + str(anomaly_counter)
    #randomly generate geo_location
    geo_location = '51.70015' + location + ', -0.5997986'
    print "----------------------------------------------------------------------------------------------------------------"
    #print "Time: " + timestamp + " wind_speed: " + str(wind_speed) + " RPM_blade: " + str(RPM_blade) + " oil_temperature: " + str(oil_temperature) + " oil_level: " + str(oil_level) + " vibration_frequency: " + str(vibration_frequency) + " pressure: " + str(pressure) + " wind_direction: " + str(wind_direction) + " temperature: " + str(temperature) 

 

    jpayload = {}

    #prepare json payload 
    jpayload ['timestamp'] = timestamp
    jpayload ['geo_location'] = geo_location
    jpayload ['turbine_id'] = int(turbine_id)
    jpayload ['wind_speed'] = int(wind_speed)
    jpayload ['RPM_blade'] = int(RPM_blade)
    jpayload ['oil_temperature'] = int(oil_temperature)
    jpayload ['oil_level'] = int(oil_level)
    jpayload ['temperature'] = int(temp)
    jpayload ['humidity'] = int(humid)
    jpayload ['vibration_frequency'] = int(vibration_frequency)
    jpayload ['pressure'] = int(pressure)
    jpayload ['wind_direction'] = int(wind_direction)
                

    json_data = json.dumps(jpayload)+"\n";

    print json_data
    print "\n" 



    response = firehose_client.put_record(
        DeliveryStreamName='<<Enter your Firehose Stream Name here>>',
        Record={'Data' : json_data}
    )


    metadata = response['ResponseMetadata'] 
    HTTPCode = metadata['HTTPStatusCode']
    if HTTPCode == 200:
        print "Successfully updated record: " + str(HTTPCode)
    else:
        print "Failure" + str(HTTPCode) 
        os.system('echo failues > failed')


       
 
        
