# JetSmart QA Automation Project

## Requirements

To run this project, you'll need Python version 3.9. You'll also need pipenv.

Once you cover both requirements, you should go to project's root directory and run following command:

`pipenv install`

This will create a python virtual env and it will also install all dependencies.

### Installing new dependencies

If you need to install new dependencies, you should run following command:

`pipenv install <library>`

This will  install the new library you need in the project virtualenv, and it will also update Pipfile and Pipfile.lock files, adding the new dependency to the project.

Then, the rest of your partners, will need to run again:

`pipenv install`

to update the projects dependencies.

## Running tests

To run all tests of the project you will need to run following command:

`pipenv run python -m pytest`