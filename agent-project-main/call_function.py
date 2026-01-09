from functions.get_file_content import get_file_content, schema_get_file_content
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import schema_write_file, write_file
from constants import WORKING_DIR

available_tools = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
]


def call_function(tool_use_block, verbose=False):
    function_name = tool_use_block.name
    tool_input = tool_use_block.input
    tool_use_id = tool_use_block.id

    if verbose:
        print(f" - Calling function: {function_name}({tool_input})")
    else:
        print(f" - Calling function: {function_name}")

    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if function_name not in function_map:
        return {
            "type": "tool_result",
            "tool_use_id": tool_use_id,
            "content": f"Error: Unknown function: {function_name}",
        }

    args = dict(tool_input)
    args["working_directory"] = WORKING_DIR
    function_result = function_map[function_name](**args)

    return {
        "type": "tool_result",
        "tool_use_id": tool_use_id,
        "content": str(function_result) if function_result else "Success",
    }
