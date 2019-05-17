# MindClickedFlaskNlu
Dialogue systems are forever learning applications therefore by building  simplistic and primitive application there is room to expand and add more intents as well as more entities to produce accurate results. This web application is using natural language processing in a dialogue system for mental health assessments to improve early intervention.

## Getting Started- 
#### http://www.mindclicked.com/ Full app deployed on heroku but serving through a custome bought domian. Use 'admin@mindclicked.com' for the username and '123456789' for password.

These instructions will get you a copy of the project up and running on your local machine or on the server. Testing purposes. See installing and deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things do we need to install the software and how to install them
Flask, Python, Rasa.

Alternatively, run

```
pip install -r requirements.txt
``` 

Just in case you are running it in Pycharm, you can save it in a requirement.txt file and pycharm recognises it 


### Installing and Procedure - Start to Finish

A server will be required A step by step series of examples that will tell us how to get the development env running and arrive at the final Application

After making sure all the Prerequisites are installed, the rasa page contains a step by step guide to install the the Rasa Nlu and how to run a the server. Also select the training data

```
data
models
README.md
app.py
database.py
MCdb.db
models.py
forms.py
requirement.txt
knowledge.py
vs_url_for.py
	tests
	---|
	   |
	   --- basic_test.py
		user_test.html
		 db_test.html     
	templates
	---|
	   |
	   --- layout.html
		login.html
		 register.html
	  	  chat.html
	staic/css
	---|
	   |
	  --- style.css
		    cover.css
            ../js
	         ---|
	            |
	          --- main.js
		    
```


## Runing the App

To view this app on your local machine. Simply download the project, open the app.py file, edit the last line(see below) & go to your bash and run the app
```
if __name__ == '__main__':
    app.run(debug=True)
```
OR
```
python app.py
```

this will start port8080 and it can be viewed on http://127.0.0.1:8080/



## Built With

* [Flask](http://flask.pocoo.org/docs/0.12/) - Micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine
* [Bootstrap](https://getbootstrap.com/docs/3.3/getting-started/) - HTML, CSS, and JS framework
* [SQLite](https://www.sqlite.org/index.html) - A single file relational database bundled with most standard Python installs
* [RASA](https://rasa.com/) - The Rasa Stack is a set of open source machine learning tools for developers to create contextual text- and voice-based chatbots and assistants.


## Authors

* **Sylvester Mbeah** -  At this point I have added all the necessary files and database and the app can be viewed on http://www.mindclicked.com
