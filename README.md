# WDP
WebDrP

📜 Documentation for Med-Snap
In the root directory (./), there is a file named CODEOWNERS, which defines the responsible reviewers for Python and JavaScript code.

1️⃣ Installation of GitHub
    1.1 Installing Git on Windows
    Download Git from the official website: Git for Windows.

    https://git-scm.com/downloads/win

Install Git by following the setup instructions.
Verify the installation by opening CMD (Command Prompt) or Git Bash and running:

    git --version

✅ Expected output:

    $ git --version
    git version 2.47.1.windows.2
    
(The version number may be different depending on the latest Git release.)
    
1.2 Installing Git on Linux
    Open a terminal and update your package list:
            
    sudo apt update
    
Install Git:
    
    sudo apt install git

Verify the installation

    git --version

✅ Expected output:

    git --version
    git version 2.47.1

(The version number may be different and possibly newer.)

2️⃣ Setting Up GitHub
    2.1 Initialize Git in Your Project
    First, create a new folder where you will store your project locally.
    Navigate to the folder and open a Bash terminal.
    2.2 Initialize Git
    Run the following command to initialize Git in your project:

    git init

To confirm Git has been initialized, check for the .git directory:

    ls -al

✅ Expected output:

    drwxr-xr-x 1 boris 197611 0 Jan 30 14:50 .git/

2.3 Add a Remote Repository
    Run the following command, replacing YOUR-TOKEN with your personal access token:
    
    git remote add origin https://YOUR-TOKEN@github.com/BorisIsacWebTechDev/Med-Snap-Backend.git
    
2.4 Verify the Remote Repository
    Check if everything worked by running:
    git remote -v

✅ Expected output:

    origin  https://YOUR-TOKEN@github.com/BorisIsacWebTechDev/Med-Snap-Backend.git (fetch)
    origin  https://YOUR-TOKEN@github.com/BorisIsacWebTechDev/Med-Snap-Backend.git (push)

2.5 Confirm Permissions
    Check with the administrator if you have the necessary permissions to contribute to the repository.
2.6 Clone the Repository
    To get a local copy of the repository, run:

    git clone https://github.com/BorisIsacWebTechDev/Med-Snap-Backend.git

⚠️ IMPORTANT: Best Practices

    ✔ Always create a new branch based on the main branch before starting your work.
    
    ✔ Use meaningful commit messages to describe your changes clearly.
    
    ✔ Push your changes regularly to avoid losing progress.
    
    ✔ Follow the repository guidelines for code style and structure.


Install and Create a Virtual Environment

1️⃣ Install Virtual Environment
Open a terminal and type:
    
    pip install virtualenv
    
2️⃣ Create a Virtual Environment
    
Run the following command in the terminal:

    python -m venv <my_venv>

exemple:

    python -m venv venv

In my case an environment will be named "venv".

Activate a Virtual Environment
Windows:

    <relative_path_to_venv>\venv\Scripts\activate

Linux/macOS:

    source <relative_path_to_venv>/venv/bin/activate

Now your virtual environment is active! On your bash should write name of your Environment before username
in my case my env is VENV and it shows me  
    
    (venv) <username> MINGW64 ~/<absolute_path_to_project> (<branch_name>)


Installation of dependencies:
Into Med-Snap-Backend, we have a requirements.txt
Run installation from requirements.txt with command 

    pip install -r requirements.txt

in terminal.
A position on terminal should be in Med-Snap-Backend. 
It will install all dependencies in your Virtual Environment

Postgres PSQL:

After installing PostgreSQL (psql), we need to create a superuser using the command:
    
    "CREATE ROLE spawnkid19xxsnap WITH SUPERUSER LOGIN PASSWORD 'your_password';

Into folder secret_folder in psql_Boris_data.py file insert in variable psql_password = 'your_password'
('your_password' is pass witch you indicate while created a superuser spawnkid19xxsnap)

After installing PostgreSQL (psql), we need to create a superuser using the following command:

    CREATE ROLE spawnkid19xxsnap WITH SUPERUSER LOGIN PASSWORD 'your_password';

Then, in the psql_Boris_data.py file inside the secret_folder, insert the password into the psql_password variable:

psql_password = 'your_password'
('your_password' is the password you set when creating the superuser spawnkid19xxsnap.) 
    
This superuser is created for testing and permissions. Additionally, this user is stored in the secret_files as the main user.

Now, let's grant permissions on the local machine using:
    
    ALTER USER spawnkid19xxsnap CREATEDB CREATEROLE;
    
To verify if the user exists, run:
    
    "\du"

After that, create a database named "snap".

    CREATE DATABASE <db_name>;

Now it is time to import the database file.
If you are still inside the psql terminal, exit by typing:

    \q

Then, in your terminal or command line, run:

    "psql -U spawnkid19xxsnap -d snap -W -f '<path_to_db>/mydb_backup.sql'"
    
👉 Replace <path_to_db> with the actual path to your .sql file.

Insert a password for the superuser spawnkid19xxsnap.

And finally run project.

Navigate to Your Django Project
    Open a terminal and move into your project directory: "cd /path/to/your/django_project"
    Your position should be in the same level with file "manage.py". then Run server with command "python manage.py runserver" or
    "python3 manage.py runserver" if you use linux.
    Open browser and insert a next link http://127.0.0.1:8000/ this link should redirect you to index page





# Docker and Docker-Compose
Before you start, install Docker and Docker Compose. Download the installation file from the official Docker website: https://www.docker.com/. Click on Download Docker Desktop, select your operating system, and click the download button.

The installation process is very easy, so I won’t describe it in detail. 😊

Don't forget that on Windows, Docker Desktop should be running before you start working with it.

When you clone the project from GitHub, it contains three important files at the same level as manage.py:

-   Dockerfile – Describes, step by step, what Docker should do.
-   docker-compose.yml – Manages communication between two containers and runs them.

# Steps to Run the Project with Docker

Open a terminal and navigate into the psychology folder.

Run ls (Linux/macOS) or dir (Windows) to confirm that your current working directory (PWD) is at the same level as manage.py.

In the terminal, run:

    docker compose up
Wait while Docker downloads all dependencies automatically.

Once the setup is complete, open a browser and go to:

http://127.0.0.1:8000/

This should redirect you to the index page. 🚀


# Books_APP DRF

Add to URL http://127.0.0.1:8000/ URI from table for teste it

|Action	            |HTTP Method	    |URL                |
|-------------------|-------------------|-------------------|
|List all books	    |GET	            |api/v1/books/      |
|Retrieve a book	|GET	            |api/v1/{pk}/books/ |
|Create a book	    |POST	            |api/v1/books/      |
|Update a book	    |PUT/PATCH  	    |api/v1/{pk}/books/ |
|Delete a book	    |DELETE	            |api/v1/{pk}/books/ |