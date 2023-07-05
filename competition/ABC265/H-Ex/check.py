import subprocess
import os
import time


def generate_testfile_list():
    input_files = set(os.listdir("testcases/input"))
    output_files = set(os.listdir("testcases/output"))

    testcases = list(input_files & output_files)
    testcases.sort()
    return testcases


def print_result(testfile, result, expected, error, run_time):
    print("== {} ==".format(testfile))
    if error:
        print("Error!")
        print(error)
        print("")
        return

    if (result == expected):
        print("Success!")
        print("実行時間: {}秒".format(run_time))
        print()
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
            start = time.perf_counter()
            result = subprocess.run(
                ["python3", "answer.py"],
                stdin=f,
                capture_output=True,
                text=True
            )
            end = time.perf_counter()
            output = result.stdout
            error = result.stderr
        expected = subprocess.run(
            ["cat", "./testcases/output/{}".format(testfile)],
            capture_output=True,
            text=True
        ).stdout
        run_time = end - start

        print_result(testfile, output, expected, error, run_time)
        total_result &= output == expected

    print("~~~~~~~~~~~~")
    print("Total Result")
    print("Success!" if total_result else "Failure!")
