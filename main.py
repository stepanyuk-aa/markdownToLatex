import tools

if __name__ == '__main__':
    path = "test.md" # get_path()
    text = tools.get_text(path)

    print(f"You' file: {path}. Show it:")
    for string in text:
        print(f"{string}", end='')
