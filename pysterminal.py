import importlib
import os
import sys
import argparse
from rich import console

import pyster.endreport as endreport

def parse_options(args_):
    parser = argparse.ArgumentParser(prog='pyster', description='Test your code!')
    parser.add_argument('-p', '-path', metavar='dir', dest='path', default='testing', help='path to the testing directory. Default is testing or test directory')
    parser.add_argument('--endreport', action='store_true', default=False, help='if turned on endreport will be printed')
    parser.add_argument('--no-priority', action='store_true', default=True, help='if turned on the priority order won\'t be used (smoke tests first, etc.)')
    parser.add_argument('--no-error', action='store_true', default=False, help='if turned on the program won\'t raise errors, just print the fails. This should be turned off when using github actions')
    parser.add_argument('--one-error', action='store_true', default=False, help='if turned on the program will only raise one error after all tests were tested')

    return parser.parse_args(args_)

def import_files(file_):
    file_ = file_.replace('//', '.').replace('/', '.').replace('\\', '.').replace('.py', '')

    x = importlib.import_module(file_)

def test_files(options, path):
    smoke_test_done = False
    for file_ in scan_dir(path):
        print(f'<{file_}>')
        if options.no_priority:
            import_files(file_=file_)
        else:
            # Do priority...
            import_files(file_=file_)

def scan_dir(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                if entry.name.endswith(".py"):
                    yield entry.path
                else:
                    pass # For now
            else:
                #symlink or dir
                if entry.is_dir():
                    return scan_dir((path+'/'+entry.name).replace('//', '/'))
                else:
                    #! Symlink
                    pass

def path_parsers(path):
    ''' Go thru testing folder '''
    if not os.path.exists(path):
        path = 'testing'
        if not os.path.exists(path):
            path = 'test'
            if not os.path.exists(path):
                path = None
                raise FileNotFoundError('The testing directory does not exits. Please create a testing/test directory!') # Actually not FileNotFoundError but DirectoryNotFoundError (well, on Windows that would make sense)
    
    if path is not None:
        return path

def main(args_):
    options = parse_options(args_=args_)
    if options.endreport:
        endreport.Endreport.use = True
    path = path_parsers(options.path)
    test_files(options, path)
    endreport.Endreport.print_data()

if __name__ == '__main__':
    main(sys.argv[1:])