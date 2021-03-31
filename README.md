# 3D_Name_Tag_Generator
A simple script to easily generate name tags for 3d printing.
OpenSCAD file from thingiverse: https://www.thingiverse.com/thing:739573

To run the script:
python3 name_generation_script.py {csvfile} {directory}

csvfile should contain the text to be generated seperated by , 
ie: John, Chris, Mary

The generated stls will be placed in the directory specified.
If the directory does not exist, a new directory will be created
with the provided name and stls placed there.

To tweak the parameters such as font, thickness etc, open
Keychain_Name_Generator.scad with OpenSCAD, make the changes,
and save the file. Subsequent generations will use this new 
settings.

OpenSCAD Command Line Page for Reference:
https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_OpenSCAD_in_a_command_line_environment