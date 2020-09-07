# techbin-design-model
 Idea of designing trash can for smart cities to increase the people to use trash-can effectively.
 
## What is techbin:
 An intelligent trash-can that rewards people for what and how much throw as waste.
 
## What we used:

 ### Micro controller and Microprocessor:
     * Arduino - nano
     * Raspberry pi - 3b model
     
 ### Sensors:
     * Ultrasonic sensor
     * Loadcell
     * Infrared sensor
     * Fingerprint
     
 ### Database:
     * Mysql (oracle workbench)
     
 ### Powersource:
     * we used mobile charger (5.5v) adapter to power arduino and raspberry pi.
     ( use can use 9v battery to power arduino but raspiberry pi need high current to operate all connected
      sensors)
 
## Method of operation:
 * When people throw waste into trash-can the infrared sensor will cut and loadcell get activated.
 * The loadcell will measure the weight of the garbage.
 * Fingerprint will be activated and user have to keep their finger.
 * If the user have account already the amount of weight of will added up.
 * Based on the amount of weight the user will be rewarded.
 
 ## PitfallsL:
 * People will through stone,sand,iron rod,etc which have high weight to get reward.
 
 ## Our solution:
 * Measuring the weight and corresponding height will give us some idea.
 (usually the stone,iron rod will have high weight with small height )
 
 
