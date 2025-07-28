from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
import openai
from firebase_admin import credentials, initialize_app, firestore

class Complaint(BaseModel):
    complaint: str

app = FastAPI()

# Initialize Firebase
cred = credentials.Certificate("firebase_credentials.json")
initialize_app(cred)
db = firestore.client()

# Replace with your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY") or "YOUR_OPENAI_API_KEY"

@app.post("/complaints")
async def create_complaint(complaint: Complaint):
    try:
        # Analyze the complaint with OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Analyze the sentiment of the following complaint: {complaint.complaint}\nSentiment:",
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        sentiment = response.choices[0].text.strip()

        # Store the complaint and sentiment in Firebase
        doc_ref = db.collection("complaints").document()
        doc_ref.set({
            "complaint": complaint.complaint,
            "sentiment": sentiment,
            "status": "pending"  # Add a complaint status
        })

        return {"message": "Complaint submitted and analyzed!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/complaints/{complaint_id}")
async def get_complaint(complaint_id: str):
    doc_ref = db.collection("complaints").document(complaint_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        raise HTTPException(status_code=404, detail="Complaint not found")