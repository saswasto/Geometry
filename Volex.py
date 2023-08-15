import pyvista as pv

# Create a cube mesh
cube = pv.Cube()

# Visualize the cube
p = pv.Plotter()
p.add_mesh(cube, color='white')
p.show()
