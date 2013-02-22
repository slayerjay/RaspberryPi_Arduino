#include <LiquidCrystal.h>
#include <Bounce.h>

#define BUTTON1 8
#define BUTTON2 12
#define LED 13

LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

byte state1 = 0;
byte state2 = 0;

boolean result1;
boolean result2;

Bounce bouncer1 = Bounce( BUTTON1,1000 );
Bounce bouncer2 = Bounce( BUTTON2,1000);

void setup() {
	pinMode(BUTTON1,INPUT);
	pinMode(BUTTON2,INPUT);
	pinMode(LED,OUTPUT);
	Serial.begin(9600);
	lcd.begin(16, 2);
	lcd.print("ready");
}
 
void loop() {
	checkButtons();
	if(result1){
		Serial.print(1);
		result1=false;
		delay(500);
	}
	if(result2){
		Serial.print(2);
		result2=false;
		delay(500);
	}
	if (Serial.available()) {
		delay(100);  //wait some time for the data to fully be read
		lcd.clear();
		int i = 0;
		while (Serial.available() > 0) {
			char c = Serial.read();
			i++;
			if(c=='\n'){
				lcd.setCursor(0, 1);
			}else if(i==16){
				lcd.setCursor(0, 1);
				lcd.write(c);
			}else{
				lcd.write(c);
			}
		}
	}
}

void checkButtons(){
	checkButton(&bouncer1, &state1, &result1);
		checkButton(&bouncer2, &state2, &result2);
}

void checkButton(Bounce* _bouncer, byte* _state, boolean* result){
	Bounce bouncer = *_bouncer;
	byte state = *_state;
	
	bouncer.update ( );
	int value = bouncer.read();

	if ( value == HIGH && state==0) {
		digitalWrite(LED, HIGH );
		*result = true;
		*_state=1;
	} else if( value == LOW && state==1){
		*_state=0;
		digitalWrite(LED, LOW );
	}
}
