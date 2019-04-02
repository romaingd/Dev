import numpy as np
import pandas as pd

df = pd.read_csv('results.txt', sep='\t', header=None)
df.columns = ['word', 'filename', 'tf_idf']

df.set_index(['filename', 'word'], inplace=True)

df_top_n = df.groupby(level=0, as_index=False).apply(lambda s: s.nlargest(n=20, columns='tf_idf'))
df_top_n = df_top_n.droplevel(0)

df_top_n.reset_index(inplace=True)
# df.sort_values(by=['filename'])
print(df_top_n.head())
print(df_top_n.values[:20, 1:])
print(df_top_n.values[20:, 1:])
