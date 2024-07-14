# VMD imposter generation script by Kleis.

import os
import xml.etree.ElementTree as ET

# Search the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Fetch the local directories
input_dir = os.path.join(script_dir, 'input')
output_dir = os.path.join(script_dir, 'output')

# Create the output directory if it does not exist for new users

if not os.path.exists(input_dir):
    os.makedirs(input_dir)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    

# Function to add imposter_model suffix to every VARIANT_MESH element
def add_imposter_to_vmd(file_path, output_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for variant_mesh in root.findall(".//VARIANT_MESH"):
        model_path = variant_mesh.get('model')
        if model_path and model_path.endswith('.rigid_model_v2'):
            variant_mesh.set('imposter_model', model_path)
    
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

# Save each .variantmeshdefinition file
for filename in os.listdir(input_dir):
    if filename.endswith('.variantmeshdefinition'):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)
        add_imposter_to_vmd(input_file_path, output_file_path)

print("Imposters added to all .vmd files! Check your output folder.")