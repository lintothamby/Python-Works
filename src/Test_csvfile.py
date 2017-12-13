import pandas as pd

path_file= "C:/Users/lthamby/Desktop/Test-Cards/Testt.csv"
df = pd.read_csv(path_file, delimiter=',')
dicts = list(df)
hu = len(dicts)
tuples = [tuple(x) for x in df.values]
#for x in range of  
print(tuples)
print(dicts)
print(hu)