from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from omegaconf import OmegaConf
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

app = FastAPI(title="API_TDTT")

app.add_middleware(CORSMiddleware,
                    allow_origins=["*"],
                    allow_methods=["*"], 
                    allow_headers=["*"])

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

class Translate:
  def __init__(self, config_path):
    self.config = OmegaConf.load(config_path)
    self.tokenizer = T5Tokenizer.from_pretrained(self.config.model_path)
    self.model = T5ForConditionalGeneration.from_pretrained(self.config.model_path)

  def __call__(self, message):
    inputs = self.tokenizer(message, return_tensors="pt")
    with torch.no_grad():
        logits = self.model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    return self.model.config.id2label[predicted_class_id]

class Answer:
  def __init__(self, config_path):
    self.config = OmegaConf.load(config_path)
    self.tokenizer = T5Tokenizer.from_pretrained(self.config.model_path)
    self.model = T5ForConditionalGeneration.from_pretrained(self.config.model_path)

  def __call__(self, message):
    inputs = self.tokenizer(message, return_tensors="pt")
    with torch.no_grad():
        logits = self.model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    return self.model.config.id2label[predicted_class_id]
 
ans=Answer("./config.yaml")
transToVI = Translate("./config.yaml")

## TODO
@app.get('/trans')
async def trans(message: str):
    return {
        "trans_to_VI": trans(message)
    }

 @app.get('/ans')
async def ans(message: str):
    return {
        "answer": ans(message)
    }
## END TODO



import threading
import uvicorn

def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

thread = threading.Thread(target=run_server, daemon=True)
thread.start()

print("Server started on http://0.0.0.0:8000")