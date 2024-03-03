from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

# Load pre-trained model for text summarization
summarizer = pipeline("summarization")

class Text(BaseModel):
    text: str
    summary_length: int

@app.post("/summarize/")
async def summarize_text(response:Text):
    # Generate summary using the loaded model
    summary = summarizer(response.text, max_length=response.summary_length, do_sample=False)
    
    # Extract the summarized text from the result
    summarized_text = summary[0]['summary_text']

    # Return the summary in JSON response
    return {"summary": summarized_text}