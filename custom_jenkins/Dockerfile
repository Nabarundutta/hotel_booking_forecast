# Use the official Jenkins LTS image
FROM jenkins/jenkins:lts

# Switch to root to install dependencies
USER root

# Install Docker from Debian repositories
RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    docker.io && \
    apt-get clean

# Add Jenkins user to the Docker group
RUN groupadd -f docker && usermod -aG docker jenkins

# Create volume directory
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Switch back to Jenkins user
USER jenkins
