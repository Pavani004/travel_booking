# Flask Travel Booking System

This project is a backend Travel Booking System built using Flask. It provides RESTful APIs for user registration, authentication, and flight booking. The system uses MySQL for relational data storage, Redis for caching, JWT for authentication, and Docker for containerized deployment.

The key features include a RESTful API built with Flask, MySQL database integration using SQLAlchemy ORM, caching using Redis via Flask-Caching, JWT-based user authentication, and support for Docker and Docker Compose to simplify local development and deployment.

The project uses Python 3.10 and libraries such as Flask, Flask-JWT-Extended for authentication, Flask-SQLAlchemy for ORM, Flask-Caching for caching, along with MySQL 8 and Redis as services. Docker and Docker Compose are used to containerize the application and dependencies.

To get started, you need Docker and Docker Compose installed. First, clone the repository from GitHub using the command `git clone https://github.com/your-username/flask-travel-booking.git`, then change into the project directory. Build and start the Docker containers with `docker-compose up --build`. The Flask API server will run locally and be accessible at `http://localhost:5000`.

The database is configured to connect to a MySQL server inside a Docker container with the hostname `db`, port 3306, username `root`, password `password`, and database name `travel_db`. Redis is also configured as a caching service running inside a Docker container.

The API endpoints include:

- **POST /register**: To register a new user by providing a username and password in JSON format.  
- **POST /login**: To log in and receive a JWT access token by sending username and password.  
- **POST /book-flight**: To book a flight, requires JWT token in the Authorization header. You provide the flight number and date.  
- **GET /recent-booking**: To retrieve the most recent booking, also requires JWT token, and uses Redis caching to improve response time.

The configuration settings such as database URI, JWT secret key, and Redis cache URL are stored in the `config.py` file.

If you prefer not to use Docker, you can manually create a Python virtual environment, install the required Python packages from `requirements.txt`, and run the application after ensuring MySQL and Redis are running on your local machine.

The project is open source and licensed under the MIT License.
