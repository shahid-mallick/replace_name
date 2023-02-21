
N = int(input("Enter the number to find Nth Harmonic number "))

h1 = 1

for i in range(2,N+1):
    h1 = h1 + 1/i # h1 = 1 + 1/2 + 1/3
    
print(h1)