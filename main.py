import pandas as pd
import pywhatkit as kit

data = pd.read_csv('number.csv',dtype = 'string')
for i, row in data.iterrows():
   print(f"Sendingmessage to {row['Name']} at {row['Number']}")
   message = open("message.txt").read()
   message = message.replace("{name}", row['Name'])
   
   
   
   kit.sendwhatmsg_instantly(phone_no = str(row["Number"]), message = message, tab_close = True, wait_time = 2, close_time = 2, browser = "chrome")
   
   #to send on specific time use kit.sendwhatmes(...)
   
   
