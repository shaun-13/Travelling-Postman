Welcome to The Travelling Postman! Here are the steps for you to run our service. 

Setup:
Unzip the files to any location you like
Start your WAMP Server

Setting up the databases:
Open phpmyadmin, import and execute each of the .sql files in the sql folder.

Start the microservices:
To run microservices using Docker, see below. Otherwise, you may continue with the following steps.

Open 6 cmd windows and cd into the app folder
Run one of these commands in one cmd window respectively:
python composite_preOrders.py
python confirmedOrders.py
python notification.py
python notification-2.py
python PreOrder.py
python User.py

Configuring Alias:
Click on the WAMP tray icon and select Apache → Alias directories → Add an alias.
Type in ‘ESD’ 
Copy the file path to the unzipped app folder, e.g. C:/Users/taylor/Documents/GitHub/Travelling-Postman/app
WAMP should restart. You can now access the app at http://localhost/ESD/app/login.html

Login:
Log in through facebook using credentials: 
	Email: avakauzjfc_1583592929@tfbnw.net 
	Password: esdisthebest

Sign up for Telegram Notification
IMPORTANT: Click on ‘Sign up for notifications’ on the top right and follow the steps.
You can now create or join preorders (PayPal credentials below). 

When joining a Preorder:
Login to Paypal using credentials:
	Email: sb-zyxov1187741@personal.example.com
	Password: MG@6pgvG



DOCKER: 
Allow remote access to database: 
(i) Open phpMyAdmin and click User Accounts.
(ii) Click ‘Add user account’ and specify the following: 
Username: is213
Hostname: %
Password: No password
(iii) Select ‘Data’ and click Go

Run commands: 
	docker build -t <dockerid>/preorder:1.0.0 .
	docker build -t <dockerid>/user:1.0.0 .
	docker build -t <dockerid>/confirmedOrders:1.0.0 .
	docker build -t <dockerid>/composite_Preorders:1.0.0 .
	docker build -t <dockerid>/notification:1.0.0 .

In the VS Code terminal, run the containers by entering the following commands:
For Preorder: 
docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/preorder <dockerid>/preorder:1.0.0
For User:
docker run -p 5002:5002 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/user <dockerid>/user:1.0.0
For Confirmed Orders:
docker run -p 5003:5003 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/confirmed_order <dockerid>/confirmedOrders:1.0.0
For Notification: 
docker run -p 5005:5005 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/notification <dockerid>/notification:1.0.0
For Join Preorder composite service: 
docker run -p 5001:5001 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/composite_preorders <dockerid>/composite_Preorders:1.0.0
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Thank you!
- G3T7