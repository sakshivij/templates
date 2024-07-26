#!/bin/bash

# Define the .env file contents
ENV_CONTENT=$(cat <<EOF
HOST="127.0.0.1"
PORT=8000
ORIGINS="http://localhost:8080"
DATABASE_URL="mysql+pymysql://foobar:foobar@localhost/{{cookiecutter.database_name}}"
EOF
)

# Create or overwrite the .env file with the defined contents
echo "$ENV_CONTENT" > .env

# Optional: Confirm the file creation
echo ".env file has been created with the following contents:"
cat .env
