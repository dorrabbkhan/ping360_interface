# Ping360 Interface
Communication with the BlueROV Ping360 sonar programatically

By Muhammad Dorrabb Khan Niazi, Luis Alberto Perez Oteiza, Sergio Martinez
For Marine Robotics Spring 2021
Prof. Francesco Maurelli
Jacobs University Bremen

This repository contains all the code for the implementation of an interface with the ping360 sonar from BlueRobotics as part of the Marine Robotics course at Jacobs University Bremen.

## How to run

In order to save measurements into a file for later processing, take the following steps:

1. Change the port location of the Sonar in the file script.py in line 9
2. Install the requirements using: 
```
pip install -r requirements.txt
```
3. Run the following command to record measurements into a file:
```
python script.py > sonar.data
```
Note that Python 3 is required for this to work. 
