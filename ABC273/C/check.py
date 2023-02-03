import subprocess
import os

def generate_testfile_list():
    input_files = set(os.listdir("testcases/input"))
    output_files = set(os.listdir("testcases/output"))

    testcases = list(input_files&output_files)
    testcases.sort()
    return testcases

def print_result(testfile, result, expected, error):
    print("== {} ==".format(testfile))
    if error:
        print("Error!")
        print(error)
        print("")
        return

    if (result == expected):
        print("Success!\n")
    else:
        print("Failure!")
        print("<result>")
        print(result)
        print("<expected>")
        print(expected)
        print("")

if __name__ == '__main__':
    testfiles = generate_testfile_list()

    total_result = True
    for testfile in testfiles:
        with open('./testcases/input/{}'.format(testfile), 'r') as f:
            result = subprocess.run(["python3", "answer.py"], stdin=f, capture_output=True, text=True)
            output = result.stdout
            error = result.stderr
        expected = subprocess.run(["cat", "./testcases/output/{}".format(testfile)], capture_output=True, text=True).stdout
        
        print_result(testfile, output, expected, error)
        total_result &= output == expected

    print("~~~~~~~~~~~~")
    print("Total Result")
    print("Success!" if total_result else "Failure!")
        
