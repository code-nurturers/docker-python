# Example Python Docker App
- Demonstrates to learners how to use Docker to spin up a MySQL db, seed it with data then connect to it with Python when it is healthy

## Getting Started
- install Docker Desktop
- clone the project
- run `docker compose up --build` from your terminal
- look at output in terminal for the query results or the docker desktop logs

## Notes
- if you change the init.sql script need to run `docker compose down -v` to delete it from volumes