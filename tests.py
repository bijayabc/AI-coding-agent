from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print(result)

    print(run_python_file("calculator", "main.py"))
    # print(run_python_file("calculator", "main.py", ["3 + 5"]))
    # print(run_python_file("calculator", "tests.py"))
    # print(run_python_file("calculator", "../main.py"))
    # print(run_python_file("calculator", "nonexistent.py"))


    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "pkg2/temp.txt", "this should not be allowed"))

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)

if __name__ == '__main__':
    main()
