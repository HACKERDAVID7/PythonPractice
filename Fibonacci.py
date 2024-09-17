# Odd Even


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    f = 0
    s = 1
    print(f,s, end=" ")
    for i in range(2, n):
        t = f+s
        print(t, end=" ")
        f = s 
        s = t