# AI Coding Agent

An intelligent AI-powered coding assistant built with Google's Gemini API that can perform file operations and execute Python code within a secure sandboxed environment.

## Overview

This AI Coding Agent leverages Google's Gemini 2.0 Flash model to provide intelligent assistance for coding tasks. It can understand natural language prompts and perform various file system operations and code execution within a controlled working directory for security.

## Features

### Core Capabilities
- **File System Operations**: List, read, and write files within the working directory
- **Code Execution**: Run Python files with optional command-line arguments
- **Security**: Sandboxed execution limited to a specified working directory
- **Interactive**: Natural language interface for all operations
- **Verbose Mode**: Optional detailed logging of operations and token usage

### Available Operations
1. **List Files and Directories** - Get information about files and directories with sizes
2. **Read File Content** - Read and display the contents of any file (with character limits)
3. **Write/Create Files** - Create new files or update existing ones
4. **Execute Python Files** - Run Python scripts with optional arguments and capture output

## Installation

### Prerequisites
- Python 3.12 or higher
- Google Gemini API key

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-coding-agent
   ```

2. Install dependencies using uv (recommended):
   ```bash
   uv sync
   ```
   
   Or using pip:
   ```bash
   pip install -e .
   ```

3. Create a `.env` file in the project root:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Configuration

The agent operates within a configurable working directory defined in `config.py`:

- **Working Directory**: `./calculator` (default)
- **Max Characters**: `1000` (for file content reading)

You can modify these settings in `config.py` to change the working directory or adjust file reading limits.

## Usage

### Basic Usage
```bash
python main.py "your natural language prompt here"
```

### Examples

**List files in the working directory:**
```bash
python main.py "show me all the files in the current directory"
```

**Read a specific file:**
```bash
python main.py "read the contents of main.py"
```

**Create or update a file:**
```bash
python main.py "create a new file called hello.txt with the content 'Hello World'"
```

**Run a Python script:**
```bash
python main.py "run the calculator.py file with arguments 5 and 3"
```

**Complex tasks:**
```bash
python main.py "create a Python script that calculates fibonacci numbers and then run it"
```

### Verbose Mode
Add `--verbose` flag for detailed operation logging:
```bash
python main.py "list all files" --verbose
```

This will show:
- Token usage statistics
- Detailed function call information
- Execution results

## Project Structure

```
ai-coding-agent/
├── main.py                 # Main entry point
├── config.py              # Configuration settings
├── call_function.py       # Function calling orchestration
├── functions/             # Available function implementations
│   ├── get_files_info.py  # List files and directories
│   ├── get_file_content.py # Read file contents
│   ├── write_file.py      # Write/create files
│   └── run_python_file.py # Execute Python files
├── calculator/            # Example working directory
│   ├── main.py           # Calculator application
│   ├── pkg/              # Calculator package
│   └── tests.py          # Calculator tests
├── pyproject.toml        # Project configuration
└── README.md            # This file
```

## Security Features

- **Sandboxed Execution**: All operations are restricted to the configured working directory
- **Path Validation**: Prevents access to files outside the working directory
- **Timeout Protection**: Python execution is limited to 30 seconds
- **File Type Validation**: Only Python files can be executed
- **Character Limits**: File reading is limited to prevent memory issues

## API Reference

### Function Schemas

The agent uses structured function calling with the following available functions:

#### `get_files_info(directory)`
Lists files and directories with metadata.

#### `get_file_content(file_path)`
Reads file contents with automatic truncation.

#### `write_file(file_path, content)`
Writes content to a file, creating directories as needed.

#### `run_python_file(file_path, args=[])`
Executes Python files with optional command-line arguments.

## Development

### Adding New Functions

To add new capabilities:

1. Create a new function file in `functions/`
2. Implement the function and its schema
3. Add the function to `call_function.py`
4. Update the available_functions list

### Testing

Run the included tests:
```bash
python tests.py
```

## Dependencies

- `google-genai==1.12.1` - Google Gemini API client
- `python-dotenv==1.1.0` - Environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions, please [create an issue](link-to-issues) in the repository.

---

**Note**: This agent is designed for development and coding assistance. Always review generated code before using it in production environments.
