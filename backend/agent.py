import asyncio
from data_fetch import company_data
from LLM import portfolio
from excel import excel
async def research_agent(company):
    try:
        yield"Initialising research agent"
        await asyncio.sleep(1)
        yield"Calling Wikipedia API for company summary"
        await asyncio.sleep(1)
        yield"Calling Yahoo Finance API for financial insights"
        await asyncio.sleep(1)
        data=company_data(company)
        yield"Generating company portfolio"
        await asyncio.sleep(1)
        result=portfolio(data)
        yield"Generating Excel report"
        await asyncio.sleep(1)
        excel(data)
        yield"Research complete"
        yield f"FINAL_REPORT::{result}"
    except Exception as e:
        yield f"ERROR:{str(e)}"
   



        



