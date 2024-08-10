from src import cli, storage
import webbrowser

def main():
    args = cli.parser_arguments()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        urls = storage.read_files_url()
        for url in urls:
            webbrowser.open(url)
        
    print("hello world")

if __name__ == "__main__":
    main()
