# ML1 Docker

Two ML1 bootcamp tasks: (1) automating file cleanup and text processing on Windows, and (2) running a small load-balanced Flask system in Docker.

## Key features

- **Task 1 — File cleanup & Python processing:** a Bash script moves `.log` files to an archive folder and logs the run; a Python script counts the lines in a text file — both scheduled to run daily with Windows Task Scheduler
- **Task 2 — Docker load balancing:** two Flask backend services behind a round-robin load balancer, plus a requester service, all on one Docker network — runnable with a single `docker compose` command

## Tech stack

- Bash, Python
- Docker, Docker Compose
- Flask, `requests`

## Task 1 — File cleanup and Python processing

`task1/file_cleanup.sh` moves all `.log` files from `task1/temp/` to `task1/old_files/` (creating the folders if needed) and appends a timestamped entry to `task1/log/file_cleanup.log`.

`task1/file_processor.py` reads `input.txt`, counts its lines, and writes `Number of lines: <count>` to `output.txt`.

The original setup ran these on Windows with Git Bash and Task Scheduler — the shell script daily at 1:00 AM and the Python script daily at 2:00 AM. The script paths in the repo are Windows-style (`/c/bash/task1/...`); adjust them to your own folders before scheduling.

```bash
# Run by hand
bash task1/file_cleanup.sh
python task1/file_processor.py
```

## Task 2 — Docker load balancer

Two Flask backends (`backend1.py` on port 5000, `backend2.py` on port 5001) sit behind `load_balancer.py` (port 8080), which forwards each request to the next backend in turn (round-robin). `request.py` sends 10 requests to the load balancer and prints each response.

```bash
git clone https://github.com/majidhanif230/ML1_Docker.git
cd ML1_Docker/task2
docker compose up --build
```

Then open http://localhost:8080 in a browser — each refresh should alternate between the two backends. The compose file defines the `my_network` bridge network and maps ports 5000, 5001 and 8080 to the host.

## Project structure

```
ML1_Docker/
├── README.md
├── task1/
│   ├── file_cleanup.sh      # Move .log files to old_files/, log the run
│   ├── file_processor.py    # Count lines in input.txt -> output.txt
│   ├── input.txt / output.txt
│   ├── hello.txt
│   └── log/ / old_files/ / temp/
└── task2/
    ├── docker-compose.yml           # backend1, backend2, load_balancer, requester on my_network
    ├── Dockerfile.backend1 / Dockerfile.backend2
    ├── Dockerfile.load_balancer / Dockerfile.requester
    ├── backend1.py / backend2.py    # Flask services
    ├── load_balancer.py             # Round-robin proxy on port 8080
    ├── request.py                   # Sends 10 requests to the load balancer
    └── requirements.txt             # flask, requests
```

## Author

**Majid Hanif** — AI Engineer, BS Artificial Intelligence, The Islamia University of Bahawalpur (CGPA 3.81/4.0)

- Portfolio: https://snap-portfolio-me.lovable.app/portfolio
- LinkedIn: https://www.linkedin.com/in/majid-hanif-23720b2a2/
- GitHub: https://github.com/majidhanif230
