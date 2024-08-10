import os

def save_url(url_path):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "url_storage.txt")
    with open(file_path,"a") as file:
        file.write(url_path + "\n")


def read_files_url():
    urls = []

    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "url_storage.txt")
    
    with open(file_path, "r") as file:
        for line in file:
            urls.append(line.strip())

    print(urls)
    return urls

