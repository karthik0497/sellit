import os
import subprocess
import sys

# Setup path to import py_logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from py_logging.py_logging import log_app

def run_command(command, cwd=None, env=None):
    """Run a shell command and handle errors."""
    log_app(f"Running: {command}")
    try:
        subprocess.check_call(command, cwd=cwd, env=env, shell=True)
    except subprocess.CalledProcessError as e:
        log_app(f"Error executing command: {command}", level="error")
        sys.exit(1)

def main():
    venv_dir = os.path.join(BASE_DIR, "venv")
    requirements_file = os.path.join(BASE_DIR, "requirements.txt")
    
    # 1. Create virtual environment if it doesn't exist
    if not os.path.exists(venv_dir):
        log_app(f"Creating virtual environment in {venv_dir}...")
        run_command(f"{sys.executable} -m venv venv", cwd=BASE_DIR)
    else:
        log_app(f"Virtual environment already exists in {venv_dir}.")

    # 2. Install requirements
    if os.path.exists(requirements_file):
        log_app("Installing requirements...")
        # Use simple activator or direct path to pip
        pip_cmd = os.path.join(venv_dir, "bin", "pip")
        run_command(f"{pip_cmd} install -r requirements.txt", cwd=BASE_DIR)
    else:
        log_app("requirements.txt not found, skipping installation.")

    # 3. Set environment variables (mimicking Docker)
    env = os.environ.copy()
    env["PYTHONPATH"] = BASE_DIR
    
    log_app("\nEnvironment setup complete.")
    log_app(f"PYTHONPATH set to: {BASE_DIR}")
    log_app("To run your application, activate the venv and run your entry point.")

if __name__ == "__main__":
    main()
