# hooks/post_gen_project.py

env_file_path = './local-setup/generate_env.sh'

if '{{ cookiecutter.connection_type}}' != "local":
    database_url = input("Enter database URL: ")
    print(f"Database URL enteredL {database_url}")
else:
    database_url = "mongodb://localhost:27017"
    print(f"Using default database URL: {database_url}")

env_content = f"""HOST="127.0.0.1"
PORT=8000
ORIGINS="http://localhost:8080"
DATABASE_URL={database_url}
"""

with open(env_file_path, 'w') as file:
    file.write(env_content)

print(f"Updated {env_file_path}  with DATABASE_URL")
