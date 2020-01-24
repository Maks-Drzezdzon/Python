import sys
import os
import argparse
import csv
import dateutil.parser
import gzip
import requests
import validators

sys.path.append("../cli_tool")  # this isnt needed but just incase there are path issues


def request_data(url) -> str and list:
    """This func handles the url request and passes it to get_data for data extraction"""

    try:
        if validators.url(url):
            file_name = url.split("/")[-1]
            response = requests.get(url, stream=True)
        else:
            raise Exception("Error with url input")

    except Exception as error:
        print("Error has occured in request_data ")
        raise Exception(error)

    if response.status_code == 200:
        with open(file_name, "wb") as f_out:
            # read in chunks
            # shutil.copyfileobj(response.raw, f_out)
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f_out.write(chunk)

    if response.status_code != 200:
        print("Error code in request_data ", response.status_code)
        raise Exception(response.status_code)

    if file_name.split(".")[-1] == "gz":
        data = get_data(file_name)
        return file_name, data
    else:
        raise Exception(
            "file format is not supported yet" + str(file_name.split(".")[-1])
        )


def get_data(file_name) -> list:
    if file_name.split(".")[-2] != "csv":
        raise Exception("file format not yet supported, expects .csv")
    try:
        with gzip.open(file_name, mode="rt") as f_out:

            data_reader = csv.reader(f_out, delimiter=",", quotechar="'")
            # reading as list is bad, it will bottleneck the code here with lare amounts of data
            # im not sure how to read it in row by row efficiently wihtout pandas, could possibly use streams again somehow
            csv_list = [row for row in data_reader]

    except FileNotFoundError as error:
        print("Error has occured in get_data when reading gzip file ")
        raise Exception(error)
    except Exception as error:
        print("Error has occured in get data when reading in file ")
        raise Exception(error)

    try:
        # user count requirement
        users_count = len([person[0] for person in csv_list[1:][0:]])
        # or
        # users_count_v2 = len([row for row in csv_list]) - 1

        # user 640x960 screen size requirement
        phone_screen_dimensions_unsorted = [
            list(phone_screen)
            for phone_screen in zip(
                [height[4] for height in csv_list[1:][0:]],
                [width[5] for width in csv_list[1:][0:]],
            )
        ]

        phone_screen_dimensions = str(
            len(
                [
                    small_phone_screen
                    for small_phone_screen in phone_screen_dimensions_unsorted[0:][0:]
                    if small_phone_screen[0] == "960" and small_phone_screen[1] == "640"
                ]
            )
        )

        # cash spent requirement
        users_spend = str(sum([int(paid[2]) for paid in csv_list[1:][0:]]))

        # first user joined requirement
        dates_joined = [dateutil.parser.parse(ele[1]) for ele in csv_list[1:][0:]]
        user_id_date_joined = [
            list(user_date_joined)
            for user_date_joined in zip(
                [ele[0] for ele in csv_list[1:][0:]],
                [dateutil.parser.parse(ele[1]) for ele in csv_list[1:][0:]],
            )
        ]
        first_user = str(
            [ele[0] for ele in user_id_date_joined if ele[1] == min(dates_joined)].pop()
        )

        data_returned = [users_count, phone_screen_dimensions, users_spend, first_user]
        format_data(data_returned, file_name)

        return data_returned

    except Exception as error:
        print("Error has occured in get_data when unpacking data ")
        raise Exception(error)


def format_data(data_returned, file_name) -> None:
    """ prints outputs for file, assuming everything ran successfully """
    print("User count for this file is", data_returned[0])
    print(
        "There are "
        + data_returned[1]
        + " users with a screen resolution of 640x960 width * height in this data set"
    )
    print("Users spend " + data_returned[2] + " dollars for this data set")
    print("First user was " + data_returned[3])

    clean(file_name)


def clean(file_name) -> None:
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            return "file removed"
    except Exception as error:
        raise error


# for black box testing only
# url = "http-link"
# print(get_data('small.csv.gz'))
# request_data(url)
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="command_line_tool",
        usage="""
                                     Usage:
                                     pass in url as an argument with script to parse data
                                     data format needed .csv.gz
                                     
                                     Available commands:
                                     # to query url
                                     python command_line_tool.py url
                                     
                                     # help
                                     python command_line_tool.py -h
                                     """,
        description="""
                                     ---------------------------------
                                     Description:
                                     This script processes and validates input from a gzip file retrived with a request get function
                                     and returns the user count, small screen size count 640x960, amount spend and the first user that joined
                                     ---------------------------------
                                     """,
        epilog="Copyrights @ Maks Drzezdzon (maksthorn.github.io/MaksymilianDrzezdzon)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=True,
    )
    parser.add_argument(
        "url",
        type=str,
        metavar="Url https://site.com",
        help="""
                        Enter a url for the parse to digest, example
                        https://somesite/data.zip.gz
                        """,
    )

    # --key optional argument alt -k / compulsary "url"
    arg = parser.parse_args()
    request_data(arg.url)
'''