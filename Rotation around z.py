import matplotlib.pyplot as plt
import numpy as np

def rot_z_point(point, kappa):
    
    x, y, z = point
    # Applying the rotation matrix for X-axis rotation
    xr = x * np.cos(kappa) - y * np.sin(kappa)
    yr = x * np.sin(kappa) + y * np.cos(kappa)
    zr = z 
    return (xr, yr, zr)

def main():
    # Initialize a new plotting window
    plt.figure(figsize=(10, 10))
    # Initialize 3D capabilities
    axes = plt.axes(projection="3d")
    
    # Setting axis properties
    axes.set_xlim(-10, 10)  # X Axis limits
    axes.set_ylim(-10, 10)  # Y Axis limits
    axes.set_zlim(-10, 10)  # Z Axis limits
    axes.set_xlabel('X')  # X Axis label
    axes.set_ylabel('Y')  # Y Axis label
    axes.set_zlabel('Z')  # Z Axis label
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
    #axes.plot([0], [0], [0], marker='o', color='black')  # Origin point (0, 0, 0)    
    # Draw the original point
    original_point = (4.0, 4.0, 4.0)
    axes.plot([original_point[0]], [original_point[1]], [original_point[2]], marker='o', color='black', label='Original Point')
    
    # Rotate the point around the z-axis by π/4
    kappa = np.pi / 4
    rotated_point = rot_z_point(original_point, kappa)
    axes.plot([rotated_point[0]], [rotated_point[1]], [rotated_point[2]], marker='o', color='blue', label='Rotated Point')
    
    # Add legend to identify points
    axes.legend()

    # Display the 3D plotting window
    plt.show()

if __name__ == "__main__":
    main()
