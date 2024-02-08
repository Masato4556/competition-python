import subprocess
import os
import time
import argparse

ROOT_PATH = "./competition"


def generate_question_path(main_dir, sub_dir):
    return f'{ROOT_PATH}/{main_dir}/{sub_dir}'


def generate_input_path(main_dir, sub_dir):
    question_path = generate_question_path(main_dir, sub_dir)
    return f'{question_path}/testcases/input/'


def generate_output_path(main_dir, sub_dir):
    question_path = generate_question_path(main_dir, sub_dir)
    return f'{question_path}/testcases/output/'


def generate_testfile_list(main_dir, sub_dir):
    input_path = generate_input_path(main_dir, sub_dir)
    output_path = generate_output_path(main_dir, sub_dir)
    input_files = set(os.listdir(input_path))
    output_files = set(os.listdir(output_path))

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
    parser = argparse.ArgumentParser(description='コードのテスト実行')
    parser.add_argument('main_dir')
    parser.add_argument('sub_dir')
    args = parser.parse_args()
    main_dir = args.main_dir
    sub_dir = args.sub_dir

    testfiles = generate_testfile_list(main_dir, sub_dir)

    total_result = True
    for testfile in testfiles:
        input_path = f"{generate_input_path(main_dir, sub_dir)}/{testfile}"
        output_path = f"{generate_output_path(main_dir, sub_dir)}/{testfile}"
        with open(input_path, 'r') as f:
            start = time.perf_counter()
            result = subprocess.run(
                [
                    "python3", 
                    f"{generate_question_path(main_dir, sub_dir)}/answer.py"
                ],
                stdin=f,
                capture_output=True,
                text=True
            )
            end = time.perf_counter()
            output = result.stdout
            error = result.stderr
        expected = subprocess.run(
            ["cat", output_path],
            capture_output=True,
            text=True
        ).stdout
        run_time = end - start

        print_result(testfile, output, expected, error, run_time)
        total_result &= output == expected

    print("~~~~~~~~~~~~")
    print("Total Result")
    print("Success!" if total_result else "Failure!")
