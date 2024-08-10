import argparse
import os

def parser_arguments():
    parser = argparse.ArgumentParser(
        prog = "miso",
        description = "TBD",
        epilog = "TBD"
    )

    subparser = parser.add_subparsers(title = "subcommand")
    # storing url paths
    save_parser = subparser.add_parser("save", help = "save an url path")
    save_parser.add_argument(type=str, dest="operands")
    save_parser.set_defaults(func=save_input_url)

    args = parser.parse_args()
    return args

def save_input_url(args):
    url_path = args.operands
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "url_storage.txt")
    with open(file_path,"a") as file:
        file.write(url_path + "\n")
