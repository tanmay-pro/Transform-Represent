from fileinput import filename
import os
import numpy as np
import open3d as o3d

### Convert Mesh to Point Cloud ###

# filePath  = "./meshObjects/trashcan.obj"

# mesh = o3d.io.read_triangle_mesh(filePath)
# pcd = mesh.sample_points_uniformly(10000)
# o3d.io.write_point_cloud("./pcdObjects/trashcan.pcd", pcd)

### ------------------------- ###

### Visualize a mesh File ###

# filePath  = "../../data/Q1/boat.obj"

# mesh = o3d.io.read_triangle_mesh(filePath)
# mesh.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh])

### ------------------------- ###

## Visualize a PCD file ###

# filePath = "./pcdObjects/scene.pcd"
# pcd = o3d.io.read_point_cloud(filePath)
# o3d.visualization.draw_geometries([pcd])    

## ------------------------- ###
