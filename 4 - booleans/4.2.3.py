temperature = input("Insert the temperature you would like to convert: ").upper()
if(temperature[-1] == 'F'):
    temperature = temperature.replace("F","")
    temperature = (float(temperature) * 5 - 160)/9
    temperature = str(temperature) + "C"
elif(temperature[-1] == 'C'):
    temperature = temperature.replace("C","")
    temperature = (float(temperature) * 9 + 32*5)/5
    temperature = str(temperature) + "F"
print(temperature)