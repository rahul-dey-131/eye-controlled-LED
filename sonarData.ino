int trigPin = 12, echoPin = 11, ledPin = 8;
float pingTime, distance;

String eyeState;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(ledPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Controlling the Trigger Pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2000);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(15);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);

  // Distance Measurement
  pingTime = pulseIn(echoPin, HIGH) / 1000000.;
  distance = (331.5 * pingTime) / 2.;

  Serial.println(distance);

  if (Serial.available()) {
    eyeState = Serial.readStringUntil('\r');
    
    if (eyeState == "0") {
      digitalWrite(ledPin, HIGH);
    } else {
      digitalWrite(ledPin, LOW);
    }
  }

  delay(500);

}
