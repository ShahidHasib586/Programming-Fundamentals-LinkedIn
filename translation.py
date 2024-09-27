import matplotlib.pyplot as plt

def main():
    # Initialize a new plotting window
    plt.figure(figsize=(10, 10))
    # Initialize 3D capabilities
    axes = plt.axes(projection="3d")
    
    # Setting axis properties
    axes.set_xlim(-10, 10)  # X Axis graduation
    axes.set_ylim(-10, 10)  # Y Axis graduation
    axes.set_zlim(-10, 10)  # Z Axis graduation
    axes.set_xlabel('X')  # X Axis label
    axes.set_ylabel('Y')  # Y Axis label
    axes.set_zlabel('Z')  # Z Axis label
    axes.xaxis.label.set_color('red')    # X Axis label color
    axes.yaxis.label.set_color('green')  # Y Axis label color
    axes.zaxis.label.set_color('blue')   # Z Axis label color
    axes.tick_params(axis='x', colors='red')    # X Axis graduation color
    axes.tick_params(axis='y', colors='green')  # Y Axis graduation color
    axes.tick_params(axis='z', colors='blue')   # Z Axis graduation color
    
    # Draw X axis (red)
    axes.plot([0, 10], [0, 0], [0, 0], color='red', linestyle='solid')   # + X axis
    axes.plot([0, -10], [0, 0], [0, 0], color='red', linestyle='dashed') # - X axis

    # Draw Y axis (green)
    axes.plot([0, 0], [0, 10], [0, 0], color='green', linestyle='solid')   # + Y axis
    axes.plot([0, 0], [0, -10], [0, 0], color='green', linestyle='dashed') # - Y axis

    # Draw Z axis (blue)
    axes.plot([0, 0], [0, 0], [0, 10], color='blue', linestyle='solid')   # + Z axis
    axes.plot([0, 0], [0, 0], [0, -10], color='blue', linestyle='dashed') # - Z axis
    
    # Draw the origin point
    axes.plot([0], [0], [0], marker='o', color='black')  # Origin point (0, 0, 0)
    
    # Draw the origin point
    axes.plot([0], [1], [2], marker='+', color='yellow')  # Origin point (0, 0, 0)
    
    # Draw the original point
    original_point = (4.0, 3.0, 2.0)
    axes.plot([original_point[0]], [original_point[1]], [original_point[2]], marker='x', color='green', label='Original Point')
    
    # Draw the translated point
    translation_vector = (0.0, 1.0, 1.0)
    translated_point = translate_point(original_point, *translation_vector)
    axes.plot([translated_point[0]], [translated_point[1]], [translated_point[2]], marker='x', color='blue', label='Translated Point')

    # Add legend to identify points
    axes.legend()

    # Display the 3D plotting window
    plt.show()

def translate_point(point, alpha, beta, gamma):
    x, y, z = point
    return (x + alpha, y + beta, z + gamma)

# Test the translate_point function
original_point = (4.0, 3.0, 2.0)
translation_vector = (0.0, 1.0, 1.0)
translated_point = translate_point(original_point, *translation_vector)

print(f"Original Point: {original_point}")
print(f"Translation Vector: {translation_vector}")
print(f"Translated Point: {translated_point}")

if __name__ == "__main__":
    main()
