from subprocess import call


def main():
    directory = '/media/usb'
    while True:
        name = raw_input('Type a file name: ')
        command = ['lp', '-o', 'sides=two-sided-long-edge']

        # check if multiple copies are requested
        if '*' in name:
            copies, name = name.split('*')
            command.append('-n')
            command.append(copies)

        command.append("{}/{}.pdf".format(directory, name))
        try:
            print ' '.join(command)
            call(command)
        except Exception, e:
            print e


if __name__ == "__main__":
    main()
