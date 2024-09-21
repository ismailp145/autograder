import os
import sys
import importlib
import unittest


submissions_dir = 'filepathto/Assignments/A1'
sys.path.insert(0, submissions_dir)
current_student = importlib.import_module('current_student')

if hasattr(current_student, 'calculate_boost_distance'):
    output1 = current_student.calculate_boost_distance(40, 9)

csv_file = open('results.csv', 'w')
csv_file.write('Filename,calculate_boost_distance\n')
csv_file.write(f'{current_student.__name__},{output1}\n')
csv_file.close()

unittest.main(argv=[''], exit=False)
