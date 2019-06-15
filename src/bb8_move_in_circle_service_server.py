#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist


def my_callback(request):
    rospy.loginfo("MoveCircle Callback has been called")
    pub.publish(move(0.2,0,0,0,0,0.2))
    rospy.loginfo("Finised MoveCircle")
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split()))

def move(x1, y1, z1, x2, y2, z2):
    move = Twist()
    move.linear.x = x1
    move.linear.y = y1
    move.linear.z = z1

    move.angular.x = x2
    move.angular.y = y2
    move.angular.z = z2
    return move


rospy.init_node('service_server')
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called my_service with the defined callback

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rospy.spin() # maintain the service open.