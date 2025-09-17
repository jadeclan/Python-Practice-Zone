def main():
    # This algorithm was tested with no extension and just a period -> Both worked.
    filename = 'this_file.txt'
    removed_extension = filename.rsplit('.',1)
    extensionless_filename = removed_extension[0]
    new_name = extensionless_filename + '.json'

    print(f"Old file name was: {filename}. The new file is now {new_name}.")

main()