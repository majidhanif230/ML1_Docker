# File Cleanup and Python Processing

## Overview

This setup involves automating two tasks on a Windows system using Git Bash and Task Scheduler:

1. **File Cleanup**: The `file_cleanup.sh` script manages `.log` files by moving them to a designated directory and logging the action.
2. **Python Processing**: The `file_processor.py` script reads a text file, counts the number of lines, and writes the count to another file.

## `file_cleanup.sh` Script

### What Happens When the Script Runs

1. **Directory Check and Creation**:
   - **Old Files Directory**: Checks if the directory `/c/bash/task1/old_files` exists. If not, it creates this directory.
   - **Log Directory**: Ensures the directory `/c/bash/task1/log` exists or creates it if necessary.

2. **File Movement**:
   - Moves all `.log` files from `/c/bash/temp/log` to `/c/bash/old_files`. Errors are suppressed if no `.log` files are found.

3. **Logging**:
   - Records an entry in `/c/bash/task1/log/file_cleanup.log` with a timestamp indicating that files have been moved.

### Automated Execution

- **Task Scheduler**: A task is configured to run the `file_cleanup.sh` script daily at 1:00 AM.
  - The task uses `bash.exe` from Git Bash with the command:

    -c "/C:\bash\task1/file_cleanup.sh"
    

## `file_processor.py` Script

### What Happens When the Script Runs

1. **File Reading**:
   - Reads the contents of `input.txt`.

2. **Line Counting**:
   - Counts the number of lines in `input.txt`.

3. **File Writing**:
   - Writes the line count to `output.txt`.

### Automated Execution

- **Task Scheduler**: A task is configured to run the `file_processor.py` script daily at 2:00 AM.
  - The task uses `python.exe` to execute the script. If using a virtual environment, ensure it is activated.

## Result

- **File Management**: `.log` files are moved to `/c/bash/old_files` and logged in `/c/bash/log/file_cleanup.log`.
- **Python Processing**: The line count of `input.txt` is written to `output.txt`.
- **Automated Execution**: 
  - The shell script runs daily at 1:00 AM.
  - The Python script runs daily at 2:00 AM, ensuring both tasks are performed automatically without manual intervention.


# Task 2 (Docker Project):

## Overview

This Docker project sets up a containerized environment with multiple services including a load balancer, backend services, and a requester service. The project utilizes Docker to build and run these services in isolated containers, connected through a shared network.

## Project Structure

### Dockerfiles

- **`Dockerfile.load_balancer`**: Defines the image for the load balancer service.
- **`Dockerfile.backend1`**: Defines the image for backend service 1.
- **`Dockerfile.backend2`**: Defines the image for backend service 2.
- **`Dockerfile.requester`**: Defines the image for the requester service.

### Python Files

- **`backend1.py`**: Code for backend service 1.
- **`backend2.py`**: Code for backend service 2.
- **`load_balancer.py`**: Code for the load balancer service.
- **`requester.py`**: Code for the requester service.

### Docker Network

- **Network Name**: `my_network`.

## Build and Run Instructions

1. **Create Docker Network**:
   
    docker network create my_network

2. **Build Docker Images**:

    docker build -t load_balancer -f Dockerfile.load_balancer .
    docker build -t backend1 -f Dockerfile.backend1 .
    docker build -t backend2 -f Dockerfile.backend2 .
    docker build -t requester -f Dockerfile.requester .

3. **Run Docker Containers**:

    docker run -d --name backend1 --network my_network backend1
    docker run -d --name backend2 --network my_network backend2
    docker run -d --name load_balancer --network my_network load_balancer
    docker run -d --name requester --network my_network requester

## Project Workflow

1. **Setup Network**: Create a Docker network named `my_network`.
2. **Build Images**: Build Docker images for each service using the corresponding Dockerfiles.
3. **Run Containers**: Launch the containers for each service, ensuring they are connected to the `my_network`.
