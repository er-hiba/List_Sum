L1 = []
L2 = []
List = []

x = int(input("Enter the size of the 2 lists: "))

for i in range (0, x) :
    N1 = int(input(f"Enter the element {i+1} of the first list: "))
    L1.append(N1)
for i in range (0, x) :
    N2 = int(input(f"Enter the element {i+1} of the second list: "))
    L2.append(N2)

for i in range(0, x):
    List.append(L1[i] + L2[i])

print("Sum is", List)

