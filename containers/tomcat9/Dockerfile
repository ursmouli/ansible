# Start from the base image you just created
FROM custom-ubi8-minimal-jre:17

# Define the Argument (Default value provided if not passed)
ARG TOMCAT_VER=9.0.82

# Set environment variables
ENV CATALINA_HOME=/opt/tomcat \
    PATH=$PATH:/opt/tomcat/bin

# Switch to root to install Tomcat
USER root

# Install requirements and Tomcat
# Using microdnf to keep it slim
RUN microdnf install -y tar gzip shadow-utils && \
    microdnf clean all

# Create directory and ADD the local Tomcat tarball
RUN mkdir -p $CATALINA_HOME

# Add the local Tomcat tar.gz file and extract it to the desired location
# ADD automatically extracts the .tar.gz into the destination
ADD files/apache-tomcat-${TOMCAT_VER}.tar.gz /opt/

RUN mv /opt/apache-tomcat-${TOMCAT_VER}/* $CATALINA_HOME && \
    rm -rf /opt/apache-tomcat-${TOMCAT_VER}

# Security: Remove default apps and set permissions
RUN rm -rf $CATALINA_HOME/webapps/* && \
    chown -R 1001:0 $CATALINA_HOME && \
    chmod -R g+rw $CATALINA_HOME

# Switch back to non-root user for security
USER 1001

# Expose the default port for Tomcat
EXPOSE 8080

# Start Tomcat
CMD ["/opt/tomcat/bin/catalina.sh", "run"]