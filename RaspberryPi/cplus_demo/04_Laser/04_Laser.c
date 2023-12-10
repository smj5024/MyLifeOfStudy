/**********************************************
 * ---------------Laser---------------
 * file name: Laser.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>
 
#define makerobo_LaserPin	0			//Laser pin


int main(void)
{
	// int res = 0;
	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (-1==wiringPiSetup())
	{
		printf("setup wiringPi failed\r\n!");
		return -1;
	}
	
	// set laser pin mode is output
	pinMode(makerobo_LaserPin, OUTPUT);
	//digitalWrite(makerobo_LaserPin, HIGH);			// open laser
	//pinMode(makerobo_LaserPin, INPUT);
	while (1)
	{
		digitalWrite(makerobo_LaserPin, HIGH);			// open laser
		delay(500);
		digitalWrite(makerobo_LaserPin, LOW);			// close laser
		delay(500);
		/*
		res = digitalRead(makerobo_LaserPin);
		if (0!=res)
		{
			printf("read laser signal: %d\r\n", res);
		}
		delay(500);
		*/
	}
	
	return 0;
}
