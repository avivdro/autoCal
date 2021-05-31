"""
aviv drori
may 2021
This file uses opnenpyxl to read and write to the excel
"""

import openpyxl
from openpyxl import load_workbook

# EXCEL FILE CONSTANTS:
DATABASE_FILE = 'database.xlsx'
SHEET1_NAME = 'Sheet1'

# SHEET1:
COL_A = 'A'

# EXCEL SHEET STARTUP
DB = load_workbook(DATABASE_FILE)
SHEET1 = DB[SHEET1_NAME]


def save():
    DB.save(DATABASE_FILE)
    return


def tests():
    # tests:
    print(SHEET1[COL_A + str(1)].value)   # output should be test
    print(SHEET1['A2'].value)       # output should be 2
    SHEET1[COL_A + str(5)] = "write test"
    save()


if __name__ == '__main__':
    tests()
