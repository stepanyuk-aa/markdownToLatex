import tools
import latex

import re


def test_header(text):
    h1 = re.match(r'(^\s+#)', string)
    h11 = re.match(r'(^#)', string)
    h2 = re.match(r'(^\s+##)', string)
    h22 = re.match(r'(^##)', string)
    h3 = re.match(r'^(\s+###)', string)
    h33 = re.match(r'^(###)', string)

    print(h1, h2, h3)
    if h1 or h11: return 1
    if h2 or h22: return 2
    if h3 or h33: return 3

    return 0

if __name__ == '__main__':
    page = """
    \\newpage
    \section*{Часть 1. Настройка устройств}
    \subsection*{Шаг 1. Настройка базовых параметров устройств.}
    """
    doc = latex.Latex_Document()
    doc.pages.append(page)
    doc.title = "Test"
    # doc.processor()

    path = "test.md" # get_path()
    text = tools.get_text(path)



    print(f"You' file: {path}. Show it:")
    for string in text:
        tmp = string
        head = test_header(tmp)

        if  head != 0:
            print(f"{string}", end='')
