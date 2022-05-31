# LOXValveTesting

This project was inspired by the liquid bipropellant rocket engine in the Saturn V rocket. I focused on developing a test for the main Liquid Oxygen Valve, so here is a video of how I think the valve operates based on the Engine manual:
https://drive.google.com/file/d/1e4KaUaL7RqEZWFsBp6MMhwI2yefwOBes/view?usp=sharing

This project compares the predicted flow rate vs. measured flow rate of the aforementioned LOX valve. It compares these flow rates at 50 to 450 psi (inclusive) where the pressure drop across the valve ranges from 4.4 to 8psi (inclusive). Then produces a 3D plot of pressure difference (x-axis), lower pressure (y-axis), and absolute error (z-axis) that will look something like this:

<img width="355" alt="3D plot example" src="https://user-images.githubusercontent.com/35115515/171088854-00e071b4-8776-48e0-b868-270b5b7756d1.png">

Note: the data above is not realistic given I do not currently have the hardware to run such a test, so the "measured" data is synthetic in this case.

Currently, this project has a websocket client that is set up and ready to connect to a server that will give the client flowrates from the actual valve; however, I do not have the hardware to actually run this test. If I had access to a poppet valve, I would adjust the constants to a low-fidelity setup (e.g. using water instead of LOX) and use an Arduino ESP32 to host a websocket server that would give the client the necessary information.

This project assumes that the flow of liquid through the valve is laminar.

## System Overview

![LOX Valve Testing Overview](https://user-images.githubusercontent.com/35115515/171089675-2fb067ec-056d-4114-bcde-b4ce933fcaa7.png)


Broadly, the test manager will communicate with a simulated LOX valve (which performs nominally) and a real LOX valve by passing in pressure and pressure drop parameters. These two LOX valves will return their flow rates given these parameters, and the absolute error between the two produced flow rates will be plotted.

## Class Diagrams

TODO Class diagrm


# Resources Used for Learning about LREs

https://sma.nasa.gov/LaunchVehicle/assets/space-launch-report-falcon-9-data-sheet.pdf

https://www.nasa.gov/sites/default/files/files/SpaceX_NASA_CRS-6_PressKit-2.pdf

https://jasc-controls.com/thrust-vector-control-actuator/#:~:text=This%20actuator%20was%20designed%20to,EFSV%20first%2Dstage%20torque%20motor.

https://www.youtube.com/watch?v=Pigsq5rt-mY

https://www.youtube.com/watch?v=VA5VW-qapzs

https://www.youtube.com/watch?v=cNFJp6psQ6E

https://en.wikipedia.org/wiki/Thrust_vectoring

https://ntrs.nasa.gov/api/citations/20140002890/downloads/20140002890.pdf

https://www.sciencedirect.com/topics/physics-and-astronomy/thrust-vector-control

https://history.nasa.gov/conghand/propulsn.htm

https://www.britannica.com/technology/bipropellant-system

https://ntrs.nasa.gov/api/citations/19750003130/downloads/19750003130.pdf

https://www1.grc.nasa.gov/historic-facilities/rockets-systems-area/pumps-and-tanks/

https://www.provac.com/blogs/news/turbo-pumps-for-liquid-rocket-engines#:~:text=A%20rocket%20engine%20turbopump%20receives,the%20turbine%20of%20the%20turbopump.

https://en.wikipedia.org/wiki/Turbopump

https://www.youtube.com/watch?v=BaEHVpKc-1Q

https://www.youtube.com/watch?v=kOgMHypp0Cw

https://www.youtube.com/watch?v=LbH1ZDImaI8

https://www.reddit.com/r/spacex/comments/cxkrtb/detailed_diagram_of_the_raptor_engine_er26_gimbal/

https://ntrs.nasa.gov/citations/19780016336

https://www.youtube.com/watch?v=M5v7fnywRaE

http://heroicrelics.org/info/f-1/f-1-main-lox-valve.html

https://wha-international.com/case-study-lox-valve-internal-fire/

https://www.pdf-archive.com/2016/10/21/rocketdyne-f1-engine-manual/rocketdyne-f1-engine-manual.pdf

https://en.wikipedia.org/wiki/Poppet_valve

https://www.youtube.com/watch?v=-3LPBo6Rz1Q

https://www.youtube.com/watch?v=QESe6rDrfX8

https://www.eucass.eu/component/docindexer/?task=download&id=5929

https://www.youtube.com/watch?v=abldMtJLJaw

https://accessanesthesiology.mhmedical.com/content.aspx?bookid=974&sectionid=61586627#:~:text=This%20relationship%20can%20be%20expressed,establishes%20the%20direction%20of%20flow

https://allsensors.com/engineering-resources/white-papers/pressure-point-11-calculating-flow-rate-from-pressure-measurements

https://cgproducts.johnsoncontrols.com/met_pdf/347vb.pdf

https://www.geminivalve.com/valve-sizing-cv-flow-calculator/

https://link.springer.com/article/10.1007/s00348-017-2478-8

https://www.britannica.com/science/specific-gravity

https://www.engineeringtoolbox.com/specific-gravity-liquids-d_336.html

https://www.fujikin.co.jp/en/support/calculator/

https://en.wikipedia.org/wiki/Rocketdyne_F-1

