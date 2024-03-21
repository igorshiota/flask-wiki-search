task1:

- Lab 7 review
- https://pythonbasics.org/flask-http-methods/
- https://stackoverflow.com/questions/22947905/flask-example-with-post
- https://www.geeksforgeeks.org/flask-http-methods-handle-get-post-requests/

Challenges:

This was fairly ok to me, my main challenges or errors at first were more on basic syntax,
like indentation (still getting me at times), I also had an issue with port 5000 still being in use
even after closing the previous project I was on, so I had to manually specify a different port
(5001 in this case). Other small things like not placing the templates in the correct directory,
but quickly amended.

task2:

- https://stackoverflow.com/questions/52394543/e-unable-to-locate-package-python3-pip
- https://www.odoo.com/forum/help-1/how-to-install-pip-in-python-3-on-ubuntu-18-04-167715
- https://askubuntu.com/questions/15447/save-an-edited-file-in-nano-but-no-permissions#:~:text=Just%20open%20a%20new%20tab,change%20ownership%20back%20to%20root.

Challenges:

Had a bit of an issue installing python3-pip from the Assignment PDF, after some research, it worked
by running the command sudo apt install python3-pip instead of sudo apt install python3-pip3, which was
giving me an error of "cannot find package".

I had created the wiki.py into my home directory, but couldn't save it due to permissions,
so I had to chmod 777 on the file to proceed.

Had difficulties running the wiki.py from the Flask application at first, so tested running it
directly from the EC2 instance and that worked, meaning it was properly set up. In the end the issue
was that I was incorrectly addressing the path of the wiki.py in my EC2. It took me to add some
console prints to debug further.

task3:

- https://stackoverflow.com/questions/78172805/flask-app-in-my-host-machine-connecting-to-an-mysql-in-a-docker-in-a-vm/78175143#78175143
- https://planetscale.com/learn/courses/mysql-for-python-developers/building-a-flask-app-with-mysql/connecting-to-the-planetscale-database
- https://www.w3schools.com/python/python_mysql_getstarted.asp

Installed Flask-MySQL to make sure our Flask app can connect to our MySQL in the VM. Since we had 
configured our VM to receive connections from our host machine via it's Network configuration:
MySQL TCP 127.0.0.1 Host Port 7703 Guest Port 6603

Main challenges were making the connection between the machines a full circle, 
so host + VM in Virtual Box + EC2, very interesting challenge. I was very confused on which host ip or port to use
as the concepts were a bit confusing. For example, I had to use my localhost ip (127.0.0.1) instead of the actual
MySQL's container's IP, which I thought was the host in this case (meaning the container is hosting MySQL, and not
my host machine hosts MySQL) but I guess I was wrong.