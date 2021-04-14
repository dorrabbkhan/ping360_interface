#!/usr/bin/python3
import rospy
from brping import Ping360
from std_msgs.msg import Int32MultiArray, MultiArrayDimension, MultiArrayLayout

dim = MultiArrayDimension("dim", 1024, 1024)
lay = MultiArrayLayout([dim], 0)

myPing = Ping360()
myPing.connect_serial("/dev/ttyUSB0", 115200)
if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)
myPing.set_mode(1)

data = myPing.transmit()

def talker():
    pub = rospy.Publisher('ping360_interface/out', Int32MultiArray, queue_size=10)
    rospy.init_node('ping360_interface', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data = myPing.transmit()
        if data:
            data = [int(byte) for byte in data.data]
            msg = Int32MultiArray(data=data)
            print("Publishing...")
            pub.publish(msg)
        else:
            rospy.logerr("Failed to get distance data")
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass