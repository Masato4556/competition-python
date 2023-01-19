import subprocess
import os

def generate_testfile_list():
    input_files = set(os.listdir("testcases/input"))
    output_files = set(os.listdir("testcases/output"))

    testcases = list(input_files&output_files)
    testcases.sort()
    return testcases

def print_result(testfile, result, expected):
    print("== {} ==".format(testfile))
    if (result == expected):
        print("Success!")
    else:
        print("Failure!")
        print("<result>")
        print(result)
        print("<expected>")
        print(expected)

if __name__ == '__main__':
    testfiles = generate_testfile_list()

    total_result = True
    for testfile in testfiles:
        with open('./testcases/input/{}'.format(testfile), 'r') as f:
            result = subprocess.run(["python3", "answer.py"], stdin=f, capture_output=True, text=True).stdout
        expected = subprocess.run(["cat", "./testcases/output/{}".format(testfile)], capture_output=True, text=True).stdout
        
        print_result(testfile, result, expected)
        total_result &= result == expected

    print("~~~~~~~~~~~~")
    print("total result")
    print("Success!" if total_result else "Failure!")
        