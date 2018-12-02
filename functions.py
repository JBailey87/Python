#Abs function to return the abaolsute number
print ('the absolute value is:', abs(-21.54))

cars =  ["Ford", "Volvo", "BMW"]

carsIterable = iter(cars)

#print(next(carsIterable))
#print(next(carsIterable))
#print(next(carsIterable))

def printAll(iterable):
	while True:
		try:
			item = next(iterable)
		except StopIteration:
			print("End of List")
			break
		else:
			print(item)

printAll(carsIterable)
