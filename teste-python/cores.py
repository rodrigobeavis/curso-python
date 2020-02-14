
def get(cor):
        cores = {
                'l': '\033[m',
                'az': '\033[34m',
                'Naz': '\033[1;34m',
                'am': '\033[33m',
                'Nam': '\033[1;33m',
                'ver': '\033[31m',
                'Nver': '\033[1;33m',
                'pb': '\033[7;30m',
        }
        return cores[cor]
