# Use the lightweight Red Hat UBI 8 Minimal image
FROM registry.access.redhat.com/ubi8/ubi-minimal:latest

# Define build arguments for JRE version and local JRE file name
ARG JRE_VERSION=17.0.8_7
ARG JRE_BUILD=8
ARG JRE_FILE=jre-17-linux-x64.tar.gz
ARG JRE_URL=https://github.com/adoptium/temurin17-binaries/releases/download/jdk-${JRE_VERSION}%2B${JRE_BUILD}/OpenJDK17U-jre_x64_linux_hotspot_${JRE_VERSION}_${JRE_BUILD}.tar.gz

# Define environment variables
ENV JAVA_HOME=/opt/java/jre
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Install tar and gzip (needed to extract the JRE), then clean up
RUN microdnf install -y tar gzip curl && \
    mkdir -p /opt/java && \
    curl -L ${JRE_URL} -o /tmp/${JRE_FILE} && \
    tar -xvf /tmp/${JRE_FILE} -C /opt/java/ && \
    rm /tmp/${JRE_FILE} && \
    # Standardize the folder name (handles different vendor naming)
    mv /opt/java/jdk*jre /opt/java/jre || mv /opt/java/jre* /opt/java/jre && \
    # We DO NOT remove curl here to avoid the RPM dependency error
    microdnf clean all

# Create directory and extract local JRE
# ADD automatically unpacks compressed archives
# ADD files/${JRE_FILE} /opt/java/

# Rename the extracted folder to 'jre' for a consistent path
# (Check the actual folder name inside your tar.gz; it's often 'jdk-17.x.x+x-jre')
# RUN mv /opt/java/jre-* /opt/java/jre

# Verify the installation
RUN java -version

# Set a non-root user (Standard practice for UBI images)
USER 1001

# Start (or any other command you want to run)
CMD ["/bin/bash"]