import pygmsh
import numpy as np
from matplotlib import pyplot as plt
from leer_GMSH import xnod_from_msh, LaG_from_msh, plot_msh

with pygmsh.geo.Geometry() as geom:
    geom.add_polygon(
        [
            [0.0, 0.0],
            [1.0, 0.0],
            [1.0, 1.0],
            [0.0, 1.0],
        ],
        mesh_size=0.1,
    )
    mesh = geom.generate_mesh()

#mesh.points, mesh.cells, ...

mesh.write('mesh_rect.vtk')

points=mesh.points
triangles=mesh.get_cells_type("triangle")
#print(triangles)

pts = points[:, :2]
for e in triangles:
    for idx in [[0, 1], [1, 2], [2, 0]]:
        X = pts[e[idx]]
        plt.plot(X[:, 0], X[:, 1], "-k")
plt.gca().set_aspect("equal", "datalim")
plt.axis("off")
plt.show()
