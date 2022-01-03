import os


def main():
    for k, v in os.environ.items():
        print(f"{k}={v}")
