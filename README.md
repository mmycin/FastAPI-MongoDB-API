## Python API using FastAPI and MongoDB

Here is an example of a note taking API created in Python using FastAPI framework. The database used here is MongoDB for which PyMongo library is installed. To install the requirements, run the following command:
```bash
$ pip install fastapi pydantic pymongo uvicorn
```
Quick note is that the version of your current Python should be 3.10.* or above.  The folder structure of the project is given bellow.

```directory
└── 📁NoteApp
    └── .env
    └── database.py
    └── main.py
```
Note that the repository only contains the backend of the project which is written in pure Python and does not cover any front end. To deploy the API to your app, use your favorite front end framework such as *React, Vue, Angular, Svelte, Solid, Preact, Qwik* etc. Or you can even use bare *html* or something more like *htmx* if you want. To access the data of the API, you can use Vanilla JavaScript's *browser fetch API* or any Node Module such as *Axios* if you wish. For now, we continue talking about the backend only.

A very important point is that you should have a file named `.env` that contains you environment variable such as:
```env
USER=yourname
PASSWORD=test123
```
It is necessary because the username and password from the environment variables are used in `database.py` for the connection to MongoDB. Mine is not here in the repository because for obvious reasons I am not going to publish it here publicly. So get your own username and password and setup a cluster from [MongoDB Website](https://www.mongodb.com/docs/compass/current/connect/) .

Now having everything setup, we are ready to run our API from our terminal. We have installed the **Uvicorn** package of python which will run our app and automatically watch and reload the server after changing the files. To run the app, write the following command:
```bash
$ cd path/to/your/directory
$ uvicorn main:app --reload
```
This will run your server on http://localhost:8000 . Open your terminal and run the command to see the output:
```bash
$ curl http://localhost:8000
[{"id":"66aa35e18a6f7a3a3730a67a","note":"this is a note"},{"id":"66aa36038a6f7a3a3730a67b","note":"I am another note"},{"id":"66aa37bf8a6f7a3a3730a67c","note":"here is another one"}]
```
You could use Postman or your voice of service or even your browser to test the API.
***(The End)***
