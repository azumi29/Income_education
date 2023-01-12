import pandas as pd

# CSV呼び出し、必要な行の抽出と列の追加
# ◆income_area◆
df_income_area = pd.read_csv('income_area.csv',encoding='ANSI', header=8, usecols=[2,3,5,7])
# 1人当たりの所得【千円】列の追加
df_income_area['1人当たりの所得【千円】'] = df_income_area['C120110_課税対象所得【千円】'] / df_income_area['C120120_納税義務者数（所得割）【人】']
# print(df_income_area)

# ◆education_area◆
df_education_area = pd.read_csv('education_area.csv',encoding='ANSI', header=8, usecols=[2,3,5,7])
# '-'をNaNへ変換してその行を削除
df_education_area['E9106_最終学歴人口（大学・大学院）【人】'] = pd.to_numeric(df_education_area['E9106_最終学歴人口（大学・大学院）【人】'], errors="coerce")
df_education_area['E9101_最終学歴人口（卒業者総数）【人】'] = pd.to_numeric(df_education_area['E9101_最終学歴人口（卒業者総数）【人】'], errors="coerce")
df_education_area = df_education_area.dropna() 
# 大学・大学院卒業割合【%】列の追加
df_education_area['大学・大学院卒業割合【%】'] = df_education_area['E9106_最終学歴人口（大学・大学院）【人】'] / df_education_area['E9101_最終学歴人口（卒業者総数）【人】']*100
# print(df_education_area)

# DataFrameの結合、不要な列の削除
df_income_education = pd.merge(df_income_area, df_education_area)
df_income_education = df_income_education.drop("地域 コード", axis=1)
df_income_education = df_income_education.drop("C120110_課税対象所得【千円】", axis=1)
df_income_education = df_income_education.drop("C120120_納税義務者数（所得割）【人】", axis=1)
df_income_education = df_income_education.drop("E9106_最終学歴人口（大学・大学院）【人】", axis=1)
df_income_education = df_income_education.drop("E9101_最終学歴人口（卒業者総数）【人】", axis=1)
print(df_income_education)






# df_education_area = df_education_area.dropna()
# df_education_area['E9106_最終学歴人口（大学・大学院）【人】'] = df_education_area['E9106_最終学歴人口（大学・大学院）【人】'].fillna(df_education_area['E9106_最終学歴人口（大学・大学院）【人】'].mean())
# df_education_area['E9106_最終学歴人口（大学・大学院）【人】'] = df_education_area['E9106_最終学歴人口（大学・大学院）【人】'].dropna()
# df_education_area = df_education_area[~df_education_area['E9106_最終学歴人口（大学・大学院）【人】'].str.contains('-')]

# df_education_area['E9106_最終学歴人口（大学・大学院）【人】'] = df_education_area['E9106_最終学歴人口（大学・大学院）【人】'].astype(int)

# print(df_education_area['E9106_最終学歴人口（大学・大学院）【人】'].dtypes)
# print(df_education_area)
# print(df_education_area['E9106_最終学歴人口（大学・大学院）【人】'.isnull()])
# # # df_education_area['E9101_最終学歴人口（卒業者総数）【人】'] = df_education_area['E9101_最終学歴人口（卒業者総数）【人】'].astype(int)
# # # print(df_education_area['E9101_最終学歴人口（卒業者総数）【人】'].dtypes)
# # print(df_education_area)