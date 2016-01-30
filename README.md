## Setup

1. Downloaded RASPBIAN JESSIE LITE image from raspberrypi.org/downloads
2. Install it on SD card raspberrypi.org/documentation/installation/installing-images/mac.md
3. Connect raspberry to ethernet and start up
4. Find IP `nmap -sn 192.168.1.1/24` 
5. Connect to raspberry with ssh

### Enable auto login

1. `sudo nano /etc/systemd/system/getty@tty1.service.d/autologin.conf`

    [Service]
    ExecStart=
    ExecStart=-/sbin/agetty --autologin pi --noclear %I 38400 linux

2. `sudo systemctl enable getty@tty1.service`
3. `sudo reboot`

### Install script

1. `git clone git@github.com:sspross/raspberry-print.git`
