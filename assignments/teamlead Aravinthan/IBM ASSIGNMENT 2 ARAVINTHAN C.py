import random
import time

while(1):
    temperature = round(random.randint(0,90))
    humidity = round(random.randint(0,90))

    if temperature <15:
        print("Temperature is very low.Current Temperture = ",temperature,"% C")
    elif temperature >= 15 & temperature <= 30:
        print("Temperature is normal.Current Temperture = ",temperature,"% C")
    else:
        print("Temperature is too High.Current Temperture = ",temperature,"% C")


    if humidity < 30:
        print("Humidity is very low.Current Humidity = ",humidity,"% C")
    elif humidity >= 15 & humidity <= 30:
        print("Humidity is normal.Current Humidity = ",humidity,"% C")
    else:
        print("Humidity is too High.Current Humidity = ",humidity,"% C")

    print()
    print("**************************************************************************")
    print()
    time.sleep(5)




