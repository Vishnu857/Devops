print("Hello world")
import os

Choice = os.getenv("Choice")
parameter = os.getenv("parameter")
if (Choice=="Run" and parameter=="start"):
  print("running")
elif ((Choice == "Stop" and parameter == "start" )or(Choice == "Run" and parameter == "Stop")  ):
  print("stopping with error")
  raise Exception("Something went wrong")
else:
  print ("stopped officially")
print(f"Build triggered by: /n Choice:{Choice} parameter:{parameter}")
