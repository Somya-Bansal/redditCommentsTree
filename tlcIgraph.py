import pandas as pd
import igraph as ig
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

g = ig.Graph.DataFrame(df, directed=True)


def findTLC(vertex):
    parent = g.predecessors(vertex)
    while parent != []:
        print("PARENT -- ",g.vs[parent][0]["name"])
        return findTLC(g.vs[parent][0])


for vertex in g.vs:
    print("VERTEX - ",vertex["name"])
    # print(g.successors(vertex))
    root = findTLC(vertex)
    print("ROOT -- ",root)

layout = g.layout_fruchterman_reingold()
ig.plot(g, target='myfile.pdf')
