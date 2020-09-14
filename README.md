## Setup

1. Install raspberry on SD card... (don't forget to place a file called `ssh` on boot disk!)
2. Connect raspberry to ethernet and start up
3. Connect to raspberry with ssh `ssh pi@raspberrypi.local`
4. `sudo apt-get update`

### Enable auto login (maybe already active!!)

1. `sudo nano /etc/systemd/system/getty@tty1.service.d/autologin.conf`

        [Service]
        ExecStart=
        ExecStart=-/sbin/agetty --autologin pi --noclear %I 38400 linux

2. `sudo systemctl enable getty@tty1.service`
3. `sudo reboot`

### Mount usb stick

1. Create mount point with `sudo mkdir /media/usb && sudo chown -R pi:pi /media/usb`
2. Get usb stick uuid with `sudo blkid`
2. Add `UUID=7E56-120C /media/usb vfat auto,users,rw,uid=1000,gid=100,umask=0002 0 0` to `/etc/fstab`

### Install script

2. `sudo apt-get install git`
3. `git clone https://github.com/sspross/raspberry-print.git`

### Install printer

See https://wiki.debian.org/SystemPrinting

1. `sudo aptitude install cups cups-client elinks`
2. `sudo service cups start`
3. `sudo usermod -a -G lpadmin pi`
4. `sudo elinks http://localhost:631/` (or open tunnel to use a real browser `ssh pi@raspberrypi.local -T -L 3631:localhost:631`)
5. Administration -> Add Printer -> Config Printer -> Set default for server
6. check default printer setting `lpstat -d`

### Auto start script

1. add start script command to `.profile` file `python /home/pi/raspberry-print/app.py`

### Activate numlock by default

1. `sudo apt-get install numlockx`
2. 



