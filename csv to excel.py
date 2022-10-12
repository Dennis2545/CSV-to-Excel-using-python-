# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:22:45 2022

@author: Kiprono
"""

import os
import glob
import csv
from xlsxwriter.workbook import Workbook


for csvfile in glob.glob(os.path.join('.', 'sample.csv')):
    workbook = Workbook(csvfile[:-4] + 'output.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()
    
    """alternative you get $ pip install pyexcel pyexcel-xlsx
you can do it in one command line:

from pyexcel.cookbook import merge_all_to_a_book
# import pyexcel.ext.xlsx # no longer required if you use pyexcel >= 0.2.2 
import glob


merge_all_to_a_book(glob.glob("your_csv_directory/*.csv"), "output.xlsx")
Each csv will have its own sheet and the name will be their file name."""