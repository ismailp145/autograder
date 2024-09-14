
import os
import sys
def rename(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            old_file_path = os.path.join(directory, filename)
            new_file_name = filename[:-3].split(" - ")[-1] + '.py'
            new_file_path = os.path.join(directory, new_file_name)
            os.rename(old_file_path, new_file_path)
            
# submissions_dir = '/Users/ismail/Desktop/GRADING/Fall-2024/CSC-243/Assignments/A1'
# rename(submissions_dir)

if __name__== "__main__":
    # submissions_dir = '/Users/ismail/Desktop/GRADING/Fall-2024/CSC-243/Assignments/A1'
    # rename(submissions_dir)
    rename(submissions_dir)
