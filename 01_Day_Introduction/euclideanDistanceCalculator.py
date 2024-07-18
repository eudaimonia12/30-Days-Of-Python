import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
def main():
    print("Euclidean Distance Calculator")
    print("-----------------------------")
    
    # Get input from the user
    x1 = float(input("Enter x-coordinate of the first point: "))
    y1 = float(input("Enter y-coordinate of the first point: "))
    x2 = float(input("Enter x-coordinate of the second point: "))
    y2 = float(input("Enter y-coordinate of the second point: "))
    
    # Calculate the distance
    distance = euclidean_distance(x1, y1, x2, y2)
    m=slope(x1,y1,x2,y2)
    
    # Print the result
    print(f"\nThe Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
    print (f'\n The slope between ({x1}, {y1}) and ({x2}, {y2}) is: {m:.2f}')

if __name__ == "__main__":
    main()