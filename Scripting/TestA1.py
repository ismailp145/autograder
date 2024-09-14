import os
import sys
import importlib

# q = importlib.import_module("192318-945350 - Sidra Quadri - Sep 11, 2024 1204 AM - Quadri_Sidra_assignment1")
# q.calculate_boost_distance(40, 9)



def main():

    submissions_dir = '/Users/ismail/Desktop/GRADING/Fall-2024/CSC-243/Assignments/A1'
    sys.path.insert(0, submissions_dir)
    count = 0
    for filename in os.listdir(submissions_dir):

        # here filename is a string so unfortunately we can't just use "import filename"
        # this is why we need the 'importlib' from above
        


        if filename.endswith('.py'):
        
            try:
                current_student = importlib.import_module(filename[:-3]) 
                print(filename)
                count +=1 
              
                # if hasattr(current_student, 'calculate_boost_distance'):
                #     output1 = current_student.calculate_boost_distance(40, 9)
                #     print(output1)
                #     # print("entered")
            except Exception as e:
                print(f"Error importing or running {filename}: {e}")
    print(count)
        
        # current_student = importlib.import_module(filename_without_extension) #import the module with the alias current_student
        # # #now you can use current_student as an alias for the module and call functions from it directly
        # output1 = current_student.calculate_boost_distance(40, 9)
        # if output1 == 360:
        #     print('entered')
        # #update a dictionary or list or whatever you want to keep track of the outputs with
        #     count += 1 
        # output2 = current_student.function2(any, args, needed)
        # if output2 == expected2:
        # #     count += 1

if __name__ == "__main__":
    main()