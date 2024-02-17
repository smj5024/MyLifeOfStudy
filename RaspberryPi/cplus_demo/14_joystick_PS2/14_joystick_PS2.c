/**********************************************
 * -----------joystick PS2---------------
 * file name: joystick_PS2.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <pcf8591.h>

#define makerobo_PCFPin			120			// pcf base pin

int pcf_AIN0 = makerobo_PCFPin + 0;			// AIN0 port
int pcf_AIN1 = makerobo_PCFPin + 1;			// AIN1 port
int pcf_AIN2 = makerobo_PCFPin + 2;			// AIN2 port

// direction status information
char *state[7] = {"home", "up", "down", "left", "right", "pressed"};

// direction judge function
int makerobo_direction()
{
	int ain_x, ain_y, ain_b;				// x, y, b is the status PS2 pressed
	int makerobo_tmp = 0;
	ain_x = analogRead(pcf_AIN1);			// x is AIN1 port
	ain_y = analogRead(pcf_AIN0);			// y is AIN0 port
	ain_b = analogRead(pcf_AIN2);			// b is AIN2 port
	if (ain_y <= 30)
	{
		makerobo_tmp = 1;					//up
	}
	if (ain_y >= 225)
	{
		makerobo_tmp = 2;					//down
	}
	if (ain_x >= 225)
	{
		makerobo_tmp = 4;					//right
	}
	if (ain_x <= 30)
	{
		makerobo_tmp = 3;					//left
	}
	if (ain_b == 0)
	{
		makerobo_tmp = 5;					//pressed
	}
	if (ain_x - 125 < 15 && ain_x - 125 > -15 && ain_y - 125 < 15 && ain_y - 125 > -15 && ain_b >= 60)
	{
		makerobo_tmp = 0;					//initial position
	}

	return makerobo_tmp;
}

int main(void)
{
	int makerobo_tmp = 0;					// current variable
	int makerobo_status = 0;				// status variable

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
		// callback direction judge function
		makerobo_tmp = makerobo_direction();
		if (makerobo_tmp != makerobo_status)
		{
			delay(1);
			if (makerobo_tmp == makerobo_direction())
			{
				printf("%s\n", state[makerobo_tmp]);
				makerobo_status = makerobo_tmp;
			}
		}
	}
	return 0;
}
