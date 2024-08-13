from src import cli

def main():
    args = cli.parser_arguments()
    if hasattr(args, 'func'):
        args.func(args)

if __name__ == "__main__":
    main()
