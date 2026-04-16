import math

# Prompt user for vector components
x = float(input("Enter the x component of the vector: "))
y = float(input("Enter the y component of the vector: "))

# Calculate magnitude
magnitude = math.sqrt(x**2 + y**2)

# Display the components and magnitude
print(f"Vector components: x = {x}, y = {y}")
print(f"Magnitude of the vector: {magnitude}")

# Calculate and display the unit vector if magnitude is not zero
if magnitude != 0:
    unit_vector_x = x / magnitude
    unit_vector_y = y / magnitude
    print(f"Unit vector: ({unit_vector_x}, {unit_vector_y})")
else:
    print("Magnitude is zero, cannot compute the unit vector."),
