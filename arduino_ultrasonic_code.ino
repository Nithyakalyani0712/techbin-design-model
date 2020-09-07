int trigPin = 8;
int echoPin = 9;


void setup() {
  Serial.begin(9600); 
   pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  // put your setup code here, to run once:

}

void loop() {
  long duration, distance;
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigPin, LOW);
  duration=pulseIn(echoPin, HIGH);
  distance =(duration/2)/29.1;
  delay(400);
 
 if((distance<=20)) 
  {
   Serial.println("1");
}
else{
  Serial.println("0");
}
 
}
