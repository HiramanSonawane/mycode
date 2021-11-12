#!/usr/bin/env python3
"""Space Details | Author: Hiraman Sonawane

   Description:
   A script to interact with an "open" api,
   http://api.open-notify.org/iss-now.json

   Documentation fr the API is available via,
   http://open-notify.org/Open-Notify-API/ISS-Location-Now/"""

from __future__ import print_function
import time
import requests

# Base API String
API = "http://api.open-notify.org/iss-now.json"
LOCATION_MSG = "CURRENT LOCATION OF THE ISS:"

def display_iss_location_detasils(iss_position, readable_time):
    """
       Displays iss Location details

    """
    print(LOCATION_MSG)
    print("TimeStamp: ", readable_time)
    print("   Lon: ", iss_position['longitude'])
    print("   Lat: ", iss_position['latitude'])

def main():
    """Executes Core code to fetch ISS details"""

    # Create a response
    iss_response = requests.get(API)

    # segregate values
    iss_timestamp = iss_response.json()['timestamp']
    iss_position = iss_response.json()['iss_position']

    #Convert timestamp into human readable format
    readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(iss_timestamp))

    # Display the Location
    display_iss_location_detasils(iss_position, readable_time)

if __name__ == "__main__":
    main()
