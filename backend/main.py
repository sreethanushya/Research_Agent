from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from agent import research_agent
app = FastAPI()
app.add_middleware(CORSMiddleware , allow_origins=["*"], allow_credentials=True, allow_methods=["*"],allow_headers=["*"],)
@app.get("/")
def home():
    return {"message": "company research agent running"}
@app.get("/research/{company}")
async def research (company:str):
    async def stream():
        async for update in research_agent(company):
            yield f"data: {update}\n\n"
    return StreamingResponse( stream(), media_type="text/event-stream")
@app.get("/download/{company}")
def download(company:str):
    file_path = f"{company}_report.xlsx"
    return FileResponse(file_path,filename=file_path)


    
   

