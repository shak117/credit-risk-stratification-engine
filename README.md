# credit-risk-stratification-engine
Research and set up the foundational architecture required for an AI/ML application deployment workflow. The objective of this task is to understand backend API development, dashboard integration, experiment tracking, and containerized deployment practices used in modern machine learning projects.

# Architecture

# Initial Project Architecture

## Project Structure

credit-risk-stratification-engine/

├── backend/
│   └── app/
│       └── main.py
│
├── frontend/
│   └── dashboard.py
│
├── models/
├── data/
├── configs/
├── docs/
├── docker/
│   └── Dockerfile
│
├── requirements.txt
├── README.md
└── .gitignore

## Architecture Workflow

Streamlit Dashboard
        ↓
FastAPI Backend
        ↓
Machine Learning Model
        ↓
Prediction Response
        ↓
Docker Container Deployment

Environment Setup Guide
1. Clone Repository
open github created manually repo
then connected folder with repo using git init commands
________________________________________
2. Create Python Virtual Environment
Windows
python -m venv venv
Activate environment:
venv\Scripts\activate
________________________________________
3. Install Dependencies
Install required packages:
pip install fastapi uvicorn streamlit mlflow pandas numpy scikit-learn python-dotenv
________________________________________
4. Generate requirements.txt
pip freeze > requirements.txt
________________________________________
5. Run FastAPI Application
python -m uvicorn backend.app.main:app --reload
Access API:
http://localhost:8000
Swagger Documentation:
http://localhost:8000/docs
________________________________________
6. Run Streamlit Dashboard
Open new terminal and activate virtual environment.
Run:
python -m streamlit run frontend/dashboard.py
Dashboard URL:
http://localhost:8501
________________________________________
7. Docker Setup
Build Docker image:
docker build -t credit-risk-app -f docker/Dockerfile .
Run Docker container:
docker run -p 8000:8000 credit-risk-app
Application URL:
http://localhost:8000
________________________________________
8. Git Branch Workflow
Main branches used:
main
development
feature/backend-api

________________________________________
9. Technologies Used
•	FastAPI 
•	Streamlit 
•	MLflow 
•	Docker 
•	Scikit-learn 
•	Pandas 
•	NumPy 
________________________________________
10. Project Structure
backend/
frontend/
models/
data/
configs/
docs/
docker/






