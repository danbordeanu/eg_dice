## Synopsis

This will provide a container running dices

## Motivation

Just for fun :D

## Installation

### Dependencies

Docker 17.* must be installed and running on your MAC. More info [here](https://docs.docker.com/docker-for-mac/install/)

### Building the image

Inside of folder where Dockerfile is located, run:

```
docker build -t eg_dice .
```

### Starting container

After image is build, in order to start a dice container:

```
docker run -d --name test_dice_2 -p 5001:5000 eg_dice
```



### Stopping containers

```
docker ps -a
docker stop container_name
```

### Removing containers

```
docker rm container_name/id
```

**!!!NB!!!**

If container is running, use ```-f``` param.

#### Deleting images

```
docker rmi eg_java8 -f
```

## Running the dices

From terminal
```
curl -i -H "secretkey:1234" http://localhost:5001/api/dice
```

The response could be something like:

```
TTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 193
Server: Werkzeug/0.11.15 Python/2.7.13
Date: Fri, 07 Jul 2017 12:44:31 GMT

<!doctype html>
<html>
   <body>

      <h1>You diced 2!</h1>

           <img src='/static/dice2.jpg'>


        <h1>you won, package delivered</h1>

   </body>
```

For more graphical users, please take a look on [postaman app](https://www.getpostman.com/)

## Debugging docker server

### Connecting to docker server in MACOSX

```
screen -L -dmS docker ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/tty
```

```
screen -r
```

### Docker logs

```
#tail -f /var/log/docker.log
```


## Contributors

