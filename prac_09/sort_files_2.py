import os


def main():
    """Move the files."""
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            # Now we can map this new extension to a folder name
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


if __name__ == '__main__':
    main()
