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

  * ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

4. CORS Configuration:

 * The application allows all origins for development. For production, you should specify allowed origins in settings.py:
    python
   
*CORS_ALLOWED_ORIGINS = ["https://yourdomain.com","http://localhost:8000",]


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

Visit http://127.0.0.1:8000 in your web browser.

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



