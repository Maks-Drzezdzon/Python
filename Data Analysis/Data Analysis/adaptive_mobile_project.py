import pandas as pd
import re
import csv
import datetime

path = "../Data/adaptive_mobile_dataset.csv"
data = pd.read_csv(path)

path_two = "../Data/employees.csv"
data_two = pd.read_csv(path_two)


def main():
    def read_file():
        print(data)

    read_file()

    def get_name(function_name, path):
        """
        extract name from path, keep file format, concatenate with function name
        """
        file_name = path.split("/")[-1]
        return "".join(function_name + "_" + file_name)

    def to_tsv(path):
        """
        2) How would transform this file into a TSV file? (i.e. a file where the comma separator ',' is substituted with a tab character '\t')
        """
        print(to_tsv.__doc__)
        new_name = get_name("to_tsv", path)

        with open(path, "r") as myfile:
            with open(new_name, "w") as csv_file:
                for line in myfile:
                    # fileContent = re.sub("-", "\t", line)
                    fileContent = re.sub(",", "\t", line)
                    csv_file.write(fileContent)

        print("[*] done")

    to_tsv(path)

    def data_sample():
        """
        3) How would you extract a random sample of 5% of the rows from this file?
        """
        print(data_sample.__doc__)
        # there isnt enough data in this sample for 5% to work so i found another dataset
        # random_sample = data_two.sample(frac = 0.05) # 5%
        random_sample = data.sample(frac=0.5)  # 50%
        print(random_sample)
        print("[*] done")

    data_sample()

    def min_max_date_time():
        """
        4) How would extract the minimum and maximum value from the "Datetime" column?
        """
        print(min_max_date_time.__doc__)
        # in memory solution without formating data in file
        data["Datetime"] = pd.to_datetime(data["Datetime"])
        print(min(data["Datetime"]))
        print(max(data["Datetime"]))
        print("[*] done")

    min_max_date_time()

    def no_duplicate_ids(path):
        """
        5) Let us suppose we don't want duplicated "ID"s. In case there are rows 
       with duplicated IDs we just keep the first row we've found: how would you 
       extract a file, from the original one, without duplicated IDs?
        """
        print(no_duplicate_ids.__doc__)
        """with open(path,'r') as in_file, open('test.csv','w') as out_file:
            seen = set() 
            for line in in_file:
                if line in seen: continue # skip duplicate
        
                seen.add(line)
                out_file.write(line)"""
        # a cleaner solution
        new_name = get_name("no_duplicate_ids", path)
        data.drop_duplicates(subset="ID", keep="first", inplace=True)
        data.to_csv(new_name)
        print(data)
        print("[*] done")

    no_duplicate_ids(path)

    def to_unix_timestamp(path):
        """
        6) How would you create a new file where the "Datetime" column is substituted
        with a "Timestamp" column with the (Unix) timestamp in milliseconds?
        i.e., for the example above you would have:
        """
        print(to_unix_timestamp.__doc__)
        epoch = datetime.datetime.utcfromtimestamp(0)
        new_name = get_name("to_unix_timestamp", path)
        rename_col = data.rename(columns={"Datetime": "Timestamp"})

        for time in pd.to_datetime(rename_col["Timestamp"]):
            ms = (time - epoch).total_seconds() * 1000.0
            rename_col["Timestamp"] = ms
        print(rename_col)

        rename_col.to_csv(new_name)
        print("[*] done")

    to_unix_timestamp(path)

    def count_orderby_sourcetype():
        """
        7) How would you create a simple count of the distinct "SourceType"s? 
        i.e. we want to see each distinct "SourceType", with the number
        of times it appears in the file, sorted by descending number of occurencies.
        """
        print(count_orderby_sourcetype.__doc__)
        # alt i would have used a hash function
        print(data["SourceType"].value_counts())
        # print(data_two['First Name'].value_counts())
        # TODO order by count dont forget
        print("[*] done")

    count_orderby_sourcetype()


if __name__ == "__main__":
    main()

"""
Questions:
1) Which considerations can you make about the input data? 
    # i have no idea ? check it conforms to a pattern ?
    If the file size is big (let’s say 20GB), how would store it? 
    # it depends on what kind of data it is
    # compress it
    
    Would you keep the original format? If not, what would you do? 
    
    Could you describe different options/format for storing the data? 
    
    Which sanity checks would you apply and why?
    
    # TODO
    look up working with large files in python best practices
"""
