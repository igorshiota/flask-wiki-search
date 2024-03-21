# Flask Wikipedia Search Application

This Flask application allows you to perform searches on Wikipedia and cache the results in a MySQL database. It provides a simple web interface where users can enter search queries and view the search results.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Paramiko (for SSH connection)
- MySQL Connector (for MySQL database interaction)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>

2. Install the required Python dependencies using pip:

   ```bash
   pip install flask paramiko mysql-connector-python

3. Set up your MySQL database and configure the database connection details in the app.py file:

   ```bash
   # MySQL database configuration
    db_config = {
        'host': '',   # Replace with MySQL host
        'port': ,           # MySQL port
        'user': '',         # MySQL username
        'password': '',  # MySQL password
        'database': ''  # MySQL database name
    }

4. Ensure that the wiki.py script is available on the remote server specified in the app.py file.

5. Run the Flask application:

   ```bash
   python app.py

6. Access the application in your web browser at http://localhost:5001.

## Usage
   
- Enter your search query in the provided input box on the homepage.

- Click on the "Search" button to perform the search.

- The application will display the search results retrieved from Wikipedia. If the search results are already cached in the database, they will be retrieved from the cache.

## Additional Information

- The app.py file uses the wiki.py script to perform searches on Wikipedia. Ensure that the wiki.py script is available on the remote server specified in the app.py file.
- Make sure you double check the Database information, paths and other dynamic information accordingly.


