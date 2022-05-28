# LOXValveTesting

This project was inspired by the liquid bipropellant rocket engine in the Saturn V rocket. I focused on developing a test for the main Liquid Oxygen Valve, so here is a video of how I think the valve operates based on the Engine manual:
https://drive.google.com/file/d/1e4KaUaL7RqEZWFsBp6MMhwI2yefwOBes/view?usp=sharing


TODO Project Description 

## System Overview
![LOX Valve Testing Overview](https://user-images.githubusercontent.com/35115515/170798309-a6c3992c-7629-43ff-81a7-23ed34b37298.png)
Broadly, the test manager will communicate with a simulated LOX valve (which performs nominally) and a real LOX valve by giving environmental configuration data from the environment space. The test manager will compare the behavior of the simulated LOX valve and the real LOX valve given the environmental configuration and use this information to produce a model of the risk/performance of the real LOX valve given several environmental parameters.

## Class Diagram

TODO Class diagrm

Link to the F1 Engine Manual referenced:
https://www.pdf-archive.com/2016/10/21/rocketdyne-f1-engine-manual/rocketdyne-f1-engine-manual.pdf
