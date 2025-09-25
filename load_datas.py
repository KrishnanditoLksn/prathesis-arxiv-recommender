import json
import pandas as pd

rows = []
with open("arxiv-metadata-oai-snapshot.json", "r", encoding="utf-8") as f:
    for i , line in enumerate(f):
        if i == 50000:
            break
        papers =json.loads(line)
        rows.append({
            'id': papers['id'],
            'title': papers['title'],
            'abstract': papers['abstract'],
            'categories': papers['categories'],
            'author':papers['authors'],
            'doi':papers['doi'],
            'comments':papers['comments']
        })
df = pd.DataFrame(rows)
df.to_csv("arxiv_snapshotss.csv", index=False, encoding="utf-8")
df.to_excel("arxiv_paperssss.xlsx")