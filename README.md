# corona-kh4-app
An application to fuel a project focused on analyzing data from Corona KH-4.

## Deployment
This is deployed using Render, which has very simplistic requirements. Unfortunately, one of the requirements is a requirements.txt file with the Dash version specified and gunicorn included. Versions for requirements outside of Dash are not possible to set. 

## Working on Windows
Instead of `gunicorn`, it is possible to use `waitress`. The command to invoke `waitress` is `waitress-serve --listen=127.0.0.1:8050 app:server`. Alternatively `dev_app.py` may be invoked using `python dev_app.py`. This uses `watchdog` to monitor for changes within files. If it detects a change, it will automatically restart using `waitress`. Alternatively, gunicorn can be used with WSL.

## Removing Requirement to 