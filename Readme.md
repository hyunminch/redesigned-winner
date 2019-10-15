Mobile Computing 2019 - VideoShare
===

## Viewing Prototype 

The prototype of our application (named temporarily as VideoShare) is located in the prototype folder of this repository. The application prototype is made with [mockplus](https://www.mockplus.com/). 

Inside the prototype folder, there are the original mockplus file `VideoShare_prototype.mp`, and the `VideoShare_prototype` folder which contains the `html` rendered contents based on the `.mp` file.

The file structure looks like this:

```dockerfile
prototype/
├── VideoShare_prototype/
│   ├── app/
│   ├── assets/
│   ├── js/
│   ├── index.html
│   ├── remote.html
│   └── README.txt
└── VideoShare_prototype.mp
```

There are two ways of previewing the prototype:

1. Download the mockplus software, import `VideoShare_prototype` into it and click the play button, which will start the prototype preview display.

2. Open `index.html`in your browser by either using [GitHub & BitBucket HTML Preview](https://htmlpreview.github.io/) or your local copy. 

Once you open the prototype preview, you can interact with it like you would with a normal app.

Note that the prototype is not 100% refined. Necessary improvement suggestions are welcome.

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

