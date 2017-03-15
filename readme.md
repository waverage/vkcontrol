# Vk controll

This program need for run your program in remote pc using vk dialogs as bridge.

## Requirements in remote pc
1. Connecting to internet
2. Python: ^3.5
3. [Vk api wrapper](https://pypi.python.org/pypi/vk/2.0.2)
4. Filled config
5. Runed main.py file

## Requirements in your pc.
1. Connecting to internet
2. Access to working vk account
3. [Created vk app](https://vk.com/editapp?act=create)
4. Dialog with oneself in vk

## How to
For send command you need to send message in dialog.
Command structure:
```
<command_name>: <arguments>
```
**<command_name>** is equal to file name in commands folder.

After sending command, program will be try to run command file and send response into vk dialog.
