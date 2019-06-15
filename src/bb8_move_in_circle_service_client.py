#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest # you import the service message python classes generated from Empty.srv.
import sys

rospy.init_node('bb8_move_in_circle_service_client')
rospy.wait_for_service('move_bb8_in_circle')
bb8_move_srv_client = rospy.ServiceProxy('move_bb8_in_circle', Empty)
bb8_move_srv_client_obj = EmptyRequest()

result = bb8_move_srv_client(bb8_move_srv_client_obj)
print result