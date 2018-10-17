#include "push_button_utils/bumper_button.h"
#include <std_msgs/Bool.h>

BumperButton::BumperButton(ros::NodeHandle& nh, jetsonGPIO gpio):
                                                                  gpio_(gpio),
                                                                  button_pub_(NULL),
                                                                  initialized_(false){
    ros::NodeHandle private_nh("~"); 
    std::string pub_topic = "push_button_state";
    pub_topic = private_nh.param("pub_topic", pub_topic);
    pub_rate_ = private_nh.param("pub_rate", 100);

    button_pub_ = new ros::Publisher(nh.advertise<std_msgs::Bool>(pub_topic, 1));

    /*
    ROS_INFO("About to export gpio");
    if(gpioExport(gpio)) {

        ROS_ERROR("Could not export gpio %d", gpio);
        return;
    }
    */

    ROS_INFO("About to set gpio direction");
    if(gpioSetDirection(gpio, inputPin)) {
        ROS_ERROR("Could not set gpio %d direction", gpio);
        return;
    }

    initialized_ = true;
    ROS_INFO("Bumper button initialized");
}

BumperButton::~BumperButton() {

    //gpioUnexport(gpio_);
    delete button_pub_;
}

void BumperButton::start() {

    if(!initialized_) {
        ROS_ERROR("Not correctly initialized, aborting");
        return;

    }

    ros::Rate rate(pub_rate_);
    while(ros::ok()) {

        unsigned int val;
	ROS_INFO_ONCE("Getting bumper button val");
        if(gpioGetValue(gpio_, &val)) {
            ROS_ERROR("Could not gpio value");
        } else {
            std_msgs::Bool button_msg;
            button_msg.data = !(val > 0); // Set to true if button pushed
            button_pub_->publish(button_msg);
        }

        rate.sleep();
    }

}

int main(int argc, char** argv) {

    ros::init(argc, argv, "bumper_button_node");
    ros::NodeHandle nh;

    jetsonGPIO gpio = gpio298;

    BumperButton bb(nh, gpio);
    bb.start();


}
