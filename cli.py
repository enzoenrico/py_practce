import argparse
import os
import subprocess
from colorama import init, Fore, Style

init()

TEMPLATE_CODE = open("main.py", "r").read()
print(TEMPLATE_CODE)

TEST_CODE = open("main.test.py", "r").read()
print(TEST_CODE)


class ProgrammingQuiz:
    def __init__(self):
        self.workspace_dir = "quiz_workspace"
        self.score = 0

    def setup_workspace(self):
        if not os.path.exists(self.workspace_dir):
            os.makedirs(self.workspace_dir)

        with open(f"{self.workspace_dir}/main.py", "w") as f:
            f.write(TEMPLATE_CODE)
        with open(f"{self.workspace_dir}/test_main.py", "w") as f:
            f.write(TEST_CODE)

    def run_tests(self):
        try:
            result = subprocess.run(
                [
                    "pytest",
                    f"{self.workspace_dir}/test_main.py",
                    "-v",
                    "--color=yes",  # Force color output
                    "--capture=no",  # Show print statements
                    "--tb=short",  # Shorter traceback
                    "-ra",  # Show extra test summary
                ],
                capture_output=True,
                text=True,
            )
            return result.returncode == 0, result.stdout
        except Exception as e:
            print(f"{Fore.RED}Error running tests: {e}{Style.RESET_ALL}")
            return False, ""

    def start_quiz(self):
        print(f"{Fore.GREEN}Welcome to the Programming Quiz!{Style.RESET_ALL}")
        self.setup_workspace()
        print(f"\nYour workspace is ready at: {self.workspace_dir}")
        print(
            "Edit main.py to solve the problems, then run 'quiz test' to check your solutions"
        )


def main():
    parser = argparse.ArgumentParser(description="Programming Quiz CLI")
    parser.add_argument("command", choices=["start", "test"], help="Command to execute")

    args = parser.parse_args()
    quiz = ProgrammingQuiz()

    if args.command == "start":
        quiz.start_quiz()
    elif args.command == "test":
        success, output = quiz.run_tests()
        if success:
            print(f"{Fore.GREEN}All tests passed! Congratulations!{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Some tests failed. Keep trying!{Style.RESET_ALL}")
            print(output)


if __name__ == "__main__":
    main()
