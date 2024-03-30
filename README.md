# COMP4203_Project

This README will outline changes as they are made (to be added/specified as they are made):

March 13, 2024:
* Changes by Nikhail  
    * Used bleak to implement a CLI BLE Scanner - Works in windows
        * Requires some pip3 installs to work
            * pip3 install asyncio
                * Depending on the version of Python you have this may already be supported by default
            * pip3 install bleak

March 15, 2024:
* Changes by Nikhail  
    * Implemented Bluetooth classic Scanner - Works in *NIX, specifically UBUNTU
        * Require some pip3 installs and apt-get installs to work
            * pip3 install PyBluez
            * sudo apt-get install libbluetooth-dev

March 26, 2024:
* Changes by Nikhail  
    * Changed the bleak implementation slightly
        * Check the dir Upgraded_Code and launch from controller.py

March 30, 2024:
* Changes by Nikhail  
    * Adjusted ./Upgraded_Code/controller.py to allow an option to just output stats if there's already scanned devices. Also added an option to output the filtered data
