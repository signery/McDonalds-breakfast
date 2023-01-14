import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('menu.csv')
print (df['Category'].value_counts())
df['Category'].value_counts().plot(kind = 'pie', grid = True)
df = df[df[ 'Category'] == 'Breakfast']
calories_best_count = 600
calories_min_count = 400
df = df[df[ 'Calories'] >= calories_min_count]
df = df[df[ 'Calories'] <= calories_best_count]



total_fat_min_count = 10
total_fat_best_count = 15
df = df[df[ 'Total Fat'] >= total_fat_min_count]
df = df[df[ 'Total Fat'] <= total_fat_best_count]
print(df)
df = df [(df ['Total Fat'] <= 15) & (df ['Total Fat'] >= 10)]
print(f"Iдеaльна страва на снiданок:{df.head(1)['Item']}")



plt.show()










