# GoogleAPITestProject
## Environment Setup
You can set up environment with:
```
cd <project directory>
python3 -m venv env
source env/bin/activate
pip install -r <path to project directory>/requirements.txt
```

## Running Tests
You can set access token into configuration file for tests execution by running the script:
```
cd <project directory>
python3 get_access_token.py
```
You can run all tests with:
```
cd <path to project directory>

pytest tests/
or
pytest --access_token <access_token> tests/
```
