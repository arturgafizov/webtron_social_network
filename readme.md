![GitHub](https://img.shields.io/github/license/bandirom/DjangoTemplateWithDocker?style=plastic)
![Codecov](https://img.shields.io/codecov/c/gh/bandirom/DjangoTemplateWithDocker?style=plastic)

### How to use:

#### Clone the repo:

    git clone https://github.com/arturgafizov/webtron_social_network.git 
    

#### Before running add your superuser email/password and project name in docker/prod/env/.data.env file

    SUPERUSER_EMAIL=example@email.com
    SUPERUSER_PASSWORD=secretp@ssword
    MICROSERVICE_TITLE=Social network

#### Run the local develop server:

    docker-compose up -d --build
    docker-compose logs -f
    
##### Server will bind 8000 port. You can get access to server by browser [http://localhost:8090](http://localhost:8000)


#### Configuration for develop stage at 9000 port:
    docker-compose -f prod.yml -f prod.dev.yml up -d --build


#### To check the application tests
Run command:

    docker-compose exec social_network coverage run manage.py test

#### View the test coverage report app 
Run command:

    docker-compose exec social_network coverage report -m
