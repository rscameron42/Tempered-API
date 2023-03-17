# **Script to automate the Provisioning process**

## File: aw-provision.py
*File meant to run against the conductor to automate the process of provisioning new Airwalls*
### Syntaxt
``usage: aw-provision [cloud|dev|prod] [serial-number]``
### How it Works 
- Populate Conductor Location and Credential variables
  - Looks for URL/IP & API credentials in local file
  - If file is not found, promps for URL/IP & API credentials
- Look for serial numbers to provision *If possible*
- Grant Provisioning Request
- Configure Airwall as **Managed**
- Ugrade Airwall firmware
- Configure Airwall group membership(s)
- Configure Ports
  - Configure underlay port group
    - Remane port group to *ug1*
    - Disable spanning tree
  - Configure overlay port groups *repeat for each overlay port*
    - Remane port group to *ogX* where X is the port number member
    - Disable spanning tree

### Task List
[] Logic to determin if credential file exists 
[] Pull credentials from file into varialbles if file exists
[] Prompt user for info if file does not exist