CS5001 Final Project: Readme<br />
Semester: Spring 2023<br />
Student: Yushi Cui<br />

<ins>Travel List project<ins>

The Travel List project is a web application that allows users to create, manage, and share their favorite travel destinations. It's built using Python with Flask as the web framework, Jinja2 for templating HTML and CSS, and MongoDB as the database to store trip information.
The application provides features such as adding new trips, editing trip details, searching for trips, and deleting trips. Users can also add comments and rate the trips, making it a comprehensive platform for sharing travel experiences and recommendations.


<ins>Code Running<ins>

To run the code, need to set up the environment by installing all the packages listed in the requirements.txt file.<br />
Then, create a .env file inside the travel_library folder to set up the MONGODB_URI with your MongoDB account:<br />
MONGODB_URI=mongodb://mongodb_user<br />
Next, create a .flaskenv file inside the Travel List folder to set up the Flask environment:<br />
FLASK_APP=travel_library<br />
FLASK_DEBUG=1<br />
Lastly, simple execute the ‘flask run’ in the terminal to run the codes.<br />


<ins>Code Testing<ins>

There are two test files in the folder:<br />
test_models.py: This file uses unittest to test the Trip class.<br />
test_app.py: This file uses pytest-flask to test all the functions in routes.py, simply execute ‘pytest’ in the terminal to run the tests.<br />


<ins>Reflection<ins>

While working on this project, I have gained a lot of new knowledge about web development using Python and Flask, also effectively applied the concepts learned in CS5001. The main learning points of the project include implementing Flask with the Jinja2 template to create a website, using Flask-wtforms for form handling and validation, integrating MongoDB with Flask using PyMongo for database operations, applying object-oriented programming principles and utilizing various data types in the project.

For the project, I like the part that implementation of object-oriented programming concepts, such as creating the Trip class as a dataclass to represent a trip, which makes the code better organized and maintainable. I also enjoyed designing the user interface using HTML and CSS, as it is quite amazing to see the functions that I wrote in the backend visually materialize in the frontend.

Since many aspects of the project were new to me, I initially struggled with understanding some Flask concepts, such as routing, request handling, and render template. Also, connecting MongoDB with Flask and managing database operations was also challenging. However, these problems were resolved through the learning and implementation process, and now I am familiar with these concepts.

For future improvements, currently the application operates on a single-user basis, I plan to update the website as a multi-user platform by adding user accounts with proper authentication, which can enhance the user experience and security. Additionally, the search functionality could be improved to support more advanced queries, filtering, and sorting options.

The Travel List project has been an excellent opportunity to develop my skills in web development using Python and Flask. It has broadened my knowledge of various tools and libraries available and has given me the confidence to tackle web applications. As a programmer, my future goal is to become a skilled web developer, this project has provided me with valuable experience and brought me closer to achieving that goal.
