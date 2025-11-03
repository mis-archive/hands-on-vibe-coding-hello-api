# Hands-On Practice: Intro to Vibe Coding with Cursor
This project will show you how to correctly structure a vibe-coded application using Cursor.

Use the Cursor app for this project.

# Create a Workspace
- Create a new, empty directory `hello_api` on your computer in a location that makes sense
-   Directory CANNOT be a subdirectory of another directory that has a Git repository
- Open that directory in Cursor (this creates a *workspace*)

# Add Project Rules to Cursor

## Prompt Logging

- Add a project rule named `log_prompts` with the following instructions

```
- Create a `PROMPTS.md` file at the root level of the project if it is not already created
- Log each prompt given to the agent as a time-stamped entry in the `PROMPTS.md` file
```

## Git Rules
- Add another project rule named `git_rules`
```
- Ensure there is a README.md file at the root of the project that contains instructions on how to execute the program
    
- Update the `README.md` file if needed every time the application itself is updated
  
- Ensure you create a new Git branch every time you make edits to the code
  ```

# Planning Mode: Basic Python API
- Enter "Plan Mode" in Cursor and describe your plan such that the agent can build the application. Use the following instructions
```
Create a Python-based API using FastAPI with two endpoints. 'hello' responds with a casual hello message. 'goodbye' responds with a casual goodbye message of your choice.

This project will require a local Git repository.

The API will be deployed to Google Cloud Run via a connection to GitHub. Add whatever files are necessary to support this.
```

# ... Let 'er Rip!
- Submit the plan to Cursor and answer any followup questions it asks

# Save the Plan
- The plan generates a markdown file that (for some reason) IS NOT STORED in your project repository
- Create a `plans` subdirectory in the `.cursor` directory
- Manually copy the `plan.md` file into the `.cursor/plans` directory
- Ensure the plan is staged in your local Git repository

# Finishing Up
- Create a private remote repository in GitHub
- Commit your local repository and push it to GitHub
- We'll pick up with this in the next class

---

# Run the FastAPI service locally

## Setup (Windows PowerShell)
- Create and activate a virtual environment:
  - `python -m venv .venv`
  - `. .venv/Scripts/Activate.ps1`

- Install dependencies:
  - `pip install -r requirements.txt`

## Start the server
- Run with auto-reload on port 8000:
  - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

## Try the endpoints
- `curl http://localhost:8000/hello`
- `curl http://localhost:8000/goodbye`