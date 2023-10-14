/**********************************************
 * ---------------vibrate_switch---------------
 * file name: vibrate_switch.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <stdio.h>

#define makerobo_VibratePin	0			// press vibration_switch pin
#define makerobo_Rpin	1			// red light pin
#define makerobo_Gpin	2			// green light pin
int clb_tmp = 0;

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

void makerobo_Print(int x)
{
	if (x != clb_tmp)
	{
		if (x == 0)
		{
			printf("makerobo on\n");
		}
		if (x == 1)
		{
			printf("makerobo off\n");
		}

		clb_tmp = x;
	}
}

int main(void)
{
	int clb_status = 0;
	int clb_value = 1;

	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (-1==wiringPiSetup())
	{
		printf("setup wiringPi failed\r\n!");
		return -1;
	}

	// set Button pin mode is input
	pinMode(makerobo_VibratePin, INPUT);

	while(1) {
		clb_value = digitalRead(makerobo_VibratePin);
		// remove button press shake
		if (0 != clb_value)
		{
			clb_status++;
			if (clb_status > 1)
			{
				clb_status = 0;
			}
			
			double_color(clb_status);
			makerobo_Print(clb_status);
			delay(1000);
		}
	}


	return 0;
}