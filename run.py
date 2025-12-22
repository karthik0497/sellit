import sys
import os

# Add the current directory to path so we can import the submodules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from run_local import run_local
    from run_docker import run_docker
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

def main():
    print("Select run mode:")
    print("1. Local Run")
    print("2. Docker Run")
    
    try:
        choice = input("Enter choice (1 or 2): ").strip()
    except EOFError:
        print("\nNo input provided (non-interactive mode). Exiting.")
        return
    except KeyboardInterrupt:
        print("\nCancelled.")
        return

    if choice == "1":
        print("Starting Local Run...")
        # We need to make sure we are not recursively adding paths or messing up imports
        run_local.main()
    elif choice == "2":
        print("Starting Docker Run...")
        run_docker.main()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
