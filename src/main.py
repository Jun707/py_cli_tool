import webbrowser
from src.storage import read_files_url
def main():
    urls = read_files_url()
    for i in range(len(urls)):
        webbrowser.open(urls[i])
    print("hello world")

if __name__ == "__main__":
    main()
