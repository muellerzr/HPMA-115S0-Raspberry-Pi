# HPMA-115S0-Raspberry-Pi
This is a repository for using HPMA-115S0 sensors on a Raspberry Pi


## Instructions:

1. `git clone` this respository

2. Run setup.py for Adafruit_Python_BME280

3. Run setup.py for Adafruit_Python_GPIO

4. Touch __init__.py for HPMA115S0_Python

5. `chmod +x run.sh`

6. Run `screen` 

7. `sudo ./run.sh`

8. Detach with `CTRL + A + D safely exit SSH

# To find IP:

On terminal:
ip -4 addr show | grep global

Look for 172

In ZenMap: nmap -sn 172 ip except end eg: 172.20.10.0/24
Ssh pi@172..... until it goes in
