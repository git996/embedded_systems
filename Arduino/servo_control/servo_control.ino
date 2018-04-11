#include <Servo.h>
Servo serx;
int x  = 0;
void setup(){
  
  serx.attach(11);
  sery.attach(10)
  serx.write(0);
  serx.write(0);
  delay(2000);
}
void loop(){
 
  if (x < 179){
    serx.write(x);
    sery.write(x);
    delay(500);
    x = x+10;
  }
  if (x > 179){
    x = 0;
  }
   
 }


  
  

