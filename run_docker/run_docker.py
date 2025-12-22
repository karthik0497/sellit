import os
import subprocess
import sys

# Setup path to import py_logging
# run_docker.py is in sellit/sellit/run_docker/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from py_logging.py_logging import log_app

def run_command(command, cwd=None, env=None):
    """Run a shell command and handle errors."""
    log_app(f"Running: {command}")
    try:
        subprocess.check_call(command, cwd=cwd, env=env, shell=True)
    except subprocess.CalledProcessError:
        log_app(f"Error executing command: {command}", level="error")
        sys.exit(1)

def main():
    docker_dir = os.path.join(BASE_DIR, "run_docker")
    compose_file = os.path.join(docker_dir, "docker-compose.yml")
    
    if not os.path.exists(compose_file):
        log_app(f"Error: {compose_file} not found.", level="error")
        return

    log_app("Starting Docker containers...")
    # Running from BASE_DIR, pointing to the compose file
    run_command(f"docker compose -f {compose_file} up --build", cwd=BASE_DIR)

if __name__ == "__main__":
    main()
