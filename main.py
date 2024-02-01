import wikipedia
import pyjokes
import datetime

while True:
  n = input("Chat>>>")
  if n == "hello":
    print("Hello, I am J.A.R.V.I.S chatbot, how can I help you?")
  elif n == "who are you":
    print(" I am J.A.R.V.I.S chatbot...")
  elif n == "tell me joke":
    print(pyjokes.get_joke())
  elif n == "what is time now":
    print(datetime.datetime.now())
  else:
    print(wikipedia.summary(n))
