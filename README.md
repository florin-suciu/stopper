# stopper
A simple webserver for shutting down the system it's running on.

## Setup instructions

### Notes:
* get this code with: **git clone https://github.com/gplayersv/stopper.git**
* on unix systems flask must be installed in the root's python (e.g., **sudo which python**)
* make sure port 9843 is opened

### Requirements
* python 2.7
* flask
* root permission required for shutdown command on unix

### Linux
1. **sudo vi /etc/rc.local**
    * add line with: **python [full_path_to_project_root]/stopper.py &**
    * save file and exit
2. restart system
3. open http://[machine_ip or machine_hostname]:9843/ in browser from pc/mobile

### Windows
1. update **stopper.bat** paths with the ones from your system
2. copy **stopper.bat** to your startup folder (e.g. on windows 7 "c:\Users\YOUR_USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\") 