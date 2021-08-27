def series(x= -1, y= -1):
    
    series = [7, 6, 8, 4, 9, 2, 10, 0, 11, -2]

    if x <= 0 or y <= 0 or x > 255 or y > 255:
        return -1

    return (series[x-1] + series[y-1])

x = input("numbers: ")
y = input("numbers: ")

print(series(int(x), int(y)))