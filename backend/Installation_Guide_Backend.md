# Installation Guide for Backend

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment support (`python3-venv` package on Debian/Ubuntu systems)

## Steps to Install and Run the Backend

1. **Install `python3-venv` Package** (if not already installed):

   ```bash
   sudo apt install python3.10-venv
   ```

2. **Create a Virtual Environment**:

   ```bash
   python3 -m venv env
   ```

3. **Activate the Virtual Environment**:

   ```bash
   source env/bin/activate
   ```

4. **Install Required Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**:

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

6. **Run the Development Server**:

   ```bash
   python3 manage.py runserver
   ```

## Notes

- If you encounter the error `The virtual environment was not created successfully because ensurepip is not available`, install the `python3-venv` package using the following command:

   ```bash
   sudo apt install python3.10-venv
   ```

   Then recreate the virtual environment and proceed with the installation steps.
