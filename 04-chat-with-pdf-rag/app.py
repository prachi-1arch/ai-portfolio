from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import tempfile

app = FastAPI(title="Chat with PDF - RAG API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "RAG Document Q&A API", "version": "1.0.0"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        # Simulated processing
        os.unlink(tmp_path)
        
        return {
            "message": "PDF processed successfully",
            "filename": file.filename,
            "chunks": 42,
            "status": "ready_for_chat"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat(question: str):
    return {
        "question": question,
        "answer": "This is a simulated response. In production, this would use LangChain + Azure OpenAI to retrieve and generate answers from the uploaded PDF.",
        "sources": ["Page 1", "Page 3"],
        "confidence": 0.94
    }

@app.get("/health")
def health():
    return {"status": "healthy", "rag_ready": True}

# Run with: uvicorn app:app --reload
