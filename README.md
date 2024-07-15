## How it works (please read!)

So what is this in particular? 

The premise is that all **.variantmeshdefinition** files are **XML** files, so the script will basically parse the entire file in search of any **VARIANT_MESH** elements like so

    def add_imposter_to_vmd(file_path, output_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for variant_mesh in root.findall(".//VARIANT_MESH"):
        model_path = variant_mesh.get('model')
	
We get the model attribute that is inside any <VARIANT_MESH model=""/> line and store it in model_path.
 
        if model_path and model_path.endswith('.rigid_model_v2'):
            variant_mesh.set('imposter_model', model_path)

If the path ends with a .rmv2 type file then we will add it as a new imposter. The script will parse all lines (set by the for loop above) until it ends.     
    
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

Then tree.write will save the modified XML to an specified output_path previously declared.

For this to work we must import the necessary modules: 

    import os
    import xml.etree.ElementTree as ET # XML module

**The tool automatically creates the input and output folders, simply run the script. It will also fetch your local directory.** You can run as many files as you want at once, as long as they're in the input folder. 

Please consider I'm not as well versed in Python, so some GPT assistance was needed, but I'm learning. 

### If you wish to make any modifications and upload them on your own, please credit this page here, it's all I ask.

## Some considerations: 

   1. It will add the imposter suffix to every **VARIANT_MESH** model line. If you don't want imposters to appear in any certain part of a VMD, either edit the code or contact me and we can figure it out.
   2. It might not flawless. Please, check the output everytime you run this tool.
   3. The script **REQUIRES the python dependencies**. Please download it here: https://www.python.org/downloads/ (Important, when installing Python, select "Add Python to PATH". Check custom installation if you want to do anything specific, if not, click install now.)
   4. The script is launched via a .bat file. I will make a shinier interface in the future.
   5. This was designed for **Attila: TW** but I struggle to see it not working for other games. Any errors or incompatibilities please contact me.

If you are skeptical about the .bat file or... whatever... here's the code:

 	 @echo off
 	 echo Welcome to the .vmd imposter generation script by Kleis.
 	 echo.
 	 set current_dir=%cd%
 	 echo Your current .py script directory is:
 	 echo.
 	 echo %current_dir%  
 	 echo.

	  echo If it isn't correct, please set the directory in your .bat file (open the bat file with any editor of your liking). &REM If you want to change the directory, go to the sixth line. Where it says current_dir=%cd%, replace %cd% with the directory where the script sits.

 	 echo. 
  
 	 echo Press any key to generate VMD files.
	
 	 echo.

 	 pause >nul

    		vmd_script.py 
	
    		echo.

 	 echo Press any key to exit the program.
 	 pause >nul
 	 exit

That's all!


