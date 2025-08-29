import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    path1 = os.path.abspath(working_directory)
    path2 = os.path.abspath(full_path)
    if path2.startswith(path1):
        try:
            if os.path.isfile(path2):
                with open(path2, "r") as file:
                    content = file.read(MAX_CHARS)
                if os.path.getsize(path2) > MAX_CHARS:
                        return content + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                else:
                    return content
            else:
                return f'Error: File not found or is not a regular file: "{file_path}"'
        except Exception as e:
            return f"Error: {e}"
    else:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'