import numpy as np
import pandas as pd
import os

path = "Dataset\For participant 4-16"

df_main = pd.DataFrame()
for corpus in os.listdir(path):
    df = pd.read_csv(path+"/"+corpus)
    df["corpus"] = corpus.replace(".csv","")
    df_main = pd.concat([df_main, df], ignore_index=True)

df_main.to_csv("Dataset/Target-4.csv", index=None)
