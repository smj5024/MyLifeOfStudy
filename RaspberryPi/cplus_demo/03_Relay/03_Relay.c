/**********************************************
 * ---------------relay---------------
 * file name: Relay.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>
 
#define makerobo_RelayPin	0			//relay pin


int main(void)
{
	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (-1==wiringPiSetup())
	{
		printf("setup wiringPi failed\r\n!");
		return -1;
	}
	
	// set relay pin mode is output
	pinMode(makerobo_RelayPin, OUTPUT);
	while (1)
	{
		digitalWrite(makerobo_RelayPin, HIGH);			// cut relay
		delay(1000);
		digitalWrite(makerobo_RelayPin, LOW);			// close relay
		delay(1000);
	}
	
	return 0;
}
