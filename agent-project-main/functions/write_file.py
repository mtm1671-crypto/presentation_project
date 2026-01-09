import os


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    path_to_eval = os.path.abspath(os.path.join(working_directory, file_path))
    if not path_to_eval.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        dir_path = os.path.dirname(path_to_eval)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        with open(path_to_eval, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"


schema_write_file = {
    "name": "write_file",
    "description": "Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Path to the file to write, relative to the working directory.",
            },
            "content": {
                "type": "string",
                "description": "Content to write to the file.",
            },
        },
        "required": ["file_path", "content"],
    },
}
