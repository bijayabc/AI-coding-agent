import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import call_function, available_functions

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)
    system_prompt = """
    You are a helpful AI coding agent. You are working in the repository calculator.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read the content of a file
    - Write to a file (create or update)
    - Run a Python file with optional arguments

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    # user sends prompt as first arg after filename
    if len(sys.argv) > 1:
        prompt = sys.argv[1] 
    else:
        print("Usage: python main.py 'your prompt here'")
        sys.exit(1)

    # optional second argument after prompt arg
    verbose_flag = False
    if len(sys.argv) > 2 and sys.argv[2] == '--verbose':
        verbose_flag = True
    
    # wrap prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    # pass function schemas and system prompt
    config = types.GenerateContentConfig(
        tools=[available_functions], 
        system_instruction=system_prompt
    )

    max_iters = 20
    for i in range (max_iters):
        # get initial response
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages,
            config=config
        )
        if verbose_flag:
            print('User prompt: ', prompt)
            print('Prompt token count: ', response.usage_metadata.prompt_token_count)
            print('Response token count: ', response.usage_metadata.candidates_token_count)

        # if no functions called, just return
        if not response.function_calls:
            # final agent text message
            print(response.text or "[No text response]")
            return response.text
        
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        for function_call_part in response.function_calls:
            # for every function, the model thinks it need, call it with function_call_part
            # This is where stuff happens, AI is not running code. It is returning function that it thinks should be run
            # This for loop then calls those functions which runs those lines of code via call_function
            function_call_result = call_function(function_call_part, verbose=verbose_flag)
            messages.append(function_call_result)

            if (not function_call_result.parts or not function_call_result.parts[0].function_response):
                raise Exception("empty function call result")
            
            if verbose_flag:
                print(f"-> {function_call_result.parts[0].function_response.response}")


    

if __name__=='__main__':
    main()