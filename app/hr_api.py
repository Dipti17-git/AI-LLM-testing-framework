from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class HRRequest(BaseModel):
    context: str
    prompt: str


@app.post("/api/chat")
def chat(request: HRRequest):

    if not request.context.strip():
        raise HTTPException(
            status_code=400,
            detail="Context must not be empty"
        )

    if not request.prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Prompt must not be empty"
        )

    context_lower = request.context.lower()
    prompt_lower = request.prompt.lower()

    if (
        "25 vacation days" in context_lower
        and "how many vacation days" in prompt_lower
    ):
        answer = "Employees receive 25 vacation days annually."

    elif "carry" in prompt_lower:
        answer = "The supplied policy does not provide enough information about carrying unused vacation days forward."

    else:
        answer = "The supplied information is insufficient to answer the question."

    return {
        "answer": answer,
        "model": "mock-hr-assistant"
    }