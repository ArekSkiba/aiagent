import os

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