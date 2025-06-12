import os
import subprocess

def run_python_file(working_directory, file_path):

    original_file_path = file_path

    if file_path == None:
        file_path = "."
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{original_file_path}" as it is outside the permitted working directory'
    
    if os.path.dirname(file_path) and not os.path.exists(file_path):
        return f'Error: File "{original_file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{original_file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python3", file_path],
            capture_output=True, 
            cwd=working_directory, 
            timeout=30, 
            text=True
        )
        output = f"STDOUT:{result.stdout} \n STDERR:{result.stderr} \n"
        if result.returncode != 0:
            output +=  f"Process exited with code {result.returncode}"
        
        if output.strip():
            return output 
        else:
            return "No output produced."
        
    except Exception as e:
        return f'Error: executing Python file: {e}'
