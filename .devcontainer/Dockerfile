FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install Ansible and Docker CLI
RUN apt-get update && apt-get install -y \
    ansible \
    docker.io \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install the Ansible Docker collection required for your playbooks
USER vscode
RUN ansible-galaxy collection install community.docker