// include the library code:
#include <LiquidCrystal.h>
#include <OneButton.h>


#define BUTTON1 8
#define BUTTON2 12
#define LED 13

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

OneButton button1(8, false);
OneButton button2(12, false);

void setup() {
  pinMode(LED,OUTPUT);
  button1.attachClick(c1);
  button2.attachClick(c2);

  button1.attachDoubleClick(dc1);
  button2.attachDoubleClick(dc2);
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("start");

}

void loop() {
  button1.tick();
  button2.tick();
  delay(10);
  if (Serial.available()) {
    delay(100);
    lcd.clear();
    int i = 0;
    while (Serial.available() > 0) {
      char c = Serial.read();
      i++;
      if(c=='\n'){
        lcd.setCursor(0, 1);
      }
      else if(i==16){
        lcd.setCursor(0, 1);
        lcd.write(c);
      }
      else{
        lcd.write(c);
      }
    }
  }
}

void dc1(){
  doubleClick(1);
}

void dc2(){
  doubleClick(2);
}

void c1(){
  click(1);
}

void c2(){
  click(2);
}

void doubleClick(int id){
  Serial.print(id);
  Serial.println(id);
}

void click(int id){
  Serial.println(id);
}


