import os
import sys
import bpy
import argparse
import numpy as np


sys.argv = [sys.argv[0]] + sys.argv[6:]
print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument("--out_path", type=str)
parser.add_argument("--out_filename", type=str)
args = parser.parse_args()

if not os.path.exists(args.out_path):
    os.makedirs(args.out_path, exist_ok=True)

obj = bpy.context.scene.objects[0]
mtx = obj.matrix_world

context = bpy.context
dg = context.evaluated_depsgraph_get()
# evaluated object
ob = context.object.evaluated_get(dg)

eyebrow_data = []

bpy.ops.object.mode_set(mode="PARTICLE_EDIT")

bpy.ops.particle.select_all(action="SELECT")
bpy.ops.particle.rekey(keys_number=20)
bpy.ops.particle.particle_edit_toggle()

for hair in ob.particle_systems[0].particles:
    eyebrow_mat = []

    for hair_key in hair.hair_keys:
        eyebrow_mat.append([hair_key.co.x * mtx[0][0], -hair_key.co.y * mtx[1][2] , hair_key.co.z * mtx[2][1] ])
    eyebrow_data.append(np.array(eyebrow_mat))
    
np.save(os.path.join(args.out_path, args.out_filename), np.asarray(eyebrow_data))
print("Save at" + os.path.join(args.out_path, args.out_filename))