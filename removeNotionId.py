import os


def renamer(walker, layer = 0):
    for (dirpath, dirnames, filenames) in walker:
        for f in filenames:
            if f.count(' ') > 0:
                s = ''
                for i in f.split(' ')[:-1]:
                    s = s + i
                os.rename(f'{dirpath}\\{f}', f'{dirpath}\\{s}.md')



renamer(os.walk('DesignPatterns'))

