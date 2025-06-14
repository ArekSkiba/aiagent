import os
from google.genai import types

def get_file_content(working_directory, file_path):
    if file_path == None:
        file_path = "."
    if not os.path.isabs(file_path):
        file_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000
    try:
        with open(file_path, "r") as f:
            content = f.read()
            if len(content) > MAX_CHARS:
                file_content_string = content[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
            else:
                file_content_string = content

        return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets content of the given file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read from, relative to the working directory."
            ),
        },
    ),
)
