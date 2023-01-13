import pandas as pd
import matplotlib.pyplot as plt

# CSV呼び出し、必要な行の抽出と列の追加
# ◆income_area◆
df_income_area = pd.read_csv('income_area.csv',encoding='ANSI', header=8, usecols=[2,3,5,7])
# # 1人当たりの所得【千円】列の追加
df_income_area['1人当たりの所得【千円】'] = df_income_area['C120110_課税対象所得【千円】'] / df_income_area['C120120_納税義務者数（所得割）【人】']

# ◆education_area◆
df_education_area = pd.read_csv('education_area.csv',encoding='ANSI', header=8, usecols=[2,3,5,7])
# # '-'をNaNへ変換してその行を削除
df_education_area['E9106_最終学歴人口（大学・大学院）【人】'] = pd.to_numeric(df_education_area['E9106_最終学歴人口（大学・大学院）【人】'], errors="coerce")
df_education_area['E9101_最終学歴人口（卒業者総数）【人】'] = pd.to_numeric(df_education_area['E9101_最終学歴人口（卒業者総数）【人】'], errors="coerce")
df_education_area = df_education_area.dropna() 
# # 大学・大学院卒業割合【%】列の追加
df_education_area['大学・大学院卒業割合【%】'] = df_education_area['E9106_最終学歴人口（大学・大学院）【人】'] / df_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100

# DataFrameの結合、不要な列の削除
df_income_education = pd.merge(df_income_area, df_education_area)
df_income_education = df_income_education.drop("地域 コード", axis=1)
df_income_education = df_income_education.drop("C120110_課税対象所得【千円】", axis=1)
df_income_education = df_income_education.drop("C120120_納税義務者数（所得割）【人】", axis=1)
df_income_education = df_income_education.drop("E9106_最終学歴人口（大学・大学院）【人】", axis=1)
df_income_education = df_income_education.drop("E9101_最終学歴人口（卒業者総数）【人】", axis=1)
print(df_income_education)

# 散布図
# X軸：学歴、Y軸：収入
plt.scatter(df_income_education['大学・大学院卒業割合【%】'], df_income_education['1人当たりの所得【千円】'])
# グラフタイトル
plt.title("収入と学歴",fontname='MS Gothic')
# X軸ラベル
plt.xlabel('大学・大学院卒業割合【%】',fontname='MS Gothic')
# Y軸ラベル
plt.ylabel('1人当たりの所得【千円】',fontname='MS Gothic')

# グラフをpngに保存
plt.savefig("income_education_graph.png")

# 散布図表示
plt.show()