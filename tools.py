from sys import argv

def get_path():
    path = ""
    try:
        file, path = argv
    except:
        if path == "":
            path = input("Type path:\t")

    return path

def get_text(path):
    file = open(path, 'r', encoding="utf8")
    text = file.readlines()
    file.close()

    return preProcessor(text)

def preProcessor(text):
    """
    Function for delite trash
    :param text: [string,string...,string]
    :return:
    """

    text = list(filter(lambda a: a != "", text))
    text = list(filter(lambda a: a != "\n", text))

    return text