import tools
import latex

import re


def test_header(string):
    # определить что это заголовок
    headers = {
        1: "\section*{",
        2: "\subsection*{",
        3: "\subsubsection*{"
    }

    string = " " + string
    test = re.match(r'^\s+#+', string)

    if test != None and last_list != False:
        # решить какой это заголовок
        type_of_header = [x for x in test.group(0)].count('#')

        # отделить заголовок от текста заголовка
        # и добавить к тексту параметры latex
        lx = headers[type_of_header] + re.sub(r'^\s+#+', '', string) + '}'

        return lx
    else: return False

def test_list(string, last_list):
    new_list = "\\begin{enumerate} \item "
    nested_list = "\\begin{enumerate} [label*=\\arabic*.] \n \item "
    end_neted_list = "\end{enumerate} \n \item "
    end_list = "\end{enumerate} \n "
    item = "\item "

    string = " " + string
    test = re.match(r'^\s+-', string)

    # Если предыдущая строка не была списком
    if last_list == False and test != None:
        # Обявить новый список
        lx = new_list + re.sub(r'^\s+#+', '', string) + '\n'
        return [lx, test]

    # Если предыдущая строка была списком
    if last_list != False and test != None:
        # print(len(last_list.group(0)) ,'\t', len(test.group(0)))
        # Проверить изменился ли отступ
        ## Если отступ не изменился
        if len(last_list.group(0)) == len(test.group(0)):
            ### Это item
            lx = item + re.sub(r'^\s+#+', '', string) + '\n'
            return [lx, test]

        ## Если отступ стал больше
        if len(last_list.group(0)) < len(test.group(0)):
            ### начать вложенный список
            lx = nested_list + re.sub(r'^\s+#+', '', string) + '\n'
            return [lx, test]

        ## Если отступ стал меньше
        if len(last_list.group(0)) > len(test.group(0)):
            ### закрыть вложенный
            diferent = len(last_list.group(0)) - len(test.group(0)) -1
            lx = (end_list*diferent) + end_neted_list + re.sub(r'^\s+#+', '', string) + '\n'
            # print('dif  =', diferent, '\t', lx)
            return [lx, test]

        return ['', test]

    if test == None and last_list != False:
        diferent = len(last_list.group(0)) -1
        lx = end_list*diferent + '\n'
        return [lx, False]

    if last_list != False and test != None: return ['', test]
    return [False, False]

def test_table(string, col, count):
    title = "\\begin{tabular}{|"

    string = " " + string
    test = re.match(r'^.+\|', string)

    lx = False;
    if test:
        if col == 0:
            count = [x for x in test.group(0)].count('|') + 1
            lx = title + 'c|'*count + '} \n \hline \n'
        if col > 1:
            lx = re.sub(r'\|', '&', string) + ' \\\\\\hline \n'
            if col == count: lx = lx + "\end{tabular}"
        col+=1

    return [lx, col, count]

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
    last_list = False; col = 0; count = 0
    for string in text:
        tmp = string
        head = test_header(tmp)

        tmp_list = test_list(tmp, last_list)
        list = tmp_list[0]; last_list = tmp_list[1]

        tmp_table = test_table(string, col, count)
        table = tmp_table[0]; col = tmp_table[1]; count = tmp_table[2]
        if col == count: col = 0

        if list != False:
            print(list, end='')
        if  head != 0:
            print(f"{head}", end='')
        if table != False:
            print(table, end='')
