from src import cli

def main():
    args = cli.parser_arguments()
    if hasattr(args, 'func'):
        args.func(args)
        
    print("hello world")

if __name__ == "__main__":
    main()
