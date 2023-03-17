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
  - Configure underlay port group(s)
    - Remane "Underlay Port Group 1" to ==ug_port1==
    - Disable spanning tree
    - Allow bypass traffic
    - Allow non-routed traffic
    - Remane "Underlay Port Group 2" to ==ug_wifi== *For Airwall-75w's only*
  - Configure overlay port groups *repeat for each overlay port*
    - Remane port group to ==og_port*X*== where *X* is the port number of the member port
    - Disable spanning tree
    - Configure DHCP pass-through
- Allow passive device discovery on overlay port groups

### Task List
- [ ] Logic to determin if credential file exists 
- [ ] Pull credentials from file into varialbles if file exists
- [ ] Prompt user for info if file does not exist
- [ ] Task 3
- [ ] Task 4
- [ ] Task 5
- [ ] Task 6
- [ ] Task 7
- [ ] Task 8
- [ ] Task 9
- [ ] Task 10
- [ ] Task 11
- [ ] Task 12
- [ ] Task 13
- [ ] Task 14