from src import cli

def main():
    args = cli.parser_arguments()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        print("No valid subcommand provided. Use --help for usage details.")


    print("hello world")

if __name__ == "__main__":
    main()
