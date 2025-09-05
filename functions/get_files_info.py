import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    fod = []
    path1 = os.path.abspath(full_path)
    path2 = os.path.abspath(working_directory)
    if path1.startswith(path2):
        try:
            if os.path.isdir(path1):
                entries = os.listdir(path1)
                for items in entries:
                    item_path = os.path.join(path1, items)
                    try:
                        fod.append(f"-{items}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}")
                    except Exception as e:
                        return f"Error: {e}"
            else:
                return f'Error: "{directory}" is not a directory'
        except Exception as e:
            return f'Error: {e}'
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    return "\n".join(fod)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description ="Lists files in the specified directory along with their sizes, constrained to the working directory.",
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