# Docker Networking Lab

## Objective
Build and verify a Flask REST API, MySQL database, and Redis cache using a custom Docker bridge network.

## Technologies Used
- Docker Desktop
- Docker networking (custom bridge)
- Python and Flask
- MySQL
- Redis
- Windows PowerShell

## Application Details
- Flask API endpoint: `http://localhost:5001/about`
- Docker network: `my-bridge-net`
- MySQL database: `devopsdb`
- Containers: Flask, MySQL, and Redis

## Implementation
1. Created the custom bridge network `my-bridge-net`.
2. Created the Flask application and Dockerfile.
3. Built the Docker image `flask-api`.
4. Started the Flask, MySQL, and Redis containers.
5. Connected all three containers to the custom network.
6. Verified the Flask API response.
7. Verified DNS resolution for `mysql` and `redis`.
8. Verified Redis using `redis-cli ping`.
9. Verified MySQL and the `devopsdb` database.

## Verification Results
- Flask API returned the expected JSON response.
- Docker DNS resolved MySQL and Redis container names.
- Redis returned `PONG`.
- MySQL listed `devopsdb` and its system databases.
- All three application containers were running on the custom network.

## Files
- `app.py` — Flask REST API
- `Dockerfile` — Flask image configuration
- `requirements.txt` — Python dependencies
- `screenshots/` — Practical evidence screenshots
