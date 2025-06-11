import os

def write_file(working_directory, file_path, content):

    if file_path == None:
        file_path = "."
    if not os.path.isabs(file_path):
        file_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        parent_dir = os.path.dirname(file_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        with open(file_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'