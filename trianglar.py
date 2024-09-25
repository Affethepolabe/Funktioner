while True:
        try:
            n = int(input("Udda positivt tal: "))
            if n > 0 and n % 2 == 1:
                break
            else:
                print("ett udda!")
        except ValueError:
            print("inte ett heltal!")



def rTriangle(n):
    print("Rätvinklig: \n")
    for i in range(n):
        print(" " * i + "*" * (n - i))

def lTriangle(n):
    print("Likbent: \n")
    for i in range(n//2 + 1):
        print(" " * ((n//2) - i) + "*" * (2 * i + 1))

print("-"*(n+5))
print("-"*(n+5))
rTriangle(n)
print("-"*(n+5))
print("-"*(n+5))
lTriangle(n)
print("-"*(n+5))
print("-"*(n+5))

