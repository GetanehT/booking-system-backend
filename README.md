# Django Restaurant Booking System

This README provides information on how to set up, configure, and run the Django-based Restaurant Booking System project. It covers everything from initial setup to detailed usage instructions for the application's features.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Application](#running-the-application)
6. [API Endpoints](#api-endpoints)
7. [Future Implementations](#future-implementations)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview

The **Restaurant Booking System** is a Django application designed to manage table reservations for a restaurant. It allows users to view existing reservations and make new reservations via a RESTful API. The application is structured with models, views, and serializers to handle data efficiently.

## Requirements

- **Python**: Version 3.8 or higher
- **Django**: 5.1.2
- **Django REST Framework**: 3.15.2
- **PostgreSQL**: or another database of your choice
- **Other dependencies**: Listed in `requirements.txt`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/booking.git
   cd booking
2. pip install -r requirements.txt

### Configuration
1. Environment Variables:

* Create a .env file in the root of your project and set the following variables:

2.Database Configuration:

* The project uses dj-database-url to configure the database. Ensure your DATABASE_URL variable points to your PostgreSQL database, such as:
  * DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME

3. Allowed Hosts:

* Modify the ALLOWED_HOSTS setting in settings.py to include your server's domain or IP, e.g.:
  python

  * ALLOWED_HOSTS = ['8000-getaneht-bookingsystemb-ln7tky9hm33.ws.codeinstitute- 
 ide.net','*.heroku.com','restaurant-booking-app-332799487776.herokuapp.com']

4. CORS Configuration:

 * The application allows all origins for development. For production, you should specify allowed origins in settings.py:
    python
   
*CORS_ALLOWED_ORIGINS = ['8000-getaneht-bookingsystemb-ln7tky9hm33.ws.codeinstitute- 
  ide.net','*.heroku.com','restaurant-booking-app-332799487776.herokuapp.com']


### Running the Application
1. Apply migrations:

* python manage.py migrate
* Create a superuser :


* Copy code
* python manage.py createsuperuser

 
3. Run the development server:


* Copy code
* python manage.py runserver
* Access the application:


### API Endpoints

 Reservation Endpoints
 
 * List All Reservations

* GET /api/reservations/

* Description: Returns a list of all reservations.

* Create a New Reservation

* POST /api/reservations/

* Request Body (JSON):

* example of usr data
{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "1234567890",
    "date": "2024-10-21",
    "time": "19:00",
    "guests": 4,
    "table": 2,
    "message": "Window seat preferred"

}

* Description: Creates a new reservation. Returns the created 
  reservation details.

* Retrieve a Specific Reservation

* GET /api/reservations/<id>/

* Description: Retrieves a reservation by its ID.

* Update a Specific Reservation

 * PUT /api/reservations/<id>/

* Request Body (JSON):
  
 json

{
    "guests": 5,
    "message": "Add a high chair"
}

* Description: Updates the specified reservation. Returns the 
  updated reservation details.

* Delete a Specific Reservation

 * DELETE /api/reservations/<id>/

* Description: Deletes the specified reservation.



Sure! Here’s a more detailed README formatted with Markdown for your Django Restaurant Booking System project:

markdown
Copy code
# Django Restaurant Booking System

This README provides information on how to set up, configure, and run the Django-based Restaurant Booking System project. It covers everything from initial setup to detailed usage instructions for the application's features.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Application](#running-the-application)
6. [API Endpoints](#api-endpoints)
7. [Future Implementations](#future-implementations)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview

The **Restaurant Booking System** is a Django application designed to manage table reservations for a restaurant. It allows users to view existing reservations and make new reservations via a RESTful API. The application is structured with models, views, and serializers to handle data efficiently.

## Requirements

- **Python**: Version 3.8 or higher
- **Django**: 5.1.2
- **Django REST Framework**: 3.15.2
- **PostgreSQL**: or another database of your choice
- **Other dependencies**: Listed in `requirements.txt`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/booking.git
   cd booking
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Configuration
Environment Variables:

Create a .env file in the root of your project and set the following variables:
plaintext
Copy code
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
Database Configuration:

The project uses dj-database-url to configure the database. Ensure your DATABASE_URL variable points to your PostgreSQL database, such as:
perl
Copy code
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
Allowed Hosts:

Modify the ALLOWED_HOSTS setting in settings.py to include your server's domain or IP, e.g.:
python
Copy code
ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']
CORS Configuration:

The application allows all origins for development. For production, you should specify allowed origins in settings.py:
python
Copy code
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
    "http://localhost:8000",
]
Running the Application
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser (optional):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Visit http://127.0.0.1:8000 in your web browser.
API Endpoints
Reservation Endpoints
List All Reservations

GET /api/reservations/
Description: Returns a list of all reservations.
Create a New Reservation

POST /api/reservations/
Request Body (JSON):
json
Copy code
{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "1234567890",
    "date": "2024-10-21",
    "time": "19:00",
    "guests": 4,
    "table": 2,
    "message": "Window seat preferred"
}
Description: Creates a new reservation. Returns the created reservation details.
Retrieve a Specific Reservation

GET /api/reservations/<id>/
Description: Retrieves a reservation by its ID.
Update a Specific Reservation

PUT /api/reservations/<id>/
Request Body (JSON):
json
Copy code
{
    "guests": 5,
    "message": "Add a high chair"
}

* Description: Updates the specified reservation. Returns the 
  updated reservation details.

* Delete a Specific Reservation

* DELETE /api/reservations/<id>/

* Description: Deletes the specified reservation.

### Future Implementations

* User Authentication: Implement user registration and *
* authentication to manage reservations by user accounts.
* Email Notifications: Send confirmation emails to users upon 
   successful reservations.
* Reservation Management: Provide an admin interface for 
   viewing and managing reservations.
* Frontend Integration: Develop a user-friendly frontend 
  interface for users to interact with the API.
* Enhanced Search Filters: Allow users to filter reservations 
  by date, time, and number of guests.

### Contributing

* If you'd like to contribute to this project, please fork the 
 repository and create a new branch for your feature or bug 
 fix. Then, submit a pull request with a description of your 
 changes.

### License
* This project is licensed under the MIT License - see the 
   LICENSE file for details.

Feel free to customize any sections or add more details as needed!

