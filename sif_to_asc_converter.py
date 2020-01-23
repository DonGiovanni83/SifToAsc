import os
import sys

"""
    Usage: 
        #$ python3 sif_to_asc_converter.py source/directory output/directory
 
    Will convert all .sif files in /source/directory and output .asc files to output/directory
"""


def main():
    if len(sys.argv) != 3:
        print("To few arguments")
        exit(1)

    source_path = str(sys.argv[1])
    output_folder = str(sys.argv[2])

    print("Scanning " + source_path + " for .sif files: ")
    sif_url_list = get_sif_recursively(source_path)

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    print("Converting files and putting them into " + source_path)
    for i in range(len(sif_url_list)):
        convert_sif_to_asc(output_folder, sif_url_list[i])


def get_sif_recursively(source_path: str):
    """
    Search source_path recursively for .sif files. Return a list of search results
    """
    file_list = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(".sif"):
                print("Found" + os.path.join(root, file))
                file_list.append(os.path.join(root, file))

    return file_list


def convert_sif_to_asc(output_path: str, source_file: str):
    print("Converting " + source_file)
    # TODO put here your code for conversion


if __name__ == "__main__":
    main()
