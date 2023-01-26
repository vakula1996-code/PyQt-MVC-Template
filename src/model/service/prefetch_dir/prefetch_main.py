import os
import sys
import sqlite3
from .utils import Prefetch

def prefetch_main():
    file = 'C:\Windows\Prefetch'
    file_paths = []
    data = []
    if os.path.isdir(file):
        for filename in os.listdir(file):
            file_paths.append(os.path.join(file, filename))
    else:
        file_paths.append(file)
    parsed_files = []
    for filepath in file_paths:
        if filepath.endswith(".pf"):
            if os.path.getsize(filepath) > 0:
                p = Prefetch(filepath)
                parsed_files.append(p)
    for p in parsed_files:
        for i in p.prettyPrint()['last_executed']:
            data.append({
                'name_file': str(p.prettyPrint()['name_file']),
                'last_executed': str(i),
                'directory_strings': str(p.prettyPrint()['directory_strings']),
                'resources_loaded': str(p.prettyPrint()['resources_loaded'])
            })
    return data

