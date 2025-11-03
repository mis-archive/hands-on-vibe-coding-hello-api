<!-- d804cd46-97c0-40bf-bd2d-0d87dff3b2bf 5c41ce3c-2926-4022-8ec7-5a896e15a0af -->
# FastAPI Hello/Goodbye API (Local Only)

## Scope

- Build a minimal FastAPI service with two endpoints: `GET /hello` and `GET /goodbye`.
- Set up local Git repository per workspace rules.
- Add essential project files: dependencies, `.gitignore`, `README.md`, `PROMPTS.md`.
- Defer any Google Cloud/GitHub deployment logic.

## Files to Add/Modify

- `app/main.py`
  - Minimal FastAPI app exposing two routes:
    - `GET /hello` → returns a casual hello JSON
    - `GET /goodbye` → returns a casual goodbye JSON
  - Example:
    ```
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/hello")
    def hello():
        return {"message": "Hey there! 👋"}
    
    @app.get("/goodbye")
    def goodbye():
        return {"message": "Catch you later! 👋"}
    ```

- `requirements.txt`
  - `fastapi`
  - `uvicorn[standard]`

- `.gitignore`
  - Add Python ignores (e.g., `__pycache__/`, `.venv/`, `*.pyc`, `.env`)

- `README.md`
  - How to set up venv, install deps, run locally with uvicorn, curl examples for both endpoints, and notes on branching convention.

- `PROMPTS.md`
  - Create if missing; append a timestamped entry describing this request per workspace rules.

## Local Run Instructions (to place in README)

- Create venv: `python -m venv .venv && . .venv/Scripts/activate` (Windows PowerShell)
- Install deps: `pip install -r requirements.txt`
- Run server: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- Test:
  - `curl http://localhost:8000/hello`
  - `curl http://localhost:8000/goodbye`

## Git Setup (manual commands for user)

- `git init`
- `git checkout -b feat/fastapi-hello-goodbye`
- `git add .`
- `git commit -m "feat(api): add FastAPI hello/goodbye endpoints and project scaffolding"`

## Out of Scope (Deferred)

- Cloud Run configuration and CI/CD workflows
- Authentication/authorization
- Tests and linting (can be added later)

### To-dos

- [ ] Create `app/main.py` with /hello and /goodbye endpoints
- [ ] Add `requirements.txt` and document uvicorn run command in README
- [ ] Add Python-focused `.gitignore` entries
- [ ] Ensure/Update `README.md` with setup, run, and curl examples
- [ ] Create/append `PROMPTS.md` with timestamped entry for this request
- [ ] Initialize git repo, create feature branch, commit initial scaffolding