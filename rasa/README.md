## To run rasa in docker 
docker run -v $(pwd):/app rasa/rasa:3.1.0-full init --no-prompt
->((-v $(pwd):/app) mounts your current working directory to the working directory in the Docker container)
->(rasa/rasa:3.1.0-full) rasa docker image name with tag
->(init) refers to rasa init,here rasa removed cause we are in rasa docker image.

##