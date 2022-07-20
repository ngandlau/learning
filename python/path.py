from pathlib import Path

path = Path('/')

if __name__ == '__main__':
    # iterate through all files and directories in path
    [print(fd) for fd in path.iterdir()]

    # print absolute version of that path
    print(path.absolute()) 

    # print current working directory
    print(Path.cwd())

# $ python path.py
# /home
# /srv
# /etc
# /opt
# /root
# /lib
# /mnt
# /usr
# /media
# /lib64
# /sys
# /dev
# /sbin
# /boot
# /bin
# /run
# /lib32
# /libx32
# /init
# /proc
# /snap
# /tmp
# /var
# /lost+found
# /
# /home/username/projects/learning





