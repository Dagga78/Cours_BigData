# Build

### Build an image from the Dockerfile in the current directory and tag the image
	* docker build -t myimage:1.0 .
docker build -t myimage:1.0 .
### List all images that are locally stored with the Docker Engine
	* docker image ls
docker image ls
### Delete an image from the local image store
	* docker image rm alpine:3.4
docker image rm alpine:3.4

# Share

### Pull an image from a registry
	* docker pull myimage:1.0
docker pull myimage:1.0
### Retag a local image with a new image name and tag
	* docker tag myimage:1.0 myrepo/myimage:2.0
docker tag myimage:1.0 myrepo/myimage:2.0
### Push an image to a registry
	* docker push myrepo/myimage:2.0
docker push myrepo/myimage:2.0
