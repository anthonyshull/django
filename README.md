# ENGINEERS

Description...

## DEVELOP

The following instructions target [Debian](https://www.debian.org/) based Linux distributions.

Make sure that you have pip3 and [pipenv](https://pipenv.kennethreitz.org/en/latest/) installed:
```
%> sudo apt-get install python3-pip
%> pip3 install pipenv
```
Set necessary environment variables ([fish shell](https://fishshell.com/)):
```
%> set -x SECRET_KEY 'I_CAN_BE_ANYSTRING_I_PUT_MY_MIND_TO_I_CAN_BE_ANYSTRING_I_PUT_MY_MIND_TO'
%> set -x DEBUG 'True'
%> set -x POSTGRES_PASSWORD 'shipwell'
```
Clone this project:
```
%> git clone git@github.com:anthonyshull/engineers.git
```
Get a local instance of [Postgres](https://hub.docker.com/_/postgres):
```
%> docker run --name postgres -e POSTGRES_USER=engineers -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -p 5432:5432 -d postgres
```
Run the migrations:
```
%> pipenv shell
(engineers) %> python manage.py migrate
```
Create an API key:
```
(engineers) %> python manage.py shell
>>> from rest_framework_api_key.models import APIKey
>>> api_key, key = APIKey.objects.create_key(name="shipwell")
>>> key
```
Run the server:
```
(engineers) %> python manage.py runserver
```
Test that you can insert an engineer:
```
%> curl -H 'Content-Type: application/json' \
   -H 'X-Api-Key: *****' \
   -d '{"name":"Guido van Rossum","rank":1}' \
   http://localhost:8000/api/v1/engineers/
```
And, now you should be able to retrieve them:
```
%> curl -L -H 'X-Api-Key: *****' http://localhost:8000/api/v1/engineers/1
```
## TEST
```
%> pytest -v
```