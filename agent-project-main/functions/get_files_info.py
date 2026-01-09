import os


def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    path_to_eval = os.path.abspath(os.path.join(working_directory, directory))
    if not os.path.isdir(path_to_eval):
        return f'Error: "{directory}" is not a directory'
    if not path_to_eval.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    try:
        files_info = []
        for filename in os.listdir(path_to_eval):
            filepath = os.path.join(path_to_eval, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = {
    "name": "get_files_info",
    "description": "Lists files in the specified directory along with their sizes, constrained to the working directory.",
    "input_schema": {
        "type": "object",
        "properties": {
            "directory": {
                "type": "string",
                "description": "The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            },
        },
        "required": [],
    },
}
