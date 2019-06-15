# ROS Services Basics 101

In this little project(Part of a coursework of [The Construct Sim Robot Ignite Academy](http://www.theconstructsim.com/)), I wrote a code to make the **BB8** robot move in a circle-like trajectory. This was implemented using **Services**. Following steps were performed:

-   Createe a Service Server that accepts an  **Empty**  service message and activates the circle movement. This service was called  **/move_bb8_in_circle**. and is defined in **bb8_move_in_circle_service_server.py** file.

-   Created a launch file called  **start_bb8_move_in_circle_service_server.launch** that starts a node that launches the  **bb8_move_in_circle_service_server.py**  file.

-   Created a new Python file called  **bb8_move_in_circle_service_client.py**  that calls the service  **/move_bb8_in_circle**.
-  Then, generated a new launch file called  **call_bb8_move_in_circle_service_server.launch**  that executes the code in the  **bb8_move_in_circle_service_client.py**  file.

-   Finally, when you launch this  **call_bb8_move_in_circle_service_server.launch**  file, BB-8 should move in a circle.

The lauch file can be launched as follows

```
roslaunch exercise32 call_bb8_move_in_circle_service_server.launch
```