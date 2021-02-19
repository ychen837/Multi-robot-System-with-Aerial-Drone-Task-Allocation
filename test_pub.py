import rospy
from std_msgs.msg import String


def test_func():
    ans = 1+1
    return ans


def callback(data):
    rospy.loginfo('received', data)


def talker():
    sub = rospy.Subscriber('/test_topic', String, callback)
    pub = rospy.Publisher('/test_pub', String, queue_size=1)
    pub2 = rospy.Publisher('/test_pub2', String, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_string = 'hello world'
        bye_string = 'goodbye world'
        ans = test_func()
        pub.publish(hello_string)
        pub2.publish(ans)
        rospy.loginfo(hello_string)
        rospy.loginfo(bye_string)
        rate.sleep()



if __name__ == '__main__':
    try:
        talker()
        # talker2()
    except rospy.ROSInterruptException:
        pass

