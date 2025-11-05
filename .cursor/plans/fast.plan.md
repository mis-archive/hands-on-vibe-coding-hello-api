<!-- 4d7c49e3-3fe8-4fb2-9691-a8bf641416e6 012da382-c278-42f4-914e-ac4e6b112a9e -->
# FastAPI Hello/Goodbye API (no GCP yet)

## What we'll build

A minimal Python FastAPI app exposing two endpoints:

- `GET /hello`: returns a casual hello
- `GET /goodbye`: returns a casual goodbye

## Files to add

- `app/main.py` — FastAPI app with two routes
- `requirements.txt` — `fastapi`, `uvicorn[standard]`
- `Dockerfile` — container to run the app locally or later in CI/CD
- `.gitignore` — Python, venv, editor files
- `README.md` — how to run locally and via Docker
- `PROMPTS.md` — log of prompts per workspace rules

## Key snippets

- `app/main.py`:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hey there! 👋"}

@app.get("/goodbye")
def goodbye():
    return {"message": "Catch you later! ✌️"}
```

- `Dockerfile` (slim):
```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```


## Git setup

- Initialize a local git repo, create a feature branch (e.g., `feat/fastapi-skeleton`), commit files.

## How you'll run it locally

- `pip install -r requirements.txt`
- `uvicorn app.main:app --reload`
- Visit `http://127.0.0.1:8000/hello` and `/goodbye`

## Next (later):

- Add GitHub repo and Cloud Run deploy workflow when ready.

### To-dos

- [ ] Create project structure and base files (app, reqs, gitignore)
- [ ] Implement FastAPI app with hello/goodbye endpoints
- [ ] Add Dockerfile for local container run
- [ ] Create README.md and PROMPTS.md with run instructions and entry
- [ ] Initialize local git repo, create branch, initial commit