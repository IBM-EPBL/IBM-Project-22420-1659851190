#define echoPin 7
#define trigPin 10
long duration;
int distance;
void setup()
{
 Serial.begin(9600);
 pinMode(13,OUTPUT);
 pinMode(4,INPUT);
 pinMode(trigPin,OUTPUT);
 pinMode(echoPin,INPUT);
}
void loop()
{
 digitalWrite(13,LOW);
 int a= digitalRead(4);
 if(a==1){
 Serial.println("motion detected in the home");
 digitalWrite(13,HIGH);
 }
digitalWrite(trigPin,LOW);
delayMicroseconds(200);
digitalWrite(trigPin,HIGH);
delayMicroseconds(10);
digitalWrite(trigPin,LOW);
duration=pulseIn(echoPin,HIGH);
distance=(duration*0.034/2);
Serial.print("Distance : ");
Serial.print(distance);
Serial.println(" cm ");
delay(1000);
}
