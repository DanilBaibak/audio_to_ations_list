import os
from typing import Any

from argparse import ArgumentParser
import configparser


def parse_config(config_path: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(config_path)

    return config


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        data = f.read()

    return data


def get_output_file_path(input_file_path: str, output_file_path: str) -> str:
    file_name = os.path.basename(input_file_path)
    file_name = f"{os.path.splitext(file_name)[0]}.txt"

    return os.path.join(output_file_path, file_name)


def arg_parser() -> Any:
    parser = ArgumentParser()

    parser.add_argument("input_file_path", type=str)
    parser.add_argument("output_file_path", type=str)

    return parser.parse_args()
