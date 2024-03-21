from flask import Flask, render_template, request
import paramiko
import mysql.connector
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search_query')

    # MySQL database configuration
    db_config = {
        'host': '<your-mysql-host>',   # Replace with MySQL host
        'port': '<your-mysql-host>',           # MySQL port
        'user': '<your-mysql-user>',         # MySQL username
        'password': '<your-mysql-pw>',  # MySQL password
        'database': '<your-mysql-db>'  # MySQL database name
    }

    try:
        # Connect to MySQL database
        db_connection = mysql.connector.connect(**db_config)
        db_cursor = db_connection.cursor()

        # Check if search query exists in the database
        db_cursor.execute("SELECT result FROM cache_flask WHERE query = %s", (search_query,))
        cached_result = db_cursor.fetchone()

        if cached_result:
            # If cached result exists, return it
            response = cached_result[0]
        else:
            # If no cached result, perform search on Wikipedia
            response = perform_wikipedia_search(search_query)

            # Cache the search result in the database
            db_cursor.execute("INSERT INTO cache_flask (query, result) VALUES (%s, %s)", (search_query, response))
            db_connection.commit()

        db_cursor.close()
        db_connection.close()

        return render_template('search.html', search_query=search_query, result=response)

    except mysql.connector.Error as e:
        logger.error("Error connecting to MySQL database: %s", e)
        return render_template('error.html', error_message="Failed to connect to the database")

def perform_wikipedia_search(search_query):
    try:
        instance_ip = "<your-instance-ip>"
        securityKeyFile = "/path/to/privkey.pem/"

        logger.info("Attempting SSH connection...")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file(securityKeyFile)
        client.connect(hostname=instance_ip, username="ubuntu", pkey=key)
        logger.info("SSH connection successful!")

        cmd = f"python3 /home/wiki.py '{search_query}'"
        stdin, stdout, stderr = client.exec_command(cmd)
        stdin.close()
        output = stdout.read().decode('utf-8')  # Get the output and decode it
        client.close()

        logger.info("Output from Wikipedia search:")
        logger.info(output)  # Log the output for debugging

        return output

    except Exception as e:
        logger.error("Error performing Wikipedia search: %s", e)
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

