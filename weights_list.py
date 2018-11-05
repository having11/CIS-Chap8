weights = []
for i in range(4):
    weights.append(float(input("Enter weight "+str(i+1)+":\n")))
print("Weights:",weights)
print("\nAverage weight: %.2f\nMax weight: %.2f" % (sum(weights)/4,max(weights)))
location = int(input("\nEnter a list index (1 - 4):\n"))
location -=1
print("Weight in pounds: %.2f\nWeight in kilograms: %.2f"%(weights[location],weights[location]/2.2))
print("\nSorted list:",sorted(weights))
