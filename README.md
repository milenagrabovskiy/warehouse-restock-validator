## Set up a virtual environment
    - cd into project root directory (`warehouse-restock-validator/` in this repo)
    - Run the following command in your terminal:
        Create a virtual environment:
```bash
python3 -m venv .venv
```
            
        Activate the virtual environment in Mac os:
```bash
source .venv/bin/activate
```

        Activate the virtual environment in Windows (Command Prompt):
```cmd
.venv\Scripts\activate
```

        Activate the virtual environment in Windows (PowerShell):
```powershell
.venv\Scripts\Activate.ps1
```

## Install dependencies
    -From the project root directory (`warehouse-restock-validator/` in this repo):
        - Run the following command to install dependencies specified in pyproject.toml:
```bash
pip install -e .
```
        - To install optional dependencies (such as pytest), run the following command:
```bash
pip install -e ".[dev]"
```
            
            if imports are still redlined, ensure you have selected the correct python interpreter.
        - If the correct interpreter is selected, and import are still unrecognized, go to file -> invalidate caches 


## Run test suite
        Pytest detects test files automatically by search for files starting with `test_` or ending with `_test`
        To run the test suite, run the following command:
```bash
pytest
```

