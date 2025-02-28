import csv
import copy

myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Imprimir valores iniciales del vehículo
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

myInventoryList = []  # Lista de inventario de vehículos

# Abrir archivo CSV y leer los datos
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0  

    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            
            # Copiar la estructura base del diccionario
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = int(row[3])  
            currentVehicle["range"] = int(row[4])  
            currentVehicle["topSpeed"] = int(row[5])  
            currentVehicle["zeroSixty"] = float(row[6])  
            currentVehicle["mileage"] = int(row[7])  

            myInventoryList.append(currentVehicle)  
            lineCount += 1  

    print(f'Processed {lineCount} lines.')

# Imprimir inventario de vehículos
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")
