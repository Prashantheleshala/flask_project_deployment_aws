Regex Matcher Web Application

This project is a web application developed using Flask, a Python web framework, that replicates the core functionality of the popular website regex101.com. 
The application allows users to input a test string and a regular expression (regex) and displays all the matches found. 
Additionally, it provides a feature to validate email addresses.

Features:
Regex Matching:
Users can input a test string and a regex pattern.
Upon submission, the application matches the regex pattern against the test string and displays all the matches found.

Email Validation:
Users can input an email address.
The application validates whether the provided email address is valid or not according to a predefined regex pattern.

Project Structure:

app.py:
Initializes the Flask application.
Defines routes for handling user requests and form submissions.
Utilizes Python's re module for regex matching and email validation.

templates Directory:
Contains HTML templates used for rendering the user interface.
index.html: The main HTML template that displays the input forms for regex matching and email validation, as well as the output of the matches and email validation results.

How to Use:
Clone the repository to your local machine.
Install Flask if not already installed (pip install Flask).
Run the Flask application by executing python app.py.
Access the application in your web browser by navigating to localhost:5000.
Input test strings and regex patterns to find matches or validate email addresses.

Additional Notes:
The application is designed to be simple and user-friendly, with a clean interface.
Error handling is implemented to handle empty input fields and invalid email addresses.
The application can be further extended with additional regex features or improvements in the user interface.

Deployment:
The application has been deployed on the AWS Cloud to make it accessible to users remotely. Users can access the application by visiting the provided URL.(BUT AS I AM USING FREE AWS IT WOULD BE AVAILABLE FOR LONG)

Technologies Used:
Python
Flask
HTML
CSS

Feel free to contribute to the project or provide feedback for further enhancements!
