import pandas as pd
import glob

files = glob.glob("Input/"+"*.csv")

frames = []

for f in files:

    data = pd.read_csv(f,
                       header=0,
                       sep = ',' )
    
    frames.append(data)

df = pd.concat(frames, ignore_index=True)

df.to_csv("Output/consolidados.csv",header=True, sep=';')