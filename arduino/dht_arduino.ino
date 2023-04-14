//ThatsEngineering
//Sending Data from Arduino to NodeMCU Via Serial Communication
//Arduino code

//Sensor Lib
#include <DHT.h>

//Arduino to NodeMCU Lib
#include <SoftwareSerial.h>
#include <ArduinoJson.h>

//Initialise Arduino to NodeMCU (5=Rx & 6=Tx)
SoftwareSerial nodemcu(5, 6);
SoftwareSerial arduino(11,12);

//Initialisation of DHT11 Sensor
#define DHTPIN 23
DHT dht(DHTPIN, DHT11);
float temp;
float hum;

//Initialisation of Fire Sensor
#define buttonpin 22
//int buttonpin=22;
int fire_val;
String fire;
int F;

//Initialisation of Echo Sensor
const int TrigPin = 26;
const int EchoPin = 27;
float cm;

//Initialisation of Buzzer
const int Buffer = 8;

//Initialisation of Water
const int Water = 0;
float water_temp,water_data;

//Initialisation of MQ2
#define Sensor_DO 10
#define Sensor_AO A1
unsigned int sensorValue = 0;
String MQ2;
int M;

//Initiallisation of Servo.h
int servoPin = 4;
int pos = 0;
int button1,button2;

//Initiallisation of IR
int count=0;
int out = 0;
int IR_val;
bool b=false;
const int IRpin = 7;

void setup() {
  Serial.begin(9600);
  pinMode(buttonpin,INPUT);
  pinMode(TrigPin, OUTPUT);
  pinMode(EchoPin, INPUT);
  pinMode(Buffer, OUTPUT);
  pinMode(Sensor_DO,INPUT);
  pinMode(servoPin, OUTPUT);
  pinMode(IRpin, INPUT);
  dht.begin();
  nodemcu.begin(9600);
  arduino.begin(9600);
  button1 = 0;
  button2 = 0;
  delay(1000);

  Serial.println("Program started");
}

void loop() {
  StaticJsonDocument<600> doc2;
  DeserializationError error = deserializeJson(doc2,arduino);
  if(error){
    Serial.println("出错");
    Serial.println("-------------------");
  }
  Serial.println("-------------------");
  button1 = doc2["button1"];
  button2 = doc2["button2"];
  Serial.println("Recieve Message");
  Serial.print("button1: ");
  Serial.println(button1);
  Serial.print("button2: ");
  Serial.println(button2);
  Serial.println("---------------------");
  StaticJsonDocument<2000> doc;
  //Obtain Temp and Hum data
  dht11_func();
  //Obtain fire_val
  fire_func(); 
  //Obtain Echo;
  Echo_func();
  //Obtain_Water
  Water_func();
  //Obtain_MQ2
  MQ2_func();
  //Obtain_servo
  servo_func();

  IRcount_func();
  //Assign collected data to JSON Object
  doc["humidity"] = hum;
  doc["temperature"] = temp; 
  doc["fire"] = fire;
  doc["echo"] = cm;
  doc["water_depth"] = water_data;
  doc["MQ2"] = MQ2;
  doc["IR"] = IR_val;
  doc["M"] = M;
  doc["F"] = F;
  //Send data to NodeMCU
  serializeJson(doc,nodemcu);
  //doc.printTo(nodemcu);
  doc.clear();

  delay(1000);
}

void dht11_func() {

  hum = dht.readHumidity();
  temp = dht.readTemperature();
  Serial.print("Humidity: ");
  Serial.println(hum);
  Serial.print("Temperature: ");
  Serial.println(temp);
  
}

void fire_func(){
  
  fire_val = digitalRead(buttonpin);
  if(fire_val==HIGH){
    fire = "燃气灶开启";
    F = 1;
    }
  else if(fire_val == LOW){
    fire = "燃气灶关闭";  
    F = 0;
    }
    Serial.print("F：");
    Serial.println(F);
    Serial.print("Fire: ");
    Serial.println(fire);
}

void Echo_func(){
   digitalWrite(Buffer, LOW);
   digitalWrite(TrigPin, LOW);
   delayMicroseconds(2);
   digitalWrite(TrigPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(TrigPin, LOW);
   
   cm = pulseIn(EchoPin, HIGH) / 58.0; // cm
   cm = (int(cm * 100.0)) / 100.0;
   Serial.print("Echo: ");
   Serial.println(cm);    
   if(cm>=2 && cm<=10){
    digitalWrite(Buffer, HIGH);
   }
}

void Water_func(){
  water_temp=(long)analogRead(0);
  water_data=(water_temp/650)*4;
  Serial.print("the depth is:");
  Serial.print(water_data);
  Serial.println("cm");
}

void MQ2_func(){
  //digitalWrite(Buffer, LOW);
  sensorValue = analogRead(Sensor_AO);
  Serial.print("Sensor AO Value = ");
  Serial.println(sensorValue);
  if(digitalRead(Sensor_DO) == LOW)
  {
    Serial.println("Alarm!");
    MQ2 = "烟雾报警";
    M = 1;
    digitalWrite(Buffer, HIGH);
  }
  else if(digitalRead(Sensor_DO) == HIGH){
    MQ2 = "正常";
    M = 0;
  }
  Serial.print("M = ");
  Serial.println(M);
}

void servo_func(){
  if(button1 == 3 ){
    servo(180);
    delay(100);
  }
  else if(button2 == 2){
    servo(90);
    delay(100);
  }

}

void servo(int angle){
  for(int i=0;i<50;i++){
    int pulsewidth = (angle * 11) + 500;
    digitalWrite(servoPin, HIGH);
    delayMicroseconds(pulsewidth);
    digitalWrite(servoPin, LOW);
    delayMicroseconds(20000 - pulsewidth);
  }
  delay(100);
}

void IRcount_func(){
  if (digitalRead(IRpin)==LOW)
  {
    if(b == false){
      b=true;
      count += 1;
      IR_val = 0;
      Serial.print("OK:");
      Serial.println(count);
      Serial.print("detected: ");
      Serial.println(IR_val);
    }
  }
  else{
    b=false;
    IR_val = 1;
    Serial.print("no detected: ");
    Serial.println(IR_val);
  }
 
//    IR_val = digitalRead(IRpin);
//    Serial.print("IR_val: ");
//    Serial.println(IR_val);
}
