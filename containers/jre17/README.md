## Create image
`docker build -t custom-ubi8-minimal-jre:17 .`

## Run container
`docker run --rm custom-ubi8-minimal-jre:17 java -version`