import os
script = """
cd /home/mermi/FoxOS/sparkVersion/
sudo fastboot devices
cd v18D_nightly_v2/
sudo ./flash.sh
cd /home/mermi/FoxOS/sparkVersion/
sudo ./shallow_flash.sh -G/home/mermi/FoxOS/sparkVersion/gaia.zip -g/home/mermi/FoxOS/sparkVersion/b2g-42.0a1.en-US.android-arm.tar.gz
"""
os.system("bash -c '%s'" % script)
