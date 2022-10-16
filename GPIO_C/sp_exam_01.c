#include <stdio.h>
#include <wiringPi.h>
#include <softTone.h>

#define SPKR 6 // BCM_GPIO 25
#define TOTAL 32 // 학교 종 전체 계이름 수

int note[] = {
    391, 391, 440, 440, 391, 391, 329.63, 329.63, \
    391, 391, 329.63, 329.63, 293.66, 293.66, 0, \
    391, 391, 440, 440, 391, 391, 329.63, 392.63, \
    391, 329.63, 293.66, 329.63, 261.63, 261.63, 0
};

int schoolmusic(){
    int i;

    softToneCreate(SPKR);

    for(i=0;i<TOTAL;++i){
        softToneWrite(SPKR, note[i]);
        delay(280);
    }
}

int main(){
    if(wiringPiSetup() == -1) return 1;

    schoolmusic();

    return 0;
}