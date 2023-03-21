# **Script to automate the Provisioning process**

## File: aw-provision.py
*File meant to run against the conductor to automate the process of provisioning new Airwalls*
### Syntaxt
``usage: aw-provision [cloud|dev|prod] [<serial-number>]``
### How it Works 
- Populate Conductor Location and Credential variables
  - Looks for URL/IP & API credentials in local file
  - If file is not found, promps for URL/IP & API credentials
- Look for serial numbers to provision - *If possible*
- Grant Provisioning Request - *If possible*
- Configure Airwall as **Managed** - *If possible*
- Ugrade Airwall firmware
- Configure Airwall group membership(s)
- Configure Ports
  - Configure underlay port group(s)
    - Rename **Underlay Port Group 1** to **ug_port1**
    - Disable spanning tree
    - Allow bypass traffic
    - Allow non-routed traffic
    - Rename **Underlay Port Group 2** to **ug_wifi** *For Airwall-75w's only*
  - Configure overlay port groups *repeat for each overlay port*
    - Add new or modify existing overlay port group
    - Select member port
    - Rename **Overlay Port Group *X*** to **og_port*X***where *X* is the port number of the member port
    - Disable spanning tree
    - Configure DHCP pass-through
- Allow passive device discovery on overlay port groups
- Configure airsh password - *If possible*

### Task List
- [ ] Determine if credential file exists 
- [x] Pull credentials from file into varialbles if file exists
- [ ] Prompt user for info if file does not exist
- [ ] Build list of Airwall IDs to provision
- [ ] Apply settings to Airwalls in list:
    - [ ] Managed status
    - [ ] Airwall group membership
    - [ ] Ugrage Firmware
- [ ] Replace Port-Group settings for each Airwall
- [ ] Configure DHCP Passthrough for Overlay Port groups for each Airwall
- [ ] Configure passive device discovery for Overlay Port groups for each Airwall
- [ ] Configure airsh password
