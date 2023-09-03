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
 #define makerobo_Led_PinBlue	2			//blue pin
 
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
	 softPwmCreate(makerobo_Led_PinBlue, 0, 100);
 }
 
  /*******************************************
  * funciton: set the lightness of LED, range: [0x00, 0xff]
  * name: makerobo_led_Colorset
  * input: r_val--red lightness, 
  * input: g_val--green lightness,
  * input: b_val--blue lightness
  * output: void
  * return: void
 *******************************************/
 void makerobo_led_Colorset(u8 r_val, u8 g_val, u8 b_val)
 {
	 softPwmWrite(makerobo_Led_PinRed, r_val);
	 softPwmWrite(makerobo_Led_PinGreen, g_val);
	 softPwmWrite(makerobo_Led_PinBlue, b_val);
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
		makerobo_led_Colorset(0xff, 0x00, 0x00);		//red
		delay(500);
		makerobo_led_Colorset(0x00, 0xff, 0x00);		//green
		delay(500);
		makerobo_led_Colorset(0x00, 0x00, 0xff);		//blue
		delay(500);
		makerobo_led_Colorset(0xff, 0xff, 0x00);		//yellow
		delay(500);
		makerobo_led_Colorset(0xff, 0x00, 0xff);		//pick
		delay(500);
		makerobo_led_Colorset(0xc0, 0xff, 0x3e);		
		delay(500);
		makerobo_led_Colorset(0x94, 0x00, 0xd3);		
		delay(500);
		makerobo_led_Colorset(0x76, 0xee, 0x00);		
		delay(500);
		makerobo_led_Colorset(0x00, 0xc5, 0xcd);		
		delay(500);
	}
	
	return 0;
}
