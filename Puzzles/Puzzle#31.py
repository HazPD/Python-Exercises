import math


def find_triangle_coordinates(sides):
    
    a, b, c = sides
    
    # Initialize an empty list to store the coordinates
    coordinates = []
    
    # Vertex A at (0, 0)
    A = [0.0, 0.0]
    coordinates.append(A)
    # Vertex B at (c, 0)
    B = [float(c), 0.0]
    coordinates.append(B)
    # Calculate x coordinate of vertex C
    x = (a**2 - b**2 + c**2) / (2 * c)
    # Calculate y coordinate of vertex C (positive value)
    y = math.sqrt(a**2 - x**2)
    
    # Coordinates of C
    C = [x, y]
    
    coordinates.append(C)
    
    return coordinates

# Example side lengths stored in a list
side_lengths = [4, 5, 6]

# Get the coordinates of the vertices
coordinates = find_triangle_coordinates(side_lengths)

# Print the results
print("The coordinates of the vertices are:")
print(coordinates)