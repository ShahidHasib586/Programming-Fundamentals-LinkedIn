import numpy as np
import matplotlib.pyplot as plt

def cube(size):
    s = size
    return [(-s, -s, -s), # Vertex 1
            (-s, s, -s),  # Vertex 2
            (s, s, -s),   # Vertex 3
            (s, -s, -s),  # Vertex 4
            (-s, -s, s),  # Vertex 5
            (-s, s, s),   # Vertex 6
            (s, s, s),    # Vertex 7
            (s, -s, s)]   # Vertex 8

def rotate_vertex(vertex, omega, phi, kappa):
    x, y, z = vertex
    
    # Rotation around X-axis
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(omega), -np.sin(omega)],
                   [0, np.sin(omega), np.cos(omega)]])
    
    # Rotation around Y-axis
    Ry = np.array([[np.cos(phi), 0, np.sin(phi)],
                   [0, 1, 0],
                   [-np.sin(phi), 0, np.cos(phi)]])
    
    # Rotation around Z-axis
    Rz = np.array([[np.cos(kappa), -np.sin(kappa), 0],
                   [np.sin(kappa), np.cos(kappa), 0],
                   [0, 0, 1]])
    
    # Combined rotation
    rotation_matrix = Rz @ Ry @ Rx
    rotated_vertex = rotation_matrix @ np.array([x, y, z])
    
    return tuple(rotated_vertex)

def rotate_cube(vertices, omega, phi, kappa):
    rotated_vertices = []
    for vertex in vertices:
        rotated_vertex = rotate_vertex(vertex, omega, phi, kappa)
        rotated_vertices.append(rotated_vertex)
    return rotated_vertices

def draw_cube(axes, vertices):
    # Unpack vertices for readability
    v1, v2, v3, v4, v5, v6, v7, v8 = vertices
    
    # Draw the edges of the cube
    edges = [(v1, v2), (v2, v3), (v3, v4), (v4, v1),  # Bottom face
             (v5, v6), (v6, v7), (v7, v8), (v8, v5),  # Top face
             (v1, v5), (v2, v6), (v3, v7), (v4, v8)]  # Vertical edges
    
    for edge in edges:
        x_vals = [edge[0][0], edge[1][0]]
        y_vals = [edge[0][1], edge[1][1]]
        z_vals = [edge[0][2], edge[1][2]]
        
        # Determine the color based on the axis
        if edge in [(v1, v2), (v3, v4)]:  # Bottom face edges
            color = 'green'  # Y-axis
        elif edge in [(v2, v3), (v4, v1)]:  # Vertical edges along X-axis
            color = 'red'  # X-axis
        elif edge in [(v5, v6), (v7, v8)]:  # Top face edges
            color = 'green'  # Y-axis
        elif edge in [(v6, v7), (v8, v5)]:  # Vertical edges along X-axis
            color = 'red'  # X-axis
        else:  # Vertical edges along Z-axis
            color = 'blue'
        
        # Plot the edge with the determined color
        axes.plot(x_vals, y_vals, z_vals, color=color)


def main():
    # Initialize a new plotting window
    plt.figure(figsize=(10, 10))
    axes = plt.axes(projection="3d")
    
    # Create a cube of a given size
    size = 3.0
    vertices = cube(size)
    
    # Rotation angles in radians
    omega = np.pi / 4   # 45 degrees
    phi = np.pi / 3     # 60 degrees
    kappa = np.pi / 2   # 90 degrees
    
    # Rotate the cube
    rotated_vertices = rotate_cube(vertices, omega, phi, kappa)
    
    # Draw the original cube
    draw_cube(axes, vertices)
    
    # Draw the rotated cube
    draw_cube(axes, rotated_vertices)
    
    # Setting axis properties
    axes.set_xlim(-10, 10)
    axes.set_ylim(-10, 10)
    axes.set_zlim(-10, 10)
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_zlabel('Z')
    axes.xaxis.label.set_color('red')
    axes.yaxis.label.set_color('green')
    axes.zaxis.label.set_color('blue')
    axes.tick_params(axis='x', colors='red')
    axes.tick_params(axis='y', colors='green')
    axes.tick_params(axis='z', colors='blue')
    
    # Display the 3D plotting window
    plt.show()

if __name__ == "__main__":
    main()
