import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    path1 = os.path.abspath(working_directory)
    path2 = os.path.abspath(full_path)
    new_args = ['python3', path2]
    new_args.extend(args)
    if path2.startswith(path1):
        if os.path.exists(path2):
            if path2.endswith('.py'):
                try:
                    completed_process = subprocess.run(new_args, timeout=30, capture_output=True)
                    out = f"STDOUT: {completed_process.stdout.decode('utf-8').strip()}"
                    err = f"STDERR: {completed_process.stderr.decode('utf-8').strip()}"
                    code = completed_process.returncode
                    output_parts = []
                    if completed_process.stdout.decode('utf-8').strip():
                        output_parts.append(out)
                    if completed_process.stderr.decode('utf-8').strip():
                        output_parts.append(err)
                    if code != 0:
                        output_parts.append(f"Process exited with code {code}")
                    final = " ".join(output_parts)
                    if not final and code == 0:
                        final = "No output produced."
                    return final
                except Exception as e:
                    return f"Error: executing Python file: {e}"
            else:
                return f'Error: "{file_path}" is not a Python file.'
        else:
            return f'Error: File "{file_path}" not found.'
    else:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'