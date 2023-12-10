/**********************************************
 * ---------------passive buzzer---------------
 * file name: passive_buzzer.c
 * version: 1.0
 * author: Neal Shen
 *********************************************/
#include <wiringPi.h>
#include <softTone.h>
#include <stdio.h>

#define makerobo_BuzzerPin		0			// passive buzzer's pin
// define sound spectrum
// low C note frequence
#define Tone_CL1 				131
#define Tone_CL2 				147
#define Tone_CL3 				165
#define Tone_CL4 				175
#define Tone_CL5 				196
#define Tone_CL6 				221
#define Tone_CL7 				248
// middle C note frequence
#define Tone_CM1 				262
#define Tone_CM2 				294
#define Tone_CM3 				330
#define Tone_CM4 				350
#define Tone_CM5 				393
#define Tone_CM6 				441
#define Tone_CM7 				495
// high C note frequence
#define Tone_CH1 				525
#define Tone_CH2 				589
#define Tone_CH3 				661
#define Tone_CH4 				700
#define Tone_CH5 				786
#define Tone_CH6 				882
#define Tone_CH7 				990

// the first song 's spectrum
int makerobo_song_1 [] = {
	Tone_CM3, Tone_CM5, Tone_CM6, Tone_CM3, Tone_CM2, Tone_CM3, 
	Tone_CM5, Tone_CM6, Tone_CH1, Tone_CM6, Tone_CM5, Tone_CM1,
	Tone_CM3, Tone_CM2, Tone_CM2, Tone_CM3, Tone_CM5, Tone_CM2,
	Tone_CM3, Tone_CM3, Tone_CL6, Tone_CL6, Tone_CL6, Tone_CM1,
	Tone_CM2, Tone_CM3, Tone_CM2, Tone_CL7, Tone_CL6, Tone_CM1,
	Tone_CL5
};

// the first song 's beat
int makerobo_beat_1 [] = {
	1,1,3,1,1,3,
	1,1,1,1,1,1,
	1,1,3,1,1,3,
	1,1,1,1,1,1,
	1,2,1,1,1,1,
	1,1,1,1,3
};

// the second song 's spectrum
int makerobo_song_2 [] = {
	Tone_CM1, Tone_CM1, Tone_CM1, Tone_CL5, Tone_CM3, Tone_CM3, 
	Tone_CM3, Tone_CM1, Tone_CM1, Tone_CM3, Tone_CM5, Tone_CM5,
	Tone_CM4, Tone_CM3, Tone_CM2, Tone_CM2, Tone_CM3, Tone_CM4,
	Tone_CM4, Tone_CM3, Tone_CM2, Tone_CM3, Tone_CM1, Tone_CM1,
	Tone_CM3, Tone_CM3, Tone_CM2, Tone_CL5, Tone_CL7, Tone_CM2,
	Tone_CM1
};

// the first song 's beat
int makerobo_beat_2 [] = {
	1,1,1,3,1,1,
	1,3,1,1,1,1,
	1,1,3,1,1,1,
	2,1,1,1,3,1,
	1,1,3,3,2,3,
};
int main(void)
{
	int i;

	// if the initialization is failed, print the infomation
	// on the screen of raspberrypi
	if (wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !");
		return -1;
	}
	
	// simulate Tone lib initilate, print messages on the screen
	if (softToneCreate(makerobo_BuzzerPin) == -1) {
		printf("makerobo setup softTone failed !");
		return -1;
	}

	while (1) {
		printf("makerobo music is being played...\n");  // play the song
		// play the first song
		for (i=0; i<sizeof(makerobo_song_1)/4; i++) {
			softToneWrite(makerobo_BuzzerPin, makerobo_song_1[i]);
			// the first song's spectrum
			delay(makerobo_beat_1[i] * 500);  // the song's beats
		}
		// play the second song
		for (i=0; i<sizeof(makerobo_song_2)/4; i++) {
			softToneWrite(makerobo_BuzzerPin, makerobo_song_2[i]);
			// the second song's spectrum
			delay(makerobo_beat_2[i] * 500);  // the song's beats
		}
		
	}

	return 0;
}
