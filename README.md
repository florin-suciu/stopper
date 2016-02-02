# stopper
A simple webserver for shutting down the system it's running on.

## Setup
* root permission required for shutdown command

### Linux
1. **git clone https://github.com/gplayersv/stopper.git**
1. **sudo pip install flask** (must be installed in root's python)
2. **sudo vi /etc/rc.local**
    * add line with: **python [full_path_to_project_root]/stopper.py &**
    * save file and exit
3. restart system
4. open http://[machine_ip or machine_hostname]:9843/ in browser from pc/mobile

### Windows
1. 