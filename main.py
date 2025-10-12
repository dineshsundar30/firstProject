import pandas as pd
import csv
from datetime import datetime
from data_entry import *

class Csv:
    Csv_File = "Finance_data.csv" 
    Columns = ["Date","Amount","Category","Description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.Csv_File)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.Columns) 
            df.to_csv(cls.Csv_File,index=False)
    
    @classmethod
    def add_entry(cls, Date,Amount,Category,Description):
        new_entry = {
            "Date": Date,
            "Amount": Amount,
            "Category":Category,
            "Description":Description
        }
        with open(cls.Csv_File,"a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.Columns)
            writer.writerow(new_entry)
        print("Entry Added successfully")

def add():
    Csv.initialize_csv()
    date = get_date(
        "Enter the date for the transcation (dd-mm-yyy) or enter for today's date: ",
        allow_default=True
    ) 
    amount = get_amount()
    category = get_category()
    description = get_description()
    Csv.add_entry(date,amount,category,description)

add()