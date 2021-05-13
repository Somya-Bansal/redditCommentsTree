import pandas as pd
import numpy as np
import os


def writeToFile(teams, filePath):
    df = pd.DataFrame(teams)
    # write hearder only once
    write_header = not os.path.exists(filePath)
    df.to_csv(filePath, header=write_header, sep=',', mode='a', index=False)


# filename = 'comments_politics.csv'
filename = 'test.csv'
df = pd.read_csv(filename)
# columnNames = ['parent_id','id', 'link_id', 'all_awardings', 'approved_at_utc', 'associated_award', 'author', 'author_flair_background_color','author_flair_css_class', 'author_flair_richtext', 'author_flair_template_id', 'author_flair_text', 'author_flair_text_color', 'author_flair_type', 'author_fullname', 'author_patreon_flair', 'author_premium', 'awarders', 'banned_at_utc','body', 'can_mod_post', 'collapsed', 'collapsed_because_crowd_control', 'collapsed_reason', 'comment_type', 'created_utc', 'distinguished', 'edited', 'gildings', 'is_submitter',  'locked', 'no_follow',  'permalink', 'retrieved_on', 'score', 'send_replies', 'stickied', 'subreddit', 'subreddit_id', 'top_awarded_type', 'total_awards_received', 'treatment_tags', 'author_cakeday']
# df = df.reindex(columns=columnNames)
# writeToFile(df.head(100), 'test.csv')


df['parent_id'] = df['parent_id'].str[3:]
df['link_id'] = df['link_id'].str[3:]
# print(df['parent_id'])
# df['parent_id'] = pd.to_numeric(df.parent_id, errors='coerce')

# first index by id
df.set_index('id', drop=False, inplace=True)

lst = [df['id'].values]
new_df = df.copy()
# print(new_df[['id', 'parent_id']])


# Iterate until all values in 'id' are NaN 
while new_df['id'].notna().any(): 
# and not new_df['id'].isin(new_df['link_id']).any():
# and new_df["id"].any() != new_df["link_id"].any():

    # keep if parentid = id
    new_df = df.reindex(new_df['parent_id'])
    # print(new_df[['id', 'parent_id']])
    lst.append(new_df['id'].values)
# print(lst)

hierarchy = ['/'.join(filter(np.nan.__eq__, i)) for i in zip(*lst[::-1])]
topLevelCommentId = []
for h in hierarchy:
    topLevelCommentId.append(h.split('/')[0])
hierarchy = pd.DataFrame({'Top Level Comment': topLevelCommentId,'Hierarchy': hierarchy, 'id': df['id'].values})


pd.set_option('display.max_rows', df.shape[0]+1)
# print(df)
print(hierarchy)
