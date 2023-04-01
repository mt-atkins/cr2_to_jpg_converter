import os
import sys
import imageio
import rawpy

# def convert_cr2_to_jpg(input_file, output_file):
#     with open(input_file, 'rb') as file:
#         raw_data = file.read()
#     with rawpy.imread(raw_data) as raw:
#         image = raw.postprocess()
#     imageio.imwrite(output_file, image)

def convert_cr2_to_jpg(input_file, output_file):
    with rawpy.imread(input_file) as raw:
        image = raw.postprocess()
    imageio.imwrite(output_file, image)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python cr2_to_jpg_converter.py [input_file.cr2] [output_file.jpg]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)

    try:
        convert_cr2_to_jpg(input_file, output_file)
        print(f"Successfully converted '{input_file}' to '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
