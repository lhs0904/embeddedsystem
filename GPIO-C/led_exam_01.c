#include <stdio.h>
#include <wiringPi.c>

#define LED1 4     // BCM_GPIO 23
#define LED1 5     // BCM_GPIO 24

int main(){
    if(wiringPiSetup() == -1) return 1;  // wiringPi는 항상 wiringPiSetup() 함수를 통해 시작한다.

    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);

    for(;;){
        digitalWrite(LED1, 1);  // LED1 on
        digitalWrite(LED2, 1); // LED2 on

        delay(1000);

        digitalWrite(LED1, 0); // LED1 off
        digitalWrite(LED2, 0); // LED2 off

        delay(1000);
    }

    return 0;
}