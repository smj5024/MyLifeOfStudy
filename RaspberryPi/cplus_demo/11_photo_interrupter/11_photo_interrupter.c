/**********************************************
 * -----------photo interrupter---------------
 * file name: photo interrupter.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <stdio.h>

#define makerobo_LBPin			0			// photo interrupter pin
#define makerobo_Rpin			1			// red led pin
#define makerobo_Gpin			2			// green led pin

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

	if (color == 0)			// enable red led
	{
		digitalWrite(makerobo_Rpin, HIGH);
		digitalWrite(makerobo_Gpin, LOW);
	}
	else if (color == 1)	// enable green led
	{
		digitalWrite(makerobo_Rpin, LOW);
		digitalWrite(makerobo_Gpin, HIGH);
	}
	else
	{
		printf("makerobo double color led error\n");
	}


}

/**********************************************
 * function name: makerobo_Print
 * param: x
 * author: Neal Shen
 *********************************************/
void makerobo_Print(int x)
{
	if (x == 0)
	{
		printf("makerobo Light was blocked\n");
	}
}

int main(void)
{
	int clb_temp;
	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !");
		return -1;
	}

	// set photo interrupter pin mode is input
	pinMode(makerobo_LBPin, INPUT);

	while (1) {
		// detect 
		if (0 == digitalRead(makerobo_LBPin))
		{
			clb_temp = 1;
		}
		if (1 == digitalRead(makerobo_LBPin))
		{
			clb_temp = 0;
		}
		double_color(clb_temp);
		makerobo_Print(clb_temp);
	}
	return 0;
}