from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from .helpers.helper import compress_summary

app = FastAPI()

# Load pre-trained model for text summarization
summarizer = pipeline("summarization")

class SummarizeText(BaseModel):
    text: str
    summary_length: int

class CompressText(BaseModel):
    summary: str

@app.post("/summarize/")
async def summarize_text(response:SummarizeText):
    # Generate summary using the loaded model
    summary = summarizer(response.text, max_length=response.summary_length, do_sample=False)
    
    # Extract the summarized text from the result
    summarized_text = summary[0]['summary_text']

    # Return the summary in JSON response
    return {"summary": summarized_text}

@app.post('/compress_summary/')
async def compress_summary_endpoint(original_summary:CompressText):
    compressed_summary = compress_summary(original_summary.summary)
    return {'compressed_summary': compressed_summary}