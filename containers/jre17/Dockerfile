# Use the lightweight Red Hat UBI 8 Minimal image
FROM registry.access.redhat.com/ubi8/ubi-minimal:latest

# Define build arguments for JRE version and local JRE file name
ARG JRE_VERSION
ARG JRE_FILE

# Define environment variables
ENV JAVA_HOME=/opt/java/jre
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Install tar and gzip (needed to extract the JRE), then clean up
RUN microdnf install -y tar gzip && \
    microdnf clean all

# Create directory and extract local JRE
# ADD automatically unpacks compressed archives
RUN mkdir -p /opt/java
ADD files/${JRE_FILE} /opt/java/

# Rename the extracted folder to 'jre' for a consistent path
# (Check the actual folder name inside your tar.gz; it's often 'jdk-17.x.x+x-jre')
RUN mv /opt/java/jre-${JRE_VERSION}* /opt/java/jre

# Verify the installation
RUN java -version

# Set a non-root user (Standard practice for UBI images)
USER 1001

# Start (or any other command you want to run)
CMD ["/bin/bash"]