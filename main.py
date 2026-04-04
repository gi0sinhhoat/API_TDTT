from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import uvicorn

app = FastAPI(title="API_TDTT")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

MODEL_NAME = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)

@app.get("/")
async def root():
    return {"message": "API tra loi message"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/answer")
async def answer(request: Request):

    body = await request.json()
    text = body.get("text")

    if not text:
        raise HTTPException(status_code=400, detail="Text is required")

    prompt = f"Answer the question: {text}"
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=1000)

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"answer": result}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)