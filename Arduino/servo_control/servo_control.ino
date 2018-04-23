#include <Servo.h>
Servo serX;
Servo serY;
Servo serZ;
String serialData;
int x  = 0;
void setup(){
  
  serX.attach(11);
  serY.attach(10);
  serZ.attach(9);
  delay(20);
  Serial.begin(9600);
  serX.write(90);
  serY.write(90);
  serZ.write(90);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.setTimeout(10);
}
void loop(){
 // not using this
 }
 void serialEvent() {
    digitalWrite(LED_BUILTIN, HIGH);
  
  serialData = Serial.readString();
  serX.write(parseDataX(serialData));
  serY.write(parseDataY(serialData));
  serZ.write(parseDataZ(serialData));
  
}


int parseDataX(String data){
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}

int parseDataY(String data){
  data.remove(0,data.indexOf("Y") + 1);
  return data.toInt();
}

int parseDataZ(String data){
  data.remove(0,data.indexOf("Z") + 1);
  return data.toInt();
}

  
  

