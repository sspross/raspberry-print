## Setup

1. Downloaded RASPBIAN JESSIE LITE image from http://raspberrypi.org/downloads
2. Install it on SD card, see http://raspberrypi.org/documentation/installation/installing-images/mac.md
3. Connect raspberry to ethernet and start up
4. Find IP `nmap -sn 192.168.1.1/24` 
5. Connect to raspberry with ssh
6. `sudo apt-get update`

### Enable auto login

1. `sudo nano /etc/systemd/system/getty@tty1.service.d/autologin.conf`

        [Service]
        ExecStart=
        ExecStart=-/sbin/agetty --autologin pi --noclear %I 38400 linux

2. `sudo systemctl enable getty@tty1.service`
3. `sudo reboot`

### Mount usb stick

See http://raspberrypi-spy.co.uk/2014/05/how-to-mount-a-usb-flash-disk-on-the-raspberry-pi/

1. create mount point

        sudo mkdir /media/usb
        sudo chown -R pi:pi /media/usb

2. add mount to `.profile` file `sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi`

### Install script

2. `sudo apt-get install git`
3. `git clone https://github.com/sspross/raspberry-print.git`

### Install printer

See https://wiki.debian.org/SystemPrinting

1. `sudo aptitude update`
2. `sudo aptitude install cups cups-client elinks`
3. `sudo service cups start`
4. `sudo usermod -a -G lpadmin pi`
4. `sudo elinks http://localhost:631/`
5. Administration -> Add Printer -> Config Printer -> Set default for server
6. check default printer setting `lpstat -d`

### Auto start script

1. add start script command to `.profile` file `python /home/pi/raspberry-print/app.py`

### Get hama keypad working

1. `sudo apt-get install python-dev python-pip`

https://www.hama.com/00053224/hama-keypad



