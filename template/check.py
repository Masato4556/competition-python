import subprocess
import os
import time


def generate_testfile_list():
    input_files = set(os.listdir(os.path.join('testcases', 'input')))
    output_files = set(os.listdir(os.path.join('testcases', 'output')))
    testcases = sorted(input_files & output_files)
    return testcases


def print_result(testfile, result, expected, error, run_time):
    print(f"== {testfile} ==")
    if error:
        print("Error!")
        print(error)
        print("")
        return

    if (result == expected):
        print("Success!")
        print(f"実行時間: {run_time: .6f}秒")
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
        input_path = os.path.join('testcases', 'input', testfile)
        output_path = os.path.join('testcases', 'output', testfile)

        with open(input_path, 'r') as f:
            start = time.perf_counter()
            result = subprocess.run(
                ["python3", "answer.py"],
                stdin=f,
                capture_output=True,
                text=True,
                check=True
            )
            end = time.perf_counter()
            output = result.stdout
            error = result.stderr

        with open(output_path, 'r') as f:
            expected = f.read()

        run_time = end - start
        print_result(testfile, output, expected, error, run_time)
        total_result &= output == expected

    print("~~~~~~~~~~~~")
    print("Total Result")
    print("Success!" if total_result else "Failure!")
