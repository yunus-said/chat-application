This is a Web Application for online chatting which is named PicChat for the time being. There are 2 versions to the application. The first one is an asynchronous version and the second one is the synchronous version. The asynchronous version has a higher level of performance according to: https://channels.readthedocs.io/en/latest/introduction.html

This is the SYNCHRONOUS version of PicChat and this can be determined by the presences of a dummy txt file called synchronous.txt. The main differnce between the 2 versions of PicChat lies in chatApp/consumers.py file.

Both the synchronous and asynchronous versions of PicChat are available on a remote GitHub repository which can be located with the following URL: https://github.com/yunus-said/chat-application.git This GitHub repository will have 2 branches:

Master branch = asynchronous version of PicChat
Synchronous branch = synchronous version of PicChat
Prerequisites for running this web application(PicChat):

Install pipenv if you don't have it: 'pip install pipenv'
Navigate through your terminal to the directory where this application's Pipfile is located and run the command 'pipenv install' to install all the requires packages and dependencies.
Install docker: https://www.docker.com/get-started
If you want to run PicChat's chat server:

Navigate through your terminal to the directory where PicChat's manage.py file and Pipfile are located. (manage.py and Pipfile will be in the same dorectory)
Run the command 'pipenv shell' to activate a python virtual environment
Run the command 'python manage.py runserver'
While the chat server is running, if you want to use or test the chat application:

Open two or more browser tabs to the url: http://127.0.0.1:8000/chat/
Enter the same chat room name on all the tabs you opened.
Send and receive messages on all the tabs.
For further reference about this web application you can look at a Django channels tutorial at: https://channels.readthedocs.io/en/latest/tutorial/index.html
