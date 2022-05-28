import requests  # http library for python, good for HTTP requests (purpleair in this case)



# BOUNDING BOX COORDINATES OF WALNUT CREEK: -122.1112824826,37.8578571822,-122.0120455888,37.9347574986
# sensor IDs near me (closer-farther): 85561, 69049, 68631, 75579, 19581, 63269, 85823
def get_new_link(sensor_id):
    url_frame = 'https://www.purpleair.com/json?show='
    new_url = url_frame + sensor_id.strip()  # use .strip() just in case user adds a space before their input
    return new_url

headers = {
    'X-API-KEY': 'D0AC0323-3A55-11EB-9893-42010A8001E8'
}
r = requests.get('https://api.purpleair.com/v1/sensors?fields=pm2.5&location_type=0&nwlng=37.8578571822&nwlat=-122'
                 '.1112824826&selng=37.9347574986&selat=-122.0120455888', headers=headers)
response = r.json()   #    ^^ bounding box coordinates for Walnut Creek
#print(response)


def get_data(data_type):
    url = get_new_link(sensorId)  # call on get_new_link to get the new url used for requests.get()
    r = requests.get(url)  # request data from PurpleAir sensor widget
    response = r.json()  # format received data into .json type, (key: keyvalues)
    sensor_name = (response['results'][0]['Label'])  # gather name of sensor (string value)
    if data_type == 1:
        print("Gathering pm2.5 data...")
        pm2_5 = (response['results'][1]['PM2_5Value'])  # access nested JSON key 'PM2_5Value' nested in 'results' key
        print("The PM2_5 value for the " + sensor_name + " sensor is currently: " + pm2_5)
        if float(pm2_5) < 0:  # conditionals for air quality
            print("Error, the PM2.5 is a negative number.")
        elif float(pm2_5) < 12.0:
            print("The air quality poses little to no risk.")
        elif 12.0 < float(pm2_5) < 35.4:
            print(
                "Unusually sensitive individuals may experience respiratory symptoms; unusually sensitive people "
                "should "
                "consider reducing prolonged or heavy exertion.")
        elif 35.4 < float(pm2_5) < 55.4:
            print("People with respiratory or heart disease, the elderly and children should limit prolonged exertion.")
        elif 55.4 < float(pm2_5) < 150.4:
            print("People with respiratory or heart disease, the elderly and children should "
                  "avoid prolonged exertion; everyone else should limit prolonged exertion.")
        elif 150.4 < float(pm2_5) < 250.4:
            print("People with respiratory or heart disease, the elderly and children "
                  "should avoid any outdoor activity; everyone else should avoid prolonged exertion.")
        elif 250.5 < float(pm2_5) < 500.4:
            print("Stay inside...")
    elif data_type == 2:
        print("Gathering humidity data...")
        humidity = (response['results'][0]['humidity'])  # pull humidity data from sensor
        print("The humidity for the " + sensor_name + " sensor is " + humidity + "%")
    elif data_type == 3:
        print("Gathering temperature data...")
        temperature = (response['results'][0]['temp_f'])
        print("The temperature for the " + sensor_name + " in fahrenheit is " + temperature)
    elif data_type == 4:
        print("Gathering pressure data...")
        pressure = (response['results'][0]['pressure'])
        print("The air pressure for the" + sensor_name + " is " + pressure + "mb")
    elif data_type <= 0 or data_type >= 4:
        print("Invalid dataType number...")


yes_or_no = input('Would you like to view the data of a PurpleAir sensor?')
yes_or_no = yes_or_no.lower()

while yes_or_no == 'y' or yes_or_no == 'yes':  # loop that allows user to view data of another sensor
    print("Sensor IDs near me (closer-farther): 85561, 69049, 68631, 75579, 19581, 63269, 85823")
    sensorId = input('Please enter the sensor id number:')  # request user to input sensor ID
    get_new_link(sensorId)  # call on get_new_link method to create the new link that will be used
    #                         to request json() data
    print(
        "Your new purpleair sensor URL is: " + get_new_link(sensorId))  # show user their new URL
    dataType = int(input("Which piece of data would you like to view? pm2.5 (1), humidity (2), temperature (3), "
                         + "or pressure (4): "))  # ask user which type of data they would like to view
    get_data(dataType)
    yes_or_no = input('Would you like to view the data of another PurpleAir sensor?').lower()


# ideas:
# include name of sensor when printing data piece
# ask user if they would like avg of specific data values for all sensors in Walnut Creek
# ex: avg of humidity values for all sensors/monitors in walnut creek
#
# ask user if they would like to see other types of data from the same sensor
#

