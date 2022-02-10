# python_good_practices
This project is a minimal template for python projects to develop software with good practices

The code quality is enforced using Git Hooks that run before each commit. To setup the project use
the following commands

 * create a virtual env:
  ```console
  python -m venv .venv
  ```

 * activate virtual env
  ```console
  source venv/bin/activate -> Unix
  .\venv\Scripts\activate-> Windows
  ```

 * install dependencies (Here we use `requirements.txt` but it could be better to use a dependecy manager such as `pipenv` or `poetry`)
  ```console
  pip install --upgrade pip
  pip install -r requirements.txt
  ```

 * setup git hooks
  ```console
  pre-commit install
  ```
