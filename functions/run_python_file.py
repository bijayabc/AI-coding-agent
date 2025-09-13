import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if args is None:
        args = []

    if not abs_file_path.startswith(abs_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    filename = os.path.basename(abs_file_path)
    name, extension = os.path.splitext(filename)

    if extension != '.py':
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(
            ['python3', abs_file_path, *args],
            cwd=abs_dir,
            capture_output=True,
            text=True,
            timeout=30
        )
        output_string = f'STDOUT:\n{result.stdout} \nSTDERR: {result.stderr}\n'

        if result.returncode != 0:
            output_string += f'Process exited with code {result.returncode}\n'
        
        if not result.stdout:
            output_string += f"No output produced."

        return output_string
    except subprocess.TimeoutExpired:
        return f'Error: "{file_path}" timed out after 30 seconds.'
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=(
        "Executes a Python file located in the working directory with a python3 interpreter and returns its output. "
        "This function runs the file with optional command-line arguments, captures both "
        "standard output and standard error, and enforces a timeout for safety. "
        "It only works on `.py` files inside the working directory."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    "The relative path to the Python file to execute, such as 'script.py' "
                    "or 'pkg/utilities/task.py'. Must be within the working directory."
                )
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description=(
                    "Optional list of command-line argument strings to pass to the Python file. "
                    "For example: ['--debug', 'config.json']."
                ),
                items=types.Schema(type=types.Type.STRING)
            )
        },
        # required=["file_path"]
    )
)

