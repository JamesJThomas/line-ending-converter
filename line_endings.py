"""This file is intended to be a simple utility to convert unix line endings to dos/windows style.
I wrote this because I noticed that the output of many tools such as:
autopep8: the automatic style formatter for python
coverage: a tool for determining how much of python code is covered by unit tests
git log: a command for viewing git commit history
output their results using unix style line endings (\n)
Unfortunately, I use a screen reader (NVDA)
that expects windows style line endings (\r\n).
This means that, whenever the screen reader reads the output of one of these tools,
it is read as though it were all on one line.
This makes it very hard for me to debug when something goes wrong.
Therefore, I am writing this so I don't have to do manual reformatting
every time I am in this situation
"""


def get_file_to_convert():
    """Gets the name of the file to be converted"""
    file_to_convert = input("which file do you wish to convert?")
    return file_to_convert


def read_file(file_to_convert):
    """reads the file to be converted"""
    file_handle = open(file_to_convert, "rb")
    file_contents = file_handle.read()
    file_handle.close()
    return file_contents


def convert_endings(file_contents):
    """performs the conversion from unix style line endings to windows style"""
    modified_contents = file_contents.replace(b"\n", b"\r\n")
    return modified_contents


def write_new_contents(file_name, new_contents):
    """writes the converted contents to the file"""
    file_handle = open(file_name, "wb")
    file_handle.write(new_contents)
    file_handle.close()


def main():
    """main function"""
    file_to_convert = get_file_to_convert()
    file_contents = read_file(file_to_convert)
    modified_contents = convert_endings(file_contents)
    write_new_contents(file_to_convert, modified_contents)


if __name__ == "__main__":
    main()
