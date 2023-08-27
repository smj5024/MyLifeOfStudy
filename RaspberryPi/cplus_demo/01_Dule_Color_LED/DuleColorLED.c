/**********************************************
 * ---------------dule color LED---------------
 * file name: DuleColorLED.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
 #include <wiringPi.h>
 #include <softPwm.h>
 #include <stdio.h>
 
 #define makerobo_Led_PinRed	0			//red pin
 #define makerobo_Led_PinGreen	1			//green pin
 
  typedef unsigned char u8;
 
 /*******************************************
  * funciton: LED initialization
  * name: makerobo_led_Init
  * input: void
  * output: void
  * return: void
 *******************************************/
 void makerobo_led_Init(void)
 {
	 softPwmCreate(makerobo_Led_PinRed, 0, 100);
	 softPwmCreate(makerobo_Led_PinGreen, 0, 100);
 }
 
  /*******************************************
  * funciton: set the lightness of LED, range: [0x00, 0xff]
  * name: makerobo_led_Colorset
  * input: r_val--red lightness, 
  * input: g_val--green lightness
  * output: void
  * return: void
 *******************************************/
 void makerobo_led_Colorset(u8 r_val, u8 g_val)
 {
	 softPwmWrite(makerobo_Led_PinRed, r_val);
	 softPwmWrite(makerobo_Led_PinGreen, g_val);
 }


/*********************************************
 * function: main
 * name: main
 * input: void
 * output: void
 * return: 0 | -1
 ********************************************/
int main(void)
{
	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (-1==wiringPiSetup())
	{
		printf("setup wiringPi failed\r\n!");
		return -1;
	}
	makerobo_led_Init();
	
	while (1)
	{
		makerobo_led_Colorset(0xff, 0x00);		//red
		delay(500);
		makerobo_led_Colorset(0x00, 0xff);		//green
		delay(500);
		makerobo_led_Colorset(0x45, 0x45);
		delay(500);
		makerobo_led_Colorset(0x00, 0x00);
		delay(500);
		//makerobo_led_Colorset(0xff, 0xff);
		//delay(500);
	}
	
	return 0;
}
