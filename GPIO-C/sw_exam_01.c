#include <stdio.h>
#include <wiringPi.h>

#define LED1 4
#define LED2 5
#define SW 1 // BCM_GPIO 18

void switch_ctr(){
    pinMode(SW, INPUT);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);

    for(;;){
        digitalWrite(LED1, 0);
        digitalWrite(LED2, 0);

        if(digitalRead(SW) == 0){
            digitalWrite(LED1, 1); // on
            digitalWrite(LED2, 1); // on
            delay(1000);
        }
    }
}

int main(void){
    if(wiringPiSetup() == -1) return 1;

    switch_ctr();

    return0;
}