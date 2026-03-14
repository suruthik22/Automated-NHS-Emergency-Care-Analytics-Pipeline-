import os 
import requests 
import pandas as pd 
import numpy as np 
from datetime import datetime 
from bs4 import BeautifulSoup 

base_url="https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/" 

# Store raw data 
RAW_FOLDER=r"C:\Users\Suruthi\Portfolio_projects\nhs\data\raw" 
os.makedirs(RAW_FOLDER, exist_ok=True) 

# Generate year pages 
start_year=2025 
end_year=2024 

year_pages=[] 

for year in range(start_year,end_year-1,-1): 
    next_year=str(year+1)[-2:] 
    url=f"{base_url}/ae-attendances-and-emergency-admissions-{year}-{next_year}/" 
    year_pages.append(url) 
    
    print("Year pages to scan:") 
    
    for page in year_pages: 
        print(f"\n scanning {page}") 
        response=requests.get(page) 
        soup=BeautifulSoup(response.text,"lxml") 
        links=soup.find_all("a") 
        
        for link in links: 
            text=link.text.strip() 
            href=link.get("href") 
            
            if text.startswith("Monthly A&E") and href and ".csv" in href.lower(): 
                file_url=href 
                filename=file_url.split("/")[-1] 
                
                file_path=os.path.join(RAW_FOLDER,filename)
                
                # Skip if file already exists
                if os.path.exists(file_path):
                    print(f"{filename} already exists. Skipping it...")
                    continue

                # downloading files
                print(f"Downloading {filename}") 
                
                file_data=requests.get(file_url) 
                
                with open(f"{RAW_FOLDER}/{filename}","wb") as f: 
                    f.write(file_data.content) 

print("\n Download completed")