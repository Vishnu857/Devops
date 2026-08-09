print("Hello world")
import os

Choice = os.getenv("Choice")
parameter = os.getenv("parameter")
if (Choice=="Run" & parameter=="start"):
  print("running")
elif (Choice == "stop" & parameter == "start" ):
  print("stopping with error")
  raise Exception("Something went wrong")
else:
  print ("stopped officially")
print(f"Build triggered by: /n Choice:{Choice} parameter:{parameter}")
