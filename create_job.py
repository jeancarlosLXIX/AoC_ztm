import sys # get arguments from the command line
import os # make dir and get current location for the creation of the dir/file

# You will put the name/direction of the folder after that (hit space) the name of the file
# if there is no name it will create one called main.py
# don't put ".py" at the end, it will add it automatically

def create_dir(dirName: str, file_name=None):
    file_location = os.getcwd() + f"/{dirName}" # full path for the file
    
    try:

        os.makedirs(dirName, exist_ok=True) # create dir

        print("Directory " , dirName ,  " Created ")

        os.chdir(file_location)
        
        # creating txt file
        file = open("input.txt", "a")
        file.close()
        
        if file_name != None:
            create_file(file_name)
        else:
            create_file("main")
        
    except FileExistsError:
        print("Directory " , dirName ,  " already exists") 


def create_file(name: str):
    with open(name + ".py", "a") as f:
        f.write('with open("input.txt", "r") as f:\n')
        f.write('\tdata = [line.strip() for line in f.readlines()]')


flags = sys.argv[-1]
location = sys.argv[1]

if len(sys.argv) ==3:
    file_name = sys.argv[2]
else:
    file_name = None

create_dir(location,file_name)