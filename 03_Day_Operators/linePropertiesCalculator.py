def calculate_line_properties(m, b):
    """
    Calculate properties of the line y = mx + b
    :param m: slope of the line
    :param b: y-intercept of the line
    :return: tuple of (slope, x-intercept, y-intercept)
    """
    slope = m
    y_intercept = b
    
    # Calculate x-intercept
    # At x-intercept, y = 0, so: 0 = mx + b
    # Solving for x: x = -b/m
    if m != 0:
        x_intercept = -b / m
    else:
        x_intercept = None  # Line is horizontal, no x-intercept

    return slope, x_intercept, y_intercept

def main():
    print("Properties of the line y = 2x - 2")
    print("----------------------------------")

    # Given equation: y = 2x - 2
    m = 2  # slope
    b = -2  # y-intercept

    slope, x_intercept, y_intercept = calculate_line_properties(m, b)

    print(f"Slope: {slope}")
    print(f"X-intercept: {x_intercept}")
    print(f"Y-intercept: {y_intercept}")

if __name__ == "__main__":
    main()