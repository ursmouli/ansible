## Create image
`docker build --build-arg TOMCAT_VER=9.0.115 -t ubi8-minimal-tomcat:9 .`

## Run container
`docker run -d -p 8080:8080 --name my-tomcat-server ubi8-minimal-tomcat:9`

## Runtime (Flexible)
```
docker run -d -p 8080:8080 \
  -v /path/to/your/app.war:/opt/tomcat/webapps/app.war:Z \
  ubi8-tomcat:10
```

## Follow logs
`docker logs -f my-tomcat-server`  

## Check stats (CPU/Memory)
`docker stats my-tomcat-server`