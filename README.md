# Seek For Humanoid - server

This is the server side code of Seek For Humanoid. The app is running on Heroku and provides an API with 3 endpoints:

- https://boiling-journey-35582.herokuapp.com/api/humanoids for humanoids listing and searching functionalities
- https://boiling-journey-35582.herokuapp.com/api/humanoids/{:id} for single humanoid details
- https://boiling-journey-35582.herokuapp.com/api/countries for the list of all available countries

## Run and Testing

### Prerequisites

To run the app locally you need these tools:

- Python 3.9.5 installed
- Poetry 1.1.11 installed
- a fakeJSON token

## Run

After you have cloned the project cd into the created folder and install the dependencies:

```
$ poetry install
```

then create the database:

```
$ poetry run python manage.py migrate
```

Now run the following command to populate the database with humanoids and download the images for each profile:

```
$ FAKE_JSON_TOKEN=<YOUR_FAKE_JSON_TOKEN> poetry run python manage.py pullhumanoids
```

then you can run the server and test the API:

```
$ poetry run python manage.py runserver
```

## Test

```
$ poetry run python manage.py test
```
