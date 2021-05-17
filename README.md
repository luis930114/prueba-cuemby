 ## fifa API for cuemby
 
 Django project with API REST for insert and get fifa players and their teams.

## Getting Started

1) Clone project from 
2) Open a terminal and install prerequisites
3) Change .env.example for .env and change user and db name

## Prerequisites

1) Python 3.7+
2) Virtualenv
3) Django
4) django-rest-framework

## Deployment 

1) Open a terminal into the project directory
2) Run command python manage.py migrate for create tables in database
3) Run command python manage.py runserver for deploy development server

## EndPoints 

1) localhost:8000/api/v1/load/
	- GET: load players in database
	
2) localhost:8000/api/v1/team/
	- POST:  Get the players of a team
	
3) localhost:8000/api/v1/player/
	- GET:  Search for players that contain the String in the player name fields

		
## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Pip](https://pypi.org/project/pip/) - Package Management
* [Postgres](https://www.postgresql.org/) - Database used

## Contributing

Please read (https://github.com/luis930114/prueba-cuemby) for details on our code of conduct, and the process for 
submitting pull requests to us.

## Authors

* **Luis Felipe Hernandez Gomez**

## License

This project is licensed under the MIT License

