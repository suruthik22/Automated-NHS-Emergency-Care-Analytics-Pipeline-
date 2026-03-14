import subprocess
import sys

def run_step(script):
    print(f"\n Running {script}...")
    result=subprocess.run([sys.executable,f"src/{script}"])

    if result.returncode!=0:
        print(f"Error running {script}")
        exit(1)

if __name__=="__main__":
    print("Starting NHS data pipeline")

    run_step("extract_data.py")
    run_step("process_data.py")
    run_step("load_to_sqlite.py")

    print("\n Pipeline executed successfully")