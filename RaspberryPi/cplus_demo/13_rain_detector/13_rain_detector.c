/**********************************************
 * -----------rain detector---------------
 * file name: rain_detector.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <pcf8591.h>
#include <math.h>

#define makerobo_PCFPin			120			// pcf base pin
#define makerobo_DOpin 			0			// rain detector pin

// print the information about rain detector module
void makerobo_Print(int x)
{
	switch (x)
	{
	case 1:									// no rainbow
		printf("\n**********************\n");
		printf("* makerobo Not Raining *\n");
		printf("**********************\n\n");
		break;
	case 0:									// have rainbow
		printf("\n**********************\n");
		printf("* makerobo Raining!! *\n");
		printf("**********************\n\n");
		break;
	
	default:
		printf("\n**********************\n");
		printf("* Print value error. *\n");
		printf("**********************\n\n");
		break;
	}
}

int main(void)
{
	int makerobo_analogVal;				// define analogval memorizing varibale
	int makerobo_tmp, makerobo_status;	// define status information
	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !");
		return -1;
	}

	// initial pcf basic pin and adress
	pcf8591Setup(makerobo_PCFPin, 0x48);
	// set rain detector pin as input mode
	pinMode(makerobo_DOpin, INPUT);
	makerobo_status = 0;				// set status as 0

	while (1) {
		makerobo_analogVal = analogRead(makerobo_PCFPin + 0);
		// access AIN0 value, using internal electric
		printf("%d\n", makerobo_analogVal);
		makerobo_tmp = digitalRead(makerobo_DOpin);
		// read digital I/O pin, read rain detector module's Pin
		if (makerobo_tmp != makerobo_status)
		{
			makerobo_Print(makerobo_tmp);
			makerobo_status = makerobo_tmp;
		}
		delay(200);
	}
	return 0;
}
