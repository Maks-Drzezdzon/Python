import pandas as pd
import re
import datetime

# global variables
adaptive_mobile_dataset_path = "../Data/adaptive_mobile_dataset.csv"
# adaptive_mobile_dataset_path = "adaptive_mobile_dataset.csv"
adaptive_mobile_dataset = pd.read_csv(adaptive_mobile_dataset_path)

employees_data_set_path = "../Data/employees.csv"
# employees_data_set_path = "employees.csv"
employees_data_set = pd.read_csv(employees_data_set_path)


def main():
    def read_file():
        """
        original file
        """
        print(read_file.__doc__)
        print(adaptive_mobile_dataset)
        print("[*] done")

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
        extracted_name = get_name("to_tsv", path)

        with open(path, "r") as myfile:
            with open(extracted_name, "w") as csv_file:
                for line in myfile:
                    # fileContent = re.sub("-", "\t", line)
                    fileContent = re.sub(",", "\t", line)
                    csv_file.write(fileContent)

        print("[*] done")

    to_tsv(adaptive_mobile_dataset_path)

    def data_sample():
        """
        3) How would you extract a random sample of 5% of the rows from this file?
        """
        print(data_sample.__doc__)
        # there isnt enough data in this sample for 5% to work so i found another dataset
        # random_sample = employees_data_set.sample(frac = 0.05) # 5%
        random_sample = adaptive_mobile_dataset.sample(frac=0.5)  # 50%
        print(random_sample)
        print("[*] done")

    data_sample()

    def min_max_date_time():
        """
        4) How would extract the minimum and maximum value from the "Datetime" column?
        """
        print(min_max_date_time.__doc__)
        # in memory solution without formating data in file
        try:
            adaptive_mobile_dataset["Datetime"] = pd.to_datetime(adaptive_mobile_dataset["Datetime"])
        except ValueError as error:
            print(error)
        except Exception as e:
            print(e)
            
        print(min(adaptive_mobile_dataset["Datetime"]))
        print(max(adaptive_mobile_dataset["Datetime"]))
        print("[*] done")

    min_max_date_time()

    def no_duplicate_ids(path):
        """
        5) Let us suppose we don't want duplicated "ID"s. In case there are rows 
       with duplicated IDs we just keep the first row we've found: how would you 
       extract a file, from the original one, without duplicated IDs?
        """
        print(no_duplicate_ids.__doc__)
        extracted_name = get_name("no_duplicate_ids", path)
        try:
            adaptive_mobile_dataset.drop_duplicates(subset="ID", keep="first", inplace=True)
        except Exception as e:
            print(e)
            
        adaptive_mobile_dataset.to_csv(extracted_name)
        print(adaptive_mobile_dataset)
        print("[*] done")

    no_duplicate_ids(adaptive_mobile_dataset_path)

    def unix_timestamp_in_ms(path):
        """
        6) How would you create a new file where the "Datetime" column is substituted
        with a "Timestamp" column with the (Unix) timestamp in milliseconds?
        i.e., for the example above you would have:
        """
        print(unix_timestamp_in_ms.__doc__)
        epoch = datetime.datetime.utcfromtimestamp(0)
        extracted_name = get_name("to_unix_timestamp", path)
        renamed_col = adaptive_mobile_dataset.rename(columns={"Datetime": "Timestamp"})

        for time in pd.to_datetime(renamed_col["Timestamp"]):
            try:
                ms = (time - epoch).total_seconds() * 1000.0
                renamed_col["Timestamp"] = ms
            except ValueError as error:
                print(error)
            except Exception as e:
                print(e)
                
        print(renamed_col)

        renamed_col.to_csv(extracted_name)
        print("[*] done")

    unix_timestamp_in_ms(adaptive_mobile_dataset_path)

    def count_orderby_sourcetype():
        """
        7) How would you create a simple count of the distinct "SourceType"s? 
        i.e. we want to see each distinct "SourceType", with the number
        of times it appears in the file, sorted by descending number of occurencies.
        """
        print(count_orderby_sourcetype.__doc__)
        # alt i would have used a hash function
        # output is already in 
        print(adaptive_mobile_dataset["SourceType"].value_counts().sort_values(ascending = False))
        # print(employees_data_set['First Name'].value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True))
        print("[*] done")

    count_orderby_sourcetype()


if __name__ == "__main__":
    """
    formatted with black
    written with spyder in anaconda environment
    """
    main()

"""
Questions:
1)  
    -> Which considerations can you make about the input data? 
    # its not sanitized, hasn't been cleaned, needs to conform to a pattern
    
    
    
    
    -> If the file size is big (let’s say 20GB), how would store it? 
    # it depends on what kind of data it is
    # if its structured then MySQL
    # if nots not structured or semi structured MongoDB/NoSQL
    
    # this is because joins are slower in MySQL and processing lots of data is time consuming
    
    # MariaDB is also a good alternative to both because it supports SQL and NoSQL
    # compress it and store it on a cloud server so its easier to access with a .tar or gzip
    
    
    
    
    -> Would you keep the original format? If not, what would you do?
    # it also depends what kind of data it is, does it need SQL or NoSQL, is it numerical or categorical
    # it might need to be labled etc
    
    # Search engines excel at text queries, e.g elasticsearch    
    # Columnar stores for faster sum and avg operations on for example numerical data, e.g RedShift
    
    # if its not slow to access and decompress then keeping the format is ok 
    
    # allowing to focus on other aspects of data storing such as technologies used
    # this could be more beneficial and provide more speed 
    
    
    
    
    -> Could you describe different options/format for storing the data? 
    # Options #
    # NoSQL/SQL with tables, collections, schemas etc
    # MariaDB supports both
    # Cassandra tends to be used for Big Data
    
    # Columnar Store work best when read from disk meaning smaller datasets in Gigabytes can be stored inhouse
    
    # sharding could be used if the dataset gorws making the database divide data into chunks
    
    # Formats #
    # CSV - easy to use slow save times avg load time, low 
    # Pickle also works for AI models - fast read and save time, high memory consumption
    # JSON - fast read and load time
    # HDF5 for large amounts of data - avg read and save time, high memory consumption
    # Feather is a binary file format for storing data frames - very fast read and save time however this is due to the nature of small dataframes
    # Parquet - Hadoop columnar storage format - fast read and save time
    
    
    -> Which sanity checks would you apply and why?
    # validate spelling so that inconsistencies dont start emerging
    # date format check or formated
    # how values are entered 1 vs 1.0
    # avoid duplicated data
    # compare head() or tail() of dataset to random sample to ensure that structure is the same
    # check value distribution, odd data distribution may speak up for larger data quality issues
    # e.g some data points are missing, data doesnt add up i.e peak website traffic being at quater past midnight (00:15) vs 15:00 pm because of bad input
    # 
    
"""
