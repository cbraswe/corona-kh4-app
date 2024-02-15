# CORONA KH-4 Application
An application to fuel a project focused on analyzing data from Corona KH-4. It is be automatically deployed to [braswell.tech](https://www.braswell.tech) with a new version tag.

## Archivist, Local Historian, Hiker, or End User with Additional Crash Information or Context?
Please open an [issue and provide as much context as possible](https://github.com/cbraswe/corona-kh4-app/issues/new)! 

## Local Developer Set-up
- Poetry is used for package management and establishing project requirements. Packages can be installed by using `poetry install` in the directory. 
- Ruff is used for linting and formatting, and the linting/formatting can be manually checked with `ruff check src` and `ruff format src`.
- Pre-commit is used for managing pre-commit hooks. `pre-commit install` will create the hooks, which include hooks for ruff.
- Notebook output is filteerd by establishing a `config` for git: `git config filter.strip-notebook-output.clean 'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR`
- Windows users can use `gunicorn app:server` from WSL to start the application or install `waitress` and use `waitress-serve --listen=127.0.0.1:8050 app:server`.
- `dev_app.py` uses `watchdog` to monitor changes, and it will automatically restart the application when changes are detected.

