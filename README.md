# EMO Energy Complaint App

## Setup Instructions

### Backend:

1.  Navigate to the `backend` directory.
2.  Create a virtual environment: `python3 -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4.  Install dependencies: `pip install -r requirements.txt`
5.  Set up Firebase: Create a Firebase project, download your service account key as `firebase_credentials.json` and place it in the `backend` directory. Replace the placeholder values in `firebase_credentials.json` with your actual credentials.
6.  Set your OpenAI API key as an environment variable: `export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"`.
7.  Run the application: `uvicorn main:app --reload`

### Frontend:

1.  Navigate to the `frontend` directory.
2.  Install dependencies: `npm install` or `yarn install`
3.  Start the application: `npm start` or `yarn start`

## Running Tests (Backend):

1.  Ensure the backend virtual environment is activated.
2.  Run tests using pytest: `pytest`

## CI/CD

CI/CD is set up using GitHub Actions.  Pushing or creating a pull request will trigger the workflows defined in `.github/workflows`.