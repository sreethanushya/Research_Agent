import pandas as pd
import os 
def excel(data):
    df=pd.DataFrame([{"company":data["company"],"Industry":data["industry"],"Employees":data["employees"],"Revenue":data["revenue"],"Market Cap":data["market_cap"],"website":data["website"],"gross profit":data["gross_profit"],"Operationg Expense":data["operating_expense"]}])
    file_name=f"{data['company']}_report.xlsx"
    df.to_excel(file_name , index=False)
    return os.path.abspath(file_name)

