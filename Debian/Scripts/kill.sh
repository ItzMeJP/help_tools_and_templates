echo "Killing GZserver"
sleep 0.2
pkill gzserver
sleep 0.2
echo "Killing GZclient"
pkill gzclient
sleep 0.2
echo "Killing ROS Nodes"
rosnode kill -a
sleep 0.2
echo "Killing Rviz"
pkill rviz
sleep 0.2
echo "Killing Rosout"
pkill rosout
sleep 0.2
echo "Killing Rosmaster"
pkill rosmaster






