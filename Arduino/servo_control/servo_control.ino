// the setup function runs once when you press reset or power the board
int led = 8;
int state;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {

}

void serialEvent(){
  
    if(Serial.available() > 0){
      if(Serial.peek() == 't'){
        Serial.read();
        state = Serial.parseInt();
        Serial.read();
        digitalWrite(led, state);
      }
      while(Serial.available() > 0){
        Serial.read();
      }
    }
}

