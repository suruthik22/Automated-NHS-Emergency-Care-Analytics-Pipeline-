import pandas as pd
import os
import glob
import re

RAW_FOLDER=r"C:\Users\Suruthi\Portfolio_projects\nhs\data\raw"
PROCESSED_FOLDER=r"C:\Users\Suruthi\Portfolio_projects\nhs\data\processed"

PROCESSED_LOG=os.path.join(PROCESSED_FOLDER,"processed_files.txt")
COMBINED_FILE=os.path.join(PROCESSED_FOLDER,"combined_data.csv")

os.makedirs(PROCESSED_FOLDER,exist_ok=True)

#Load alreadt processed files
if os.path.exists(PROCESSED_LOG):
    with open(PROCESSED_LOG,"r") as f:
        processed_files=set(line.strip() for line in f)
else:
    processed_files=set()

files=glob.glob(f"{RAW_FOLDER}/*.csv")

dataframes=[]

standard_columns=None

new_files=[]

for file in files:

    filename=os.path.basename(file)

    #Skip already processed files
    if filename in processed_files:
        print(f"Skipping already processed file:{filename}")
        continue
    
    #processing new files
    
    print(f"processing {filename}")

    try:
        df=pd.read_csv(file)

        #remove completely empty rows
        df=df.dropna(how="all")

        #standardise column names
        df.columns=(df.columns
                    .str.strip()
                    .str.lower()
                    .str.replace(" ","_")
                    .str.replace(r"[^\w]","",regex=True)
        )

        #remove unnamed columns
        df=df.loc[:, ~df.columns.str.contains("^unnamed")]
        
        #Check column consistency
        if standard_columns is None:
            standard_columns=df.columns
        else:
            if not df.columns.equals(standard_columns):
                print(f"Column mismatch in {filename}")
                print(df.columns)
               
                #finding matching columns
                matching_cols=df.columns.intersection(standard_columns)
               
                print(f"Appending only matching columns: {list(matching_cols)}")
                df=df.reindex(columns=standard_columns)                
        
        # extract month and year from file name
        
        match=re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December)[-_]*(\d{4})",filename,re.IGNORECASE)

        if match:
            month=match.group(1)
            year=match.group(2)
        else:
            month=None
            year=None
        
        df['month']=month
        df['year']=year

        text_columns=["period","org_code","parent_org","org_name","month"]

        #Cleaning numeric columns and converting to numeric 
        for col in df.columns:
            if col not in text_columns:
                df[col]=(df[col]
                    .astype(str)
                    .str.replace(",","",regex=False)
                    )
                df[col]=pd.to_numeric(df[col],errors="coerce")
        
        dataframes.append(df)
        new_files.append(filename)
    
    except Exception as e:
        print(f"Skipping {filename} due to error: {e}")

#If nothing new, exit
if not dataframes:
    print("No new files to process... No data processed.")
    exit()

#combine new data
combined_new=pd.concat(dataframes,ignore_index=True)

#Append to existing combined dataset if present
if os.path.exists(COMBINED_FILE):
    existing_df=pd.read_csv(COMBINED_FILE)
    combined_df=pd.concat([existing_df,combined_new],ignore_index=True)
else:
    combined_df=combined_new


combined_df.to_csv(COMBINED_FILE,index=False)

#Update processed log
with open(PROCESSED_LOG,"a") as f:
    for file in new_files:
        f.write(file + "\n")

print("\n New data appended and Combined dataset updated")
print(f"Added {combined_new.shape[0]} rows")
print(f"Combined data set has {combined_df.shape[0]} rows and {combined_df.shape[1]} columns")
print(f"File saved to : {COMBINED_FILE}")
