import math

def area_of_circle(radius):
    return (math.pi)*(radius**2)
def circum_of_circle(radius):
    return (math.pi)*(radius*2)
def main():
    print("Circle Calculator")
    print("-----------------------------")
    radius=float(input("Please enter the radius of a circle: "))
    area=int(area_of_circle(radius))
    circum=int(circum_of_circle(radius))
    print("Area:", area)
    print("Circumference:", circum)

if __name__ == "__main__":
    main()