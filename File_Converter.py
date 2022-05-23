# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:58:46 2022

@author: Rodolfo Henrique T. Valentin 
"""

#The converter will change the file type of all files in the Base file
#Choose below the converter function: Excel to CSV or CSV to Excel 


def Excel_CSV():
    import pandas as pd 
    import os
    import glob
    os.chdir("Base/")
    extension = 'xlsx' #read excel file type xlsx
    
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    for f in range(0,len(all_filenames)):  
        df = pd.read_excel(all_filenames[f])
        df.to_csv(all_filenames[f][:-5]+".csv", index=False)

def CSV_Excel():
    import pandas as pd 
    import os
    import glob
    os.chdir("Base/")
    extension = 'csv' 
    
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    for f in range(0,len(all_filenames)):  
        df = pd.read_csv(all_filenames[f])
        Exceldf = pd.ExcelWriter(all_filenames[f][:-4]+".xlsx")
        df.to_excel(Exceldf,sheet_name=all_filenames[f], index=(False))
        Exceldf.save() 

def Survey():
    print("For CSV to Excel type: 1")
    print("For Excel to CSV Type: 2")

    while True:
        try:
            question = int(input('Inform Function: '))
            break
        except:
            print("That's not a valid option!")

    if question == 1:
        CSV_Excel()
    elif question == 2:
        Excel_CSV()
    else:
        print('That\'s not an option!')


Survey()