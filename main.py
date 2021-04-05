import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# print(data_frame.head())
# print(data_frame.tail())

# Highest number oof posts
# print(data_frame.groupby("TAG").sum())
# How many months of entries exist per programming language.
# print(data_frame.groupby("TAG").count())

data_frame['DATE'] = pd.to_datetime(data_frame.DATE)
# print(data_frame)

# test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
#                         'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
#                         'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
# print(test_df)
#
# pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# print(pivoted_df)

reshaped_df = data_frame.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)
reshaped_df.fillna(0)
# print(reshaped_df)
roll_df = reshaped_df.rolling(window=12).mean()
# print(roll_df)
plt.figure(figsize=(8, 5))
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Posts', fontsize=12)
plt.ylim(0, 35000)
# plt.plot(reshaped_df.index, reshaped_df.java)
# plt.plot(reshaped_df.index, reshaped_df['python'])

for col in roll_df.columns:
    plt.plot(roll_df.index, roll_df[col], label=roll_df[col].name, linewidth=2)
plt.legend(fontsize=10)
plt.show()