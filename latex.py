class Latex_Document(object):
    def __init__(self):
        self.title = ""
        self.author = ""

        self.pages = []

        self.library = """
\\documentclass[a4paper,12pt]{article}
\\usepackage{cmap}					% поиск в PDF
\\usepackage[T2A]{fontenc}			% кодировка
\\usepackage[utf8]{inputenc}			% кодировка исходного текста
\\usepackage[english,russian]{babel}	% локализация и переносы
\\usepackage{fancybox, fancyhdr} 
\\usepackage{lastpage}

\\usepackage{graphicx}
\\usepackage{xcolor}
\\usepackage{lipsum}

\\usepackage{makecell}
    \\renewcommand\\theadalign{bc}
    \\renewcommand\\theadfont{\\bfseries}
    \\renewcommand\\theadgape{\\Gape[4pt]}
    \\renewcommand\\cellgape{\\Gape[4pt]}

\\usepackage{enumitem}

\\setlength\\headheight{26pt}
\\setlength{\\parindent}{5ex}
% \\setlength{\\parskip}{1em}

\\usepackage{datetime}
\\newdateformat{bkdate}{\\twodigit{\\THEDAY}\\ \\shortmonthname\\ \\THEYEAR}

\\renewcommand{\headrulewidth}{1pt}
\\renewcommand{\\footrulewidth}{5pt}

% Изменить нумерацию второго уровня на цифры
\\renewcommand{\labelenumii}{\\arabic{enumii}}
\\renewcommand{\labelenumiii}{\\arabic{enumii}}

\begin{document}
        """

    def colontitul_base(self):
        return "\pagestyle{fancy} \n \\fancyhf{}"

    def colontitul_head(self):
        return "\\fancyhead[L]{ " + self.title + " }" + "\\fancyhead[R]{ \\bkdate\\today }"

    def colontitul_footer(self):
        return "\\fancyfoot[L]{ \\bkdate\\today \\newline " + self.author + "}" + "\\fancyfoot[R]{\\thepage \ из \pageref{LastPage}}"

    def get_colontitul(self):
        return self.colontitul_base() + self.colontitul_head() + self.colontitul_footer()

    def processor(self):
        text = self.library + self.get_colontitul()

        for page in self.pages:
            text += page

        text += "\end{document} % Конец текста."

        print(text)


        # return text

    def parser(self, text):
        pass

# for debugging
if __name__ == '__main__':
    page = """
\\newpage
\section*{Часть 1. Настройка устройств}
\subsection*{Шаг 1. Настройка базовых параметров устройств.}
"""
    doc = Latex_Document()
    doc.pages.append(page)
    doc.title = "Test"
    doc.processor()