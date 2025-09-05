import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    path1 = os.path.abspath(working_directory)
    path2 = os.path.abspath(full_path)
    dir_name = os.path.dirname(path2)
    
    if path2.startswith(path1):
            try:
                if os.path.isfile(path2):
                    with open(path2, "w") as f:
                        f.write(content)
                else:
                    os.makedirs(dir_name, exist_ok=True)
                    if os.path.isdir(path2):
                        return f'Error: "{file_path}" is a directory'
                    else:
                        with open(path2, "w") as f:
                            f.write(content)
            except Exception as e:
                return f"Error: {e}"
    else:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description ="Write contents to a file relative to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content that will be written to the file"
            )
        },
    ),
)