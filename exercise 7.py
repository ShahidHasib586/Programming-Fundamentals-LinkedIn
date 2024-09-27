import matplotlib.pyplot as plt
from numpy import *

def rot_x_point(point, omega):
    x, y, z = point
    xr = x
    yr = y * cos(omega) - z * sin(omega)
    zr = y * sin(omega) + z * cos(omega)
    return (xr, yr, zr)

def rot_y_point(point, phi):
    x, y, z = point
    xr = x * cos(phi) + z * sin(phi)
    yr = y
    zr = -x * sin(phi) + z * cos(phi)
    return (xr, yr, zr)

def rot_z_point(point, kappa):
    x, y, z = point
    xr = x * cos(kappa) - y * sin(kappa)
    yr = x * sin(kappa) + y * cos(kappa)
    zr = z
    return (xr, yr, zr)

def rot_point(point, omega, phi, kappa):
    x, y, z = point
    xr = x * cos(phi) * cos(kappa) + y * (sin(omega) * sin(phi) * cos(kappa) - cos(omega) * sin(kappa)) + z * (cos(omega) * sin(phi) * cos(kappa) + sin(omega) * sin(kappa))
    yr = x * cos(phi) * sin(kappa) + y * (sin(omega) * sin(phi) * sin(kappa) + cos(omega) * cos(kappa)) + z * (cos(omega) * sin(phi) * sin(kappa) - sin(omega) * cos(kappa))
    zr = -x * sin(phi) + y * sin(omega) * cos(phi) + z * cos(omega) * cos(phi)
    return (xr, yr, zr)

def main():
    # Initialize a new plotting window
    plt.figure(figsize=(10, 10))
    axes = plt.axes(projection="3d")
    
    # Setting axis properties
    axes.set_xlim(-10, 10)
    axes.set_ylim(-10, 10)
    axes.set_zlim(-10, 10)
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_zlabel('Z')

    # Draw axes
    axes.plot([0, 10], [0, 0], [0, 0], color='red', linestyle='solid')
    axes.plot([0, -10], [0, 0], [0, 0], color='red', linestyle='dashed')
    axes.plot([0, 0], [0, 10], [0, 0], color='green', linestyle='solid')
    axes.plot([0, 0], [0, -10], [0, 0], color='green', linestyle='dashed')
    axes.plot([0, 0], [0, 0], [0, 10], color='blue', linestyle='solid')
    axes.plot([0, 0], [0, 0], [0, -10], color='blue', linestyle='dashed')
    
    # Original point
    original_point = (4.0, 4.0, 4.0)
    axes.plot([original_point[0]], [original_point[1]], [original_point[2]], marker='o', color='black', label='Original Point')
    
    # Rotation by different angles
    omega = pi / 4
    rotated_x = rot_x_point(original_point, omega)
    axes.plot([rotated_x[0]], [rotated_x[1]], [rotated_x[2]], marker='o', color='red', label='Rotated around X')

    phi = pi / 4
    rotated_y = rot_y_point(original_point, phi)
    axes.plot([rotated_y[0]], [rotated_y[1]], [rotated_y[2]], marker='o', color='green', label='Rotated around Y')

    kappa = pi / 4
    rotated_z = rot_z_point(original_point, kappa)
    axes.plot([rotated_z[0]], [rotated_z[1]], [rotated_z[2]], marker='o', color='blue', label='Rotated around Z')
    
    # Global rotation around X, Y, Z
    rotated_xyz = rot_point(original_point, omega, phi, kappa)
    axes.plot([rotated_xyz[0]], [rotated_xyz[1]], [rotated_xyz[2]], marker='x', color='orange', label='Global Rotation')

    # Add legend to identify points
    axes.legend()

    # Display the 3D plotting window
    plt.show()

if __name__ == "__main__":
    main()
