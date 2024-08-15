import argparse
import os
import webbrowser
from urllib.parse import urlparse

def parser_arguments():
    parser = argparse.ArgumentParser(
        prog = "miso",
        description = "TBD",
        epilog = "TBD"
    )

    subparser = parser.add_subparsers(title = "subcommand")

    # reading url paths
    read_parser = subparser.add_parser("read", help = "open all the stored url paths")
    read_parser.add_argument("-ls", "--list", action ="store_true")
    read_parser.set_defaults(func=read_files_url)

    # storing url paths
    save_parser = subparser.add_parser("save", help = "save an url path")
    save_parser.add_argument("operands")
    save_parser.set_defaults(func=save_input_url)

    # removing url paths
    remove_parser = subparser.add_parser("rm", help = "remove an url path")
    remove_parser.add_argument("operands")
    remove_parser.set_defaults(func=remove_url_input)

    args = parser.parse_args()
    return args

def read_files_url(args, list = False):
    urls = []

    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "url_storage.txt")
    with open(file_path, "r") as file:
        for line in file:
            urls.append(line.strip())
    if args.list:
        for url in urls:
            print(url, end = " ")
    else:
        for url in urls:
            webbrowser.open(url)
    

def save_input_url(args):
    url_path = args.operands
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "url_storage.txt")

    if not valid_url_paths(url_path):
        raise argparse.ArgumentTypeError(
            'invalid url'
        )

    with open(file_path, 'r') as file:
        data = [line.strip() for line in file.readlines()]
    if url_path not in data:
        with open(file_path,"a") as file:
            file.write(url_path + "\n")
            print(f"{url_path} is saved")
    else:
        print(f"{url_path} has exits")

def valid_url_paths(url):
    parse_url = urlparse(url)

    if parse_url.netloc:
        return True

    return False

def remove_url_input(args):
    url_path = args.operands
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "url_storage.txt")
    with open(file_path, "r") as file:
        data = file.readlines()
    
    with open(file_path, "w") as file:
        for line in data:
            if line.strip("\n") != url_path:
                file.writelines(line)
    print(f"{url_path} is removed")

