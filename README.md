# command-repository
Simple, quick Flask application for creating a database of commands for use with INNBot's repositories.

**This project is a work-in-progress.**

## Quick Start
In order to use this you'll need at least Python 3 installed. It helps to have Git to clone the repository. You should create a virtual environment for the dependencies.
```
$ git clone https://github.com/davidtwco/command-repository.git
$ cd command-repository
$ python -m  venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=app
$ export FLASK_DEBUG=1
$ export COMMAND_REPO_SECRET_KEY=<secret_key>
$ python -m flask create_database
$ python -m flask run
```
Replace `<secret_key>` with a Secret Key that you've made up, I recommend generating secret keys as follows:

```python
import os
print(os.urandom(24))
```
You'll need to add the site as a repository in INNBot for it to work properly. When you start the application it should tell you the IP/Port it's running on.

## Related Projects
`command-repository` creates a JSON output that works perfectly with INNBot's repository system - check out [INNBot](https://github.com/ImperialNewsNetwork/inn-bot) if you haven't already.

## Changelog
**v1.0.0 - 30/05/2016**
- Initial Release - add and delete commands w/ help texts and responses.
