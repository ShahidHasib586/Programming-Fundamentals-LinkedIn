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
    size = 3
    vertices = cube(size)
    
    # Draw the cube
    draw_cube(axes, vertices)
    
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

    # Display the 3D plotting window
    plt.show()

if __name__ == "__main__":
    main()
