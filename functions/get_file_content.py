import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f'Error reading file: {e}'
    

schema_get_file_content = types.FunctionDeclaration(
    name='get_file_content',
    description="Reads and returns the full text content of a file in the working directory. "
        "This function is limited to files inside the working directory for security reasons. "
        "Use this to view or inspect the contents of a specific file as a string.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the file whose content should be read. "
                    "For example: 'notes.txt' or 'pkg/config.json'. "
            )
        }
    )
)
    