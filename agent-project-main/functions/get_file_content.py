import os

from constants import MAX_WORDS


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    path_to_eval = os.path.abspath(os.path.join(working_directory, file_path))
    if not path_to_eval.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(path_to_eval):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(path_to_eval, "r") as f:
            file_content_string = f.read(MAX_WORDS)
        return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"


schema_get_file_content = {
    "name": "get_file_content",
    "description": "Reads and returns the content from a specified file within the working directory.",
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The path to the file whose content should be read, relative to the working directory.",
            },
        },
        "required": ["file_path"],
    },
}
