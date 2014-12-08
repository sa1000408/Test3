import time
start_time = time.time()

userVariable = raw_input("Geben Sie bitte eine Zahl ein:")
numBerechnung = float(userVariable)*float(userVariable)
print numBerechnung

print("--- %s seconds ---" % (time.time() - start_time))