# Tiny URL

This web demo is used for shortiing long, complex URL to tiny URL. This project was built on Django framework and SQLite databse.
### How does it work?
When user enter a URL, the server will generater 5 digits random characters which map to original URL. After creating a new mapping relationship, server will save it into SQL database. So server can read the random string directly next time.
### Deploy
This web demo was deployed on Heroku Cloud plantform. We didn't set our own hostname. So the final tiny URL may include long random host name.
Demo: https://young-lowlands-79935.herokuapp.com/
