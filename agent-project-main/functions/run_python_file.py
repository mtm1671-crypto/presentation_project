import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    if args is None:
        args = []
    abs_working_dir = os.path.abspath(working_directory)
    path_to_eval = os.path.abspath(os.path.join(working_directory, file_path))
    if not path_to_eval.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not path_to_eval.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    if not os.path.exists(path_to_eval):
        return f'Error: File "{file_path}" not found'
    try:
        completed_process = subprocess.run(
            ["python", path_to_eval] + args,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=abs_working_dir,
        )
        if completed_process.returncode != 0:
            return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\nProcess exited with code {completed_process.returncode}"
        return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
    except Exception as e:
        return f"Error executing python file: {e}"


schema_run_python_file = {
    "name": "run_python_file",
    "description": "Executes a Python file within the working directory and returns the output from the interpreter.",
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Path to the Python file to execute, relative to the working directory.",
            },
            "args": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional arguments to pass to the Python file.",
            },
        },
        "required": ["file_path"],
    },
}
