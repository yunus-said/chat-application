This is a Web Application for online chatting which is named PicChat for the time being.
There are 2 versions to the application. The first one is an asynchronous version and
the second one is the synchronous version. The asynchronous version has a higher level
of performance according to:
https://channels.readthedocs.io/en/latest/introduction.html

This is the ASYNCHRONOUS version of PicChat and this can be determined by the presences
of a dummy txt file called asynchronous.txt. The main differnce between the 2 versions
of PicChat lies in chatApp/consumers.py file.

Both the synchronous and asynchronous versions of PicChat are available on a remote
GitHub repository which can be located with the following URL:
https://github.com/yunus-said/chat-application.git
This GitHub repository will have 2 branches:
1. Master branch      = asynchronous version of PicChat
2. Synchronous branch = synchronous version of PicChat

Prerequisites for running this web application(PicChat):
1. Install pipenv if you don't have it: `pip install pipenv`
2. Navigate through your terminal to the directory where this application's Pipfile
   is located and run the command `pipenv install` to install all the requires
   packages and dependencies.
3. Install docker: https://www.docker.com/get-started
4. Run `docker run -p 6379:6379 -d redis:5`

If you want to run PicChat's chat server:
1. Navigate through your terminal to the directory where PicChat's manage.py file
   and Pipfile are located. (manage.py and Pipfile will be in the same dorectory)
2. Run the command `pipenv shell` to activate a python virtual environment
3. Run the command `python manage.py runserver`

While the chat server is running, if you want to use or test the chat application:
1. Open two or more browser tabs to the url: http://127.0.0.1:8000/chat/
2. Enter the same chat room name on all the tabs you opened.
2. Send and receive messages on all the tabs.

For further reference about this web application you can look at a Django channels
tutorial at: https://channels.readthedocs.io/en/latest/tutorial/index.html

`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
To run PicChat with a react front end:
1. Navigate through your terminal to get inside the frontend directory.
2. Install either npm or yarn JavaScript package managers from:
    npm (recommended): https://nodejs.org/en/download/
    yarn: https://yarnpkg.com/getting-started/install
3. Install parcel from: https://parceljs.org/getting_started.html or run one of
   these commands for either npm or yarn:
    npm (recommended): `npm install -g parcel-bundler`
    yarn: `yarn global add parcel-bundler`
4. Create a package.json file in your project directory using:
    npm (recommended): `npm init -y`
    yarn: `yarn init -y`
5. Run the command `npm install --save-dev @babel/core @babel/plugin-proposal-class-properties @babel/preset-react`
6. Run the command `npm install --save react react-dom`
7. Run the command `npm start` (8:48)
