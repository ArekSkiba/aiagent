import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    if directory == None:
        directory = "."
    if not os.path.isabs(directory):
        directory = os.path.join(working_directory, directory)
    if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    list_of_contents = []
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                list_of_contents.append(f"- {item}: file_size={os.path.getsize(item_path)}, is_dir=False")
            else:
                list_of_contents.append(f"- {item}: file_size={os.path.getsize(item_path)}, is_dir=True")
            
        return "\n".join(list_of_contents)
    except Exception as e:
        return f'Error: {str(e)}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

    
