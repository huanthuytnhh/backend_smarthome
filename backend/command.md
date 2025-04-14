# Terminal Commands for Django Project Setup

## Setting Up the Django Project

### Step-by-Step Commands:

1. **Create a Virtual Environment**:

   - Run the following command to create a virtual environment named `env`:
     ```bash
     python -m venv env
     ```

2. **Activate the Virtual Environment**:

   - Depending on your terminal, use one of the following commands:
     - **Command Prompt (cmd):**
       ```cmd
       env\Scripts\activate.bat
       ```
     - **PowerShell:**
       ```powershell
       .\env\Scripts\Activate.ps1
       ```
     - **Git Bash:**
       ```bash
       source env/Scripts/activate
       ```

3. **Install Required Dependencies**:

   - Install all required Python packages listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Start a New Django Project**:

   - Create a new Django project named `backend`:
     ```bash
     django-admin startproject backend
     ```

5. **Navigate to the Project Directory**:

   - Move into the newly created project directory:
     ```bash
     cd backend
     ```

6. **Create a New Django App**:

   - Create a new Django app named `api`:
     ```bash
     python manage.py startapp api
     ```

## Notes

- Ensure you have Python and Django installed before running these commands.
- Replace `env` with your desired virtual environment name if different.

## Modifications to `settings.py`

### Added Features:

1. **Environment Variables**:

   - Integrated `python-dotenv` to load environment variables using `load_dotenv()`.

2. **CORS Configuration**:

   - Enabled cross-origin requests by adding the following settings:
     ```python
     CORS_ALLOWED_ALL_ORIGINS = True
     CORS_ALLOW_CREDENTIALS = True
     ```

3. **Installed Apps**:

   - Added the following apps to `INSTALLED_APPS`:
     ```python
     INSTALLED_APPS = [
         ...existing apps...
         'api',
         'rest_framework',
         'corsheaders',
     ]
     ```

4. **Middleware**:

   - Added `CorsMiddleware` to the middleware stack:
     ```python
     MIDDLEWARE = [
         'corsheaders.middleware.CorsMiddleware',
         ...existing middleware...
     ]
     ```

## Running the Server

### Step-by-Step Commands:

1. **Make Migrations**:

   - Detect changes in models and prepare them for migration:
     ```bash
     python manage.py makemigrations
     ```

2. **Apply Migrations**:

   - Apply all migrations to the database:
     ```bash
     python manage.py migrate
     ```

3. **Run the Development Server**:

   - Start the Django development server (default URL: `http://127.0.0.1:8000/`):
     ```bash
     python manage.py runserver
     ```
