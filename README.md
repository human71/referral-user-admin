# Flask Referral System

A simple Flask web application that implements a referral code system with user registration, an admin panel, and a SQLite database for managing and downloading user data.

## Features

- **User Registration:** Users can input their name and phone number to generate a unique referral code.
- **Admin Panel:** Password-protected admin panel to view and search user information, and download data as a CSV file.
- **Database Storage:** User information is stored in an SQLite database using SQLAlchemy.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-referral-system.git
    cd flask-referral-system
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

### User Registration

- Visit the home page and input your name and phone number.
- Click "Submit" to generate a unique referral code.

### Admin Panel

- Visit the admin login page (`http://127.0.0.1:5000/admin`) and log in with the provided credentials.
- After login, access the admin panel to view all registered users, search by referral code, and download user data as a CSV file.
- Log out from the admin panel to secure access.

## Important Note

- For educational purposes, the admin credentials are stored in the code. In a real-world scenario, use a more secure authentication method.

Feel free to explore and modify the code to suit your needs!
