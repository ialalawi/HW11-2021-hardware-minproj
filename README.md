# HW11-2021-hardware-minproj
EC463 Hardware Miniproject Team #11
by Ismaeel AlAlawi and Laith Shamieh.

Using our modified ble_scan.py code to detect bluetooth devices using Raspberry Pi 4B in an area:
- Data logging started at 2:45 pm, Saturday September 11th, 2021. 
- Location: GSU, in the dining area in front of the Market, next to the last column in front of the boundary wall separating the supermarket
- Five entries lasting 1 minute each with a 1 minute interval in between 
- First entry: 2:45 pm, second entry 2:47 pm, third entry 2:49 pm, fourth entry 2:51 pm, fifth entry 2:53 pm

After Getting data from "ble_scan.py" which outputs it into a text file "hw11_miniproj_data.txt", we wrote the code ble_analysis.py which read the text file and removes the duplicates from the file then summing all the lines up and subtract 1 (because of the "Scanning BLE devices for 60 seconds" line) to get the total number of people during a 10 minute period. This code also outputs a modified file "hw11_miniproj_data_modified.txt" with no duplicates. 
