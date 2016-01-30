from os.path import expanduser
from subprocess import call


def main():
    directory = expanduser("~/files")
    while True:
        name = raw_input('Type a file name: ')
        try:
            call(["lp", "{}/{}.pdf".format(directory, name)])
        except Exception, e:
            print e


if __name__ == "__main__":
    main()
