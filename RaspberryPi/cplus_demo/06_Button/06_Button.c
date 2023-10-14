/**********************************************
 * ---------------Button---------------
 * file name: Button.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <stdio.h>

#define makerobo_BtnPin	0			// press button pin
#define makerobo_Rpin	1			// red light pin
#define makerobo_Gpin	2			// green light pin

/**********************************************
 * function name: double_color
 * param: color
 * author: Neal Shen
 *********************************************/
void double_color(int color)
{
	// set Red light pin mode is output
	pinMode(makerobo_Rpin, OUTPUT);
	// set Green light pin mode is output
	pinMode(makerobo_Gpin, OUTPUT);

	if (color == 0)
	{
		digitalWrite(makerobo_Rpin, HIGH);
		digitalWrite(makerobo_Gpin, LOW);
	}
	else if (color == 1)
	{
		digitalWrite(makerobo_Rpin, LOW);
		digitalWrite(makerobo_Gpin, HIGH);
	}
	else
	{
		printf("makerobo double color led error\n");
	}


}

int main(void)
{
	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (-1==wiringPiSetup())
	{
		printf("setup wiringPi failed\r\n!");
		return -1;
	}

	// set Button pin mode is input
	pinMode(makerobo_BtnPin, INPUT);
	double_color(1);

	while(1) {
		// remove button press shake
		if (0 == digitalRead(makerobo_BtnPin))
		{
			delay(10);
			if (0 == digitalRead(makerobo_BtnPin))
			{
				double_color(0);
				printf("button is pressed\n");
			}
		}
		else if (1 == digitalRead(makerobo_BtnPin))
		{
			delay(10);
			if (1 == digitalRead(makerobo_BtnPin))
			{
				while (!digitalRead(makerobo_BtnPin));
				double_color(1);
				printf("no button is pressed\n");
			}
		}
	}


	return 0;
}
