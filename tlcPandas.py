import pandas as pd
import numpy as np
import os


def writeToFile(teams, filePath):
    df = pd.DataFrame(teams)
    write_header = not os.path.exists(filePath)
    df.to_csv(filePath, header=write_header, sep=',', mode='a', index=False)


# filename = 'comments_politics.csv'
filename = 'test.csv'
df = pd.read_csv(filename)
# writeToFile(df.head(100), 'test.csv')


df['parent_id'] = df['parent_id'].str[3:]
df['link_id'] = df['link_id'].str[3:]

# first index by id
df.set_index('id', drop=False, inplace=True)
lst = [df['id'].values]
new_df = df.copy()

# Iterate until all values in 'id' are NaN 
while new_df['id'].notna().any(): 
    new_df = df.reindex(new_df['parent_id'])
    lst.append(new_df['id'].values)

hierarchy = ['/'.join(filter(np.nan.__eq__, i)) for i in zip(*lst[::-1])]
topLevelCommentId = []
for h in hierarchy:
    topLevelCommentId.append(h.split('/')[0])
hierarchy = pd.DataFrame({'Top Level Comment': topLevelCommentId,'Hierarchy': hierarchy, 'id': df['id'].values})

df['tlc_id'] = topLevelCommentId
pd.set_option('display.max_rows', df.shape[0]+1)
# print(df)
df.to_csv('test.csv')