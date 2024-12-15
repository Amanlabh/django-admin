# Assignment Using Django

This repository contains the code for the Django-based assignment. Follow the instructions below to set up the project locally and run the server.

## 1. Clone the Repository

To clone this repository on your local machine, open your terminal and run the following command:

```bash
git clone https://github.com/Amanlabh/assignment-using-Django.git  # Clone the repository
cd assignment-using-Django  # Navigate to the project directory
2. Set Up Your Django Project Locally
Create a Virtual Environment (Optional but Recommended)
It’s recommended to create a virtual environment to keep your project dependencies isolated. 
```
For Linux/MacOS, run:
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment
```
```bash
For Windows, run:


python -m venv venv  # Create a virtual environment
venv\Scripts\activate  # Activate the virtual environment
Install Dependencies
After activating the virtual environment, install the required dependencies:

```
```bash
pip install -r requirements.txt  # Install project dependencies
```
3. Run the Django Development Server
Once the environment is set up, you can run the Django development server with the following command:

```bash
python manage.py runserver  # Start the Django server
The development server will run at http://127.0.0.1:8000/. You can visit this URL in your browser to view the project.
```

4. Access the Django Admin Panel
To access the Django Admin Panel, you need to create a superuser account. Run the following command:

```bash
python manage.py createsuperuser  # Create a superuser account
```
Follow the prompts to set up the admin credentials (username, email, and password).

After creating the superuser, you can access the admin panel at:

http://127.0.0.1:8000/admin

Log in with the superuser credentials you just created.

5. Additional Notes
Make sure you have Python installed (preferably Python 3.8+).
If you face any issues during setup, make sure all dependencies are correctly installed.
markdown
Copy code

### Summary of Sections:
1. **Clone the Repository**: Cloning the repository and navigating into the project directory.
2. **Set Up Virtual Environment**: Instructions to set up a virtual environment for isolation of dependencies.
3. **Install Dependencies**: How to install all project dependencies using `pip`.
4. **Run the Server**: Instructions to run the Django development server and view the site locally.
5. **Django Admin Panel**: Creating a superuser to access Django's admin panel.

This `README.md` should be enough to help anyone set up and run your project on their local machine. If you have any questions or need further assistance, feel free to reach out to the instructor or TAs.