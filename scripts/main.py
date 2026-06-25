print("Hello world")
import os

Choice = os.getenv("Choice")

if (choice=="Run"):
  print("running")
else:
  print("stopped")
print(f"Build triggered by: {Choice}")
