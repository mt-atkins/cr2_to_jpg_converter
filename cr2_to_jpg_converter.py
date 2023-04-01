import os
import sys
import imageio
import rawpy
import glob

def convert_cr2_to_jpg(input_file, output_file):
    with rawpy.imread(input_file) as raw:
        image = raw.postprocess()
    imageio.imwrite(output_file, image)

def convert_all_cr2_in_directory(input_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    cr2_files = glob.glob(os.path.join(input_directory, '*.CR2'))
    for cr2_file in cr2_files:
        file_name = os.path.splitext(os.path.basename(cr2_file))[0]
        output_file = os.path.join(output_directory, f"{file_name}.jpg")
        convert_cr2_to_jpg(cr2_file, output_file)
        print(f"Successfully converted '{cr2_file}' to '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python cr2_to_jpg_converter.py [input_directory] [output_directory]")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.isdir(input_directory):
        print(f"Error: Input directory '{input_directory}' does not exist.")
        sys.exit(1)

    try:
        convert_all_cr2_in_directory(input_directory, output_directory)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
