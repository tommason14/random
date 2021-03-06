#!/usr/bin/env python3

'''
Averages cells in multiple dataframes i.e. averages values in cell 1A in every frame, and outputs results to excel file.
'''

import pandas as pd
import sys


def read_in_files(args):

    dataframes = {}
    for index, arg in enumerate(args):
        key = 'df' + str(index + 1)  # df1, df2...
        dataframes[key] = pd.read_csv(arg)
    return dataframes


def grouping(dictionary):
    vals = [value for value in dictionary.values()]
    return vals


def operations(lst):
    concat = pd.concat(lst)
    group = concat.groupby(concat.index)
    mean = group.mean()
    return mean


def write_to_file(file):
    file.to_excel('mean_values.xlsx', index=False)


def main():
    files = sys.argv[1:]
    sheets = read_in_files(files)
    values = grouping(sheets)
    result = operations(values)
    write_to_file(result)


if __name__ == '__main__':
    main()
