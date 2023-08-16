# ControlProduct
## Initial setup FastAPI

Initialize the Poetry and add its requirements:

```bash
poetry init
poetry add fastapi
poetry add uvicorn[standard]
poetry add motor
```

## FastApi + MongoDB

```bash
docker run --name database-api 
    -e MONGO_INITDB_ROOT_USERNAME=salon 
    -e MONGO_INITDB_ROOT_PASSWORD=Salon123 
    -e MONGO_INITDB_DATABASE=test 
    -p 27017:27017 
    -d mongo:latest

```

## Database

```bash
cd db
docker build -t salon-control-db .
docker run -p 27017:27017 -d salon-control-db
```

## API

```bash
cd api
docker build -t salon-api .
docker run -p 8000:8000 -d salon-api
```

# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!