import subprocess
import sys
import os

def main():
    # Retrieve file, process it
    if len(sys.argv) != 3 :
        print("Error: please input textfile and folder")
        return 
        
    filename = sys.argv[1]
    folder = sys.argv[2]
    if not os.path.exists(folder):
        os.makedirs(folder)

    print("Generating names from file", filename)
    file = open(filename, "r")
    text = file.read()
    name_list = text.split(", ")

    # Generate stls with openscad
    print('executing openscad script')
    for name in name_list:
        # Fix output stl name
        file_name = name.replace(" ", "_")
        file_name = file_name.rstrip()
        print("Generating stl for", name)

        # Command to pass into bash
        command = "openscad -o " + folder + "/" + file_name + ".stl Keychain_Name_Generator.scad -D 'name=\"" + name + "\"'"
        print(command)
        subprocess.run(command, shell=True)
        
    print('\n\n\n\n\nALL DONE!!! Generated', len(name_list), 'STLs')


if __name__ == '__main__':
    main()