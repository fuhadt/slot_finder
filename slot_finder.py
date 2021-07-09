import pandas as pd


URL_1 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=302&date=28-06-2021'
URL_2 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=302&date=29-06-2021'

pin = [676306, 676305, 676501]

def pincode_find(n):
  
  length = len(center)
  for i in range(length):
    if center[i]['pincode']==n:
      if center[i]['sessions'][0]['available_capacity']>0:
        message = 'Place: {}\nCapacity: {}\nDose_1: {}\nDose_2: {}\nType: {}\nDate: {}'.format(center[i]['name'], center[i]['sessions'][0]['available_capacity'], center[i]['sessions'][0]['available_capacity_dose1'], center[i]['sessions'][0]['available_capacity_dose2'], center[i]['sessions'][0]['vaccine'],  center[i]['sessions'][0]['date'])
        return message


df = pd.read_json(URL_1)
  center = df['centers']
  for i in pin:
    status = pincode_find(i)
    if status != None:
      print(status)
df = pd.read_json(URL_2)
  center = df['centers']
  for i in pin:
    status = pincode_find(i)
    if status != None:
      print(status)