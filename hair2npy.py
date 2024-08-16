import os
import argparse
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process EBStore dataset!")
    parser.add_argument('--input', default="./dataset/blender", type=str)
    parser.add_argument('--output', default="./strand_npy_rekey", type=str)

    args = parser.parse_args()
    
    data_list = sorted(os.listdir(args.input))
    blender_path = "blender"  # replace your blender path here
    
    for item in tqdm(data_list):
        blend_file = os.path.join(args.input, item, item + ".blend")    
        out_file = item + "_eyebrow_npy"
        os.system(f"{blender_path} -b {blend_file} -P hair_export_rekey.py -- --out_path {args.output} --out_filename {out_file}")