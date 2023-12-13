# User Service

Documentation: 
FastAPI: https://fastapi.tiangolo.com
Streamlit: https://docs.streamlit.io/

## Getting started


## Requirements
Python 3.8+

### Create Environment
`pip install virtualenv`

`python -m venv env`

`source env/bin/activate`

### Install Libraries in a Virtual Environment
`pip freeze > requirements.txt`

### Requirements File
`pip install -r requirements.txt`

## Run FastAPI
`uvicorn main:app --reload --port 8080`
## Documentation Swagger RestAPI
`http://127.0.0.1:8080/redoc`


## Visualization UI with streamlit
`streamlit run visualization.py --server.port 8000`

## View Visualization Record 
Open file: video-visualization.webm


