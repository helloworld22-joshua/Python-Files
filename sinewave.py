import math
import time

amplitudeA = 30 #30
frequencyB = 16 #16
horzShiftH = 0  #0
vertShiftK = 35 #35

xAxisLimit = 100  #100
debugMode = False #False
delayInMs = 0.1   #0.1
symbol = "❌"     #Example symbols: ⬤, ×, •, ⭕, ⚫, ❌

for xAxis in range(xAxisLimit):
  yAxis = round(amplitudeA * math.sin(math.pi / frequencyB * (xAxis - horzShiftH)) + vertShiftK)  #"math.pi /" to make things easier

  if debugMode:
    print(xAxis, "|", yAxis, end=" ")

  if yAxis >= 0:
    print(" " * yAxis + symbol)
  else:
    print()

  time.sleep(delayInMs)