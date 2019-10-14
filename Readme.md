Mobile Computing 2019
===

## Using pipenv 

### Install pipenv
On macOS,
```
brew install pipenv
```

On Ubuntu,
```
sudo apt install pipenv
```

### Install
```
pipenv install
```

This will install python frameworks onto your virtual python workspace.

### Activate Shell
```
pipenv shell
```
Activate the python workspace. You'll now have access to all the python dependencies you've installed using `pipenv install`.

## Running the server
```
cd videosharex
python manage.py runserver
```

The server will be running on `127.0.0.1:8000`. Open your web browser and access the server!
