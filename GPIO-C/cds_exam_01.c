#include <stdio.h>
#include <wiringPi.h>

#define LED1 4
#define LED2 5
#define CDS 0

int cdsControl(){
    pinMode(CDS, INPUT);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);

    digitalWrite(LED1, 0);
    digitalWrite(LED2, 0);
    delay(1000);

    while(1){
        if(digitalRead(CDS)==HIGH){
            digitalWrite(LED1, 1);
            digitalWrite(LED2, 1);
        }
        else{
            digitalWrite(LED1, LOW);
            digitalWrite(LED2, LOW);
        }
    }
}

int main(void){
    if(wiringPiSetup()==-1) return 1;

    cdsControl();

    return 0;
}