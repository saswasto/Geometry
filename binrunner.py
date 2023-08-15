import numpy as np
import pyvista as pv

def create_object(input_string, cube_size=0.1):
    # Define the size of a single cube
    s = cube_size

    # Create a dictionary of cube vertices for each letter in the alphabet
    # We will use this to lookup the vertices of each cube needed for the object
    letter_vertices = {
        'a': [(0, 0, 0), (s, 0, 0), (s, s, 0), (0, s, 0),
              (0, 0, s), (s, 0, s), (s, s, s), (0, s, s)],
        'b': [(0, 0, 0), (s, 0, 0), (s, s, 0), (0, s, 0),
              (0, 0, s), (s, 0, s), (s, s, s), (0, s, s),
              (0, 0, s/2), (s, 0, s/2), (s, s, s/2), (0, s, s/2)],
        # add more letters here...
    }

    # Create an empty point cloud to store the vertices of each cube
    points = pv.PolyData()

    # Loop over each character in the input string
    for i, char in enumerate(input_string.lower()):
        # Lookup the vertices for the current character
        vertices = np.array(letter_vertices.get(char, []))

        # Shift the vertices to the current position in the object
        vertices += np.array([i*s, 0, 0])

        # Add the vertices to the point cloud
        points.points = np.concatenate((points.points, vertices))

    # Create a grid of cells from the points
    cells = np.c_[np.arange(0, points.n_points, 8)]
    cells = np.hstack((np.full((cells.shape[0], 1), 8), cells))

    # Create a polydata object from the cells and points
    polydata = pv.PolyData()
    polydata.points = points.points
    polydata.lines = cells

    # Triangulate the polydata to make it visible
    surface = polydata.delaunay_3d()

    return surface
