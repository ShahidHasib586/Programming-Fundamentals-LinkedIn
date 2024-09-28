import matplotlib.pyplot as plt
from numpy import sin, cos, pi

def rot_x_point(point, omega):
    x, y, z = point
    xr = x
    yr = y * cos(omega) - z * sin(omega)
    zr = y * sin(omega) + z * cos(omega)
    return xr, yr, zr

def rot_y_point(point, phi):
    x, y, z = point
    xr = x * cos(phi) + z * sin(phi)
    yr = y
    zr = -x * sin(phi) + z * cos(phi)
    return xr, yr, zr

def rot_z_point(point, kappa):
    x, y, z = point
    xr = x * cos(kappa) - y * sin(kappa)
    yr = x * sin(kappa) + y * cos(kappa)
    zr = z
    return xr, yr, zr

def rot_point_comp(point, omega, phi, kappa):
    # Apply rotation around X axis
    point = rot_x_point(point, omega)
    # Apply rotation around Y axis
    point = rot_y_point(point, phi)
    # Apply rotation around Z axis
    point = rot_z_point(point, kappa)
    return point

def rot_point(point, omega, phi, kappa):
    x, y, z = point
    xr = (x * cos(phi) * cos(kappa) +
          y * (sin(omega) * sin(phi) * cos(kappa) - cos(omega) * sin(kappa)) +
          z * (cos(omega) * sin(phi) * cos(kappa) + sin(omega) * sin(kappa)))
    yr = (x * cos(phi) * sin(kappa) +
          y * (sin(omega) * sin(phi) * sin(kappa) + cos(omega) * cos(kappa)) +
          z * (cos(omega) * sin(phi) * sin(kappa) - sin(omega) * cos(kappa)))
    zr = (-x * sin(phi) +
          y * sin(omega) * cos(phi) +
          z * cos(omega) * cos(phi))
    return xr, yr, zr

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
    
    # Draw X, Y, Z axes
    axes.plot([0, 10], [0, 0], [0, 0], color='red', linestyle='solid')
    axes.plot([0, -10], [0, 0], [0, 0], color='red', linestyle='dashed')
    axes.plot([0, 0], [0, 10], [0, 0], color='green', linestyle='solid')
    axes.plot([0, 0], [0, -10], [0, 0], color='green', linestyle='dashed')
    axes.plot([0, 0], [0, 0], [0, 10], color='blue', linestyle='solid')
    axes.plot([0, 0], [0, 0], [0, -10], color='blue', linestyle='dashed')
    
    # Draw the original point
    original_point = (4.0, 4.0, 4.0)
    axes.plot([original_point[0]], [original_point[1]], [original_point[2]], marker='o', color='black', label='Original Point')
    
    # Rotation angles
    omega = pi / 4
    phi = pi / 4
    kappa = pi / 4
    
    # Rotate using rot_point
    rotated_point = rot_point(original_point, omega, phi, kappa)
    axes.plot([rotated_point[0]], [rotated_point[1]], [rotated_point[2]], marker='x', color='orange', label='Rotated Point (rot_point)')
    
    # Rotate using rot_point_comp
    rotated_point_comp = rot_point_comp(original_point, omega, phi, kappa)
    axes.plot([rotated_point_comp[0]], [rotated_point_comp[1]], [rotated_point_comp[2]], marker='+', color='violet', label='Rotated Point (rot_point_comp)')
    
    # Add legend to identify points
    axes.legend()

    # Display the 3D plotting window
    plt.show()

if __name__ == "__main__":
    main()
