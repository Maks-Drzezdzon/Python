import csv
import os
import pandas as pd
import glob

def combine_csv():
    # prerequesit data
    # os.chdir("/Desktop/csvFolder")
    extension = "csv"
    # match all files with extension with * all .{} format and extension variable
    # using glob for working dir
    all_files = [ele for ele in glob.glob('*.{}'.format(extension))]
    # combine all csv files
    full_csv = pd.concat([pd.read_csv(ele) for ele in all_files])
    # using utf-8-sig for none english player names IE china etc + ignore index numbers
    full_csv.to_csv("fire-mage-mythic-logs.csv",index = False, encoding = 'utf-8-sig')


boss_kill_duration = pd.read_csv('fire-mage-mythic-logs.csv')

duration = boss_kill_duration['Duration']



