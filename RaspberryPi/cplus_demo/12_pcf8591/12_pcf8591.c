/**********************************************
 * -----------pcf8951---------------
 * file name: pcf8951.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <pcf8951.h>

#define makerobo_PCFPin			120			// pcf base pin

int main(void)
{
	int pcf_value;		// define a variable storing AIN input value
	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !");
		return -1;
	}

	// initial pcf basic pin and adress
	pcf8591Setup(makerobo_PCFPin, 0x48);

	while (1) {
		// access AIN0 value, using internal electric
		pcf_value = analogRead(makerobo_PCFPin + 0);
		printf("%d\n", pcf_value);
		// control aout , and then control LED
		analogWrite(makerobo_PCFPin + 0, pcf_value);
		delay(10);
	}
	return 0;
}