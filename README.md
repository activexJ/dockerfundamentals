Sample app to show case docker fundamentals along with docker swarm

Stack
1. Python
2. Redis
3. Docker

Setup
1. Install docker 
2. Setup redis instance for non docker-compose setup
3. Register an account in hub.docker.com
4. Run docker build -t <<IMAGENAME>>:<<TAG>> to build the image
5. Login to docker by running docker login
6. Push the built image to docker hub by running docker push <<IMAGENAME>>:<<TAG>> 
7. Run docker run -it -e  <<IMAGENAME>>:<<TAG>> -d to start the app


Docker compose 
1. Run docker-compose up