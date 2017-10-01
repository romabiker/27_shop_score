# Shop Score Page

One of the key indicators of the effectiveness of the managers of the online store (call center) is the processing speed of incoming orders. If you do not have time to respond to the order within 30 minutes, it is very likely that the order will be canceled by the client.

This site reflects the current  situation of the online store
The page is updated every 10 seconds.
The score indicator changes color depending on the value:

- green - waiting time of unprocessed applications does not exceed 7 minutes
- yellow - delay no more than 30 minutes
- red - delay more than 30 minutes

Outputs additional secondary information:

- number of open orders
- number of orders processed for the current day


Quickstart
----------


Run the following commands to install project locally:

```
    # to install dependancies:
    pipenv shell
    pipenv install


    #set the ``FLASK_APP`` and ``FLASK_DEBUG`` environment variables :
    export FLASK_DEBUG=1
    export FLASK_APP=autoapp.py


    # enter db path
    export SQLALCHEMY_DATABASE_URI=path/to/score.db

    # run server and open http://127.0.0.1:5000/ page in browser
    flask run

```


Deployment
----------

Project is prepared for deployment to Heroku cloud

To deploy:

Register on Heroku

[Download and install Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

Run the following commands:

```
    heroku login
    git clone https://github.com/romabiker/27_shop_score.git
    cd 27_shop_score
    heroku create # creates application
    pipenv install #automaticaly installs all dependancies from Pipfile
    pipenv shell   # activates virtual environment

    heroku local web  # to check server locally
    git push heroku master # deploy and after that visit dashboard settings on Heroku to provide SQLALCHEMY_DATABASE_URI
    heroku ps:scale web=1 # runs project
    heroku open   # opens in browser
    heroku logs --tail # to see logging

```

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

