import pandas as pd

df = pd.read_csv("data/product_info.csv")

df['商品説明'] = df['商品説明'].str.strip()
df['価格'] = df['価格'].replace('"', '').replace(',', '')
df['評価数'] = df['評価数'].replace('"', '').replace(',', '')

# print(df['商品説明'].isnull())
df = df.dropna(subset=['商品説明'])

df.to_csv("data/processed_product_info.csv", index=False)