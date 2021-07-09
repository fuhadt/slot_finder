import pandas as pd
from datetime import datetime, timedelta
from time import time, sleep


present_day = datetime.now()
present_day_formatted = present_day.strftime('%d-%m-%Y')
next_day = present_day + timedelta(1)
next_day_formatted = next_day.strftime('%d-%m-%Y')

URL_1 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=302&date='+present_day_formatted
URL_2 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=302&date='+next_day_formatted

pin = [676306, 676305, 676501]

def pincode_find(n):
  
  length = len(center)
  for i in range(length):
    if center[i]['pincode']==n:
      if center[i]['sessions'][0]['available_capacity']>0:
        message = 'Place: {}\nCapacity: {}\nDose_1: {}\nDose_2: {}\nType: {}\nDate: {}'.format(center[i]['name'], center[i]['sessions'][0]['available_capacity'], center[i]['sessions'][0]['available_capacity_dose1'], center[i]['sessions'][0]['available_capacity_dose2'], center[i]['sessions'][0]['vaccine'],  center[i]['sessions'][0]['date'])
        return message


while True:
    sleep(30 - time() % 30)
    df = pd.read_json(URL_1)
    center = df['centers']
    for i in pin:
        status = pincode_find(i, center)
        if status != None:
            print(status)
    sleep(30 - time() % 30)
    df = pd.read_json(URL_2)
    center = df['centers']
    for i in pin:
        status = pincode_find(i, center)
        if status != None:
            print(status)