READ!

This is a tool that I made in my spare time. I'm not as well versed in python so some GPT assistance was needed. If you wish to make any modifications and upload them on your own, please credit this page here, it's all I ask.

*** This REQUIRES a local folder to work. Go to releases and download the .rar file there. If not, simply download the .bat and .py into a folder and, inside that folder, create an 'input' and 'output' folder (without the '').

The premise is that all .variantmeshdefinition files are XML files, so the script will basically parse the entire file in search of any VARIANT_MESH elements like so:

  def add_imposter_to_vmd(file_path, output_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for variant_mesh in root.findall(".//VARIANT_MESH"):
        model_path = variant_mesh.get('model')
        if model_path and model_path.endswith('.rigid_model_v2'):
            variant_mesh.set('imposter_model', model_path)
    
    tree.write(output_path, encoding='utf-8', xml_declaration=True)


Then it is all saved neatly.

Some considerations: 

   1. It will add the imposter suffix to every VARIANT_MESH model line. If you don't want imposters to appear in any certain part of a VMD, either edit the code or contact me and we can figure it out.
   2. It is not flawless. Please, check the output everytime you run this tool as sometimes it may not work. Don't ask me why.
   3. The script REQUIRES the python dependencies. Please download them here: https://www.python.org/downloads/
   4. The script is launched via a .bat file. I will make a shinier interface in the future.

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


