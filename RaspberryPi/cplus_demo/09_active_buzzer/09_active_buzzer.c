/**********************************************
 * ---------------active buzzer---------------
 * file name: active_buzzer.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <stdio.h>

#define makerobo_BuzzerPin		0			// active buzzer's pin

int main(void)
{
	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !");
		return -1;
	}

	// set buzzer pin mode is output
	pinMode(makerobo_BuzzerPin, OUTPUT);

	while (1) {
		// set pin low level, enable buzzer
		digitalWrite(makerobo_BuzzerPin, LOW);
		delay(100);		//delay 100ms
		// set pin high level, disable buzzer
		digitalWrite(makerobo_BuzzerPin, HIGH);
		delay(100);		//delay 100ms
	}

	return 0;
}