import argparse
import os
import re
import webbrowser
from urllib.parse import urlparse

def parser_arguments():
    parser = argparse.ArgumentParser(
        prog = "miso",
        description = "Miso is a command-line tool designed to help you manage and automate your daily tasks with ease. Whether it's managing URLs, executing repetitive commands, or streamlining workflows, Miso provides a simple and intuitive interface for enhancing productivity.",
        epilog = "%(prog)s is still in beta. Thanks for using %(prog)s! :)"
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
    try:
        with open(file_path, "r") as file:
            for line in file:
                urls.append(line.strip())
    except FileNotFoundError:
        urls = []

    if urls:
        if args.list:
            for url in urls:
                print(url)
        else:
            for url in urls:
                webbrowser.open(url)
    else:
        print("No url paths exist")

def valid_url_paths(url):
    if not urlparse(url).scheme:
        url = 'https://' + url

    parsed_url = urlparse(url)
    
    domain = parsed_url.netloc

    domain_regex = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'

    if re.match(domain_regex, domain):
        return True
    return False

def save_input_url(args):
    url_path = args.operands
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "url_storage.txt")

    if not valid_url_paths(url_path):
        print(f"Invaild URL path: {url_path}")
        return
    
    try:
        with open(file_path, 'r') as file:
            data = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        data = []

    if url_path not in data:
        with open(file_path,"a") as file:
            file.write(url_path + "\n")
            print(f"{url_path} is saved")
    else:
        print(f"{url_path} has exits")

def remove_url_input(args):
    url_path = args.operands
    file_exist = False
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "url_storage.txt")
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        data = []
    if data:
        with open(file_path, "w") as file:
            for line in data:
                if line.strip("\n") == url_path:
                    file_exist = True
                else:
                    file.writelines(line)
        if file_exist:
            print(f"{url_path} is removed")
            return
        else:
            print(f"{url_path} not found")
            return
    print("Empty url paths list")
