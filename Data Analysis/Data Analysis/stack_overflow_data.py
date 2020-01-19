import pandas as pd


df = pd.read_csv("..\Data\developer_survey_2019\survey_results_public.csv")
# print(df.head())
# print(df.tail(8))
# print(df.info())

data = {
        'user_name' : ['maks','mag'],
        'user_from' : ['ger', 'pol'],
        'other' : ['thing  1', 'thing 2']
}

create_df = pd.DataFrame(data)
# print(create_df)
# print(create_df['user_name']) == print(create_df.user_name)
# like join in sql
# print(create_df[['other', 'user_name']])

# to see cols
create_df.columns

# to see first row by index [[rows], [cols]]
print(create_df.iloc[[0, 1]])


