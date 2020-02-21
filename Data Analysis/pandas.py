import pandas as pd

dev_survey_dataset_path = "Data/survey_results_public.csv"
dev_survey_dataset = pd.read_csv(dev_survey_dataset_path)

survey_schema_dataset_path = "Data/survey_results_schema.csv"
survey_schema_dataset = pd.read_csv(survey_schema_dataset_path)


def br():
    print(" ")
    print("[*] break for new call")
    print(" ")
    return


# gives you rows
print(dev_survey_dataset.shape)
br()
# shows entries, cols and lists the cols with data type
print(dev_survey_dataset.info())
br()
# set options for seeing full row
# dev_survey_dataset.set_option('display.max_columns', 85)
# survey_schema_dataset.set_option('display.max_rows', 85)

print(dev_survey_dataset.head(10))
br()
print(dev_survey_dataset.tail(10))
br()


people = {
    "first": ["Maks", "Adam", "Magda"],
    "last": ["D", "P", "P"],
    "email": ["maks@email.com", "adam@email.com", "magda@email.com"],
}

# convert to df
df = pd.DataFrame(people)
print(df)
br()

# series object is a 1 dimential array
# each col is a series
# dataframe is a container of a series object that contains the rows for 1 column
"""
first last email

maks  x    x

adam  x    x

magda x    x

# the 'first' col is a series

"""

print(df[["last", "email"]])
br()

# prints all col names
print(df.columns)
br()

# interger location
# returns first row of data by index
# https://www.youtube.com/watch?v=zmdjNSmRXF4&t=1133s
print(df.iloc[0])
print(df.iloc[[0, 2]])
br()
# to get the email of the first 2 rows
print(df.iloc[[0, 2], 2])
br()
# for locations
print(df.loc[0])
br()
# you can also pass in the label
print(df.loc[[0, 1], ["email", "name"]])
br()
print(dev_survey_dataset["Hobbyist"].value_counts())
br()
# getting data for first row in col hobbyist, loc is also inclusive
print(dev_survey_dataset.loc[0, "Hobbyist"])
br()
print(dev_survey_dataset.loc[0:2, "Hobbyist":"Employment"])
