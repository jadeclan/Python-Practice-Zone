def main():
    # This algorithm was tested with no extension and just a period -> Both worked.
    filename = 'this_file.txt'

    removed_extension = filename.rsplit('.',1)
    extensionless_filename = removed_extension[0]
    new_name = extensionless_filename + '.json'

    test = filename.rsplit('.',1)[0] + '.json' # <- This line does the same as the previous 3 lines
    print(f"Old file name was: {filename}. The new file is now {new_name}.")
    print(f"Old file name was: {filename}. The new file is now {test}.")

main()