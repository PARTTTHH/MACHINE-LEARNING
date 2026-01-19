"""
AFTER PRIVEWING DATA WHEN WE NEED TO KNOW DATA SUMMARY LIKE INFO 
        TYPE OF OBJECT     [CONFORM THIS IS A DATAFRAME]
        NUMBER OF COLUMNS AND ROWS  
        WHAT TYPE OF DATA  [int64, float64, python object]
        COLUMMS NAMES
        NON-NULL COUNT
        MEMORY UASAGE OF THE DATA FRAME

FOR THIS PANDAS PROVIDES A BUIT-IN METHOS info()
data_frame_here.info()
THIS RETURNS ALL ABOVE INFO ABOUT DATA   LETS SEE AN EXAMPLE

NOTE --- info() is used for structural inspection, not value inspection
         It prints output and returns None
object usually means:
text
OR mixed types
OR dates not parsed yet
"""

import pandas as pd

datafame = pd.read_csv("PANDAS/FOUNDATION/FILE_READING/sales_data_sample.csv", encoding="latin1")
datafame.info()