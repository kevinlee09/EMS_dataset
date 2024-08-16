import os
import argparse
import numpy as np
from tqdm import tqdm

def save_obj_with_line_elements(mesh_path, verts, lines):
    file = open(mesh_path, 'w')
    
    for v in verts:
        file.write('v %.4f %.4f %.4f\n' % (v[0], v[1], v[2]))
    for l in lines:
        file.write('l %d %d \n' % (l[0]+1, l[1]+1))
    file.close()

def write_strand2obj(dst_path, strands_path):
    assert dst_path.endswith('obj'), "Error, invalid dst_path!"
    strands = np.load(strands_path)
    pc = []
    lines = []
    sline = 0

    for i in range(len(strands)):
        for j in range(strands.shape[1]):
            pc.append(strands[i][j])
            if j == strands.shape[1] - 1:
                continue     ## for the last node of a strand: not save index
            lines.append([sline + j, sline + j + 1])
        
        sline += len(strands[i])
    
    save_obj_with_line_elements(dst_path, pc, np.asarray(lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert npy to obj format!")
    parser.add_argument('--input', default="./strand_npy_rekey", type=str)
    parser.add_argument('--output', default="./strand_obj_rekey/", type=str)

    args = parser.parse_args()

    data_list = sorted(os.listdir(args.input))

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    for item in tqdm(data_list):
        write_strand2obj(os.path.join(args.output, item[:-3] + "obj") , os.path.join(args.input, item))
