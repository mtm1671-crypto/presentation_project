import argparse
import os
import sys

from dotenv import load_dotenv
import anthropic

from call_function import call_function, available_tools
from constants import MAX_ITERS
from prompts import SYSTEM_PROMPT


def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Claude")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY environment variable not set")

    client = anthropic.Anthropic(api_key=api_key)
    messages = [{"role": "user", "content": args.user_prompt}]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, args.verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
            raise


def generate_content(client, messages, verbose):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8096,
        system=SYSTEM_PROMPT,
        tools=available_tools,
        messages=messages,
    )

    if verbose:
        print(f"Input tokens: {response.usage.input_tokens}")
        print(f"Output tokens: {response.usage.output_tokens}")

    # Check if we need to process tool calls
    if response.stop_reason == "tool_use":
        # Add assistant's response to messages
        messages.append({"role": "assistant", "content": response.content})

        # Process each tool use block
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                tool_result = call_function(block, verbose)
                tool_results.append(tool_result)

        # Add tool results to messages
        messages.append({"role": "user", "content": tool_results})
        return None  # Continue the loop

    # Extract text response
    for block in response.content:
        if hasattr(block, "text"):
            return block.text

    return None


if __name__ == "__main__":
    main()
