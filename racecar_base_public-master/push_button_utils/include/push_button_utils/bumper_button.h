#ifndef BUMPER_BUTTON_H
#define BUMPER_BUTTON_H

#include <ros/ros.h>
#include "push_button_utils/jetsonGPIO.h"

class BumperButton {

public:
    BumperButton(ros::NodeHandle& nh, jetsonGPIO gpio);
    ~BumperButton();
    void start();

private:
    jetsonGPIO gpio_;
    ros::Publisher* button_pub_;
    double pub_rate_;
    bool initialized_;

};

#endif // BUMPER_BUTTON_H
