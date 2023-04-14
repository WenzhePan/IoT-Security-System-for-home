//ThatsEngineering
//Sending Data from Arduino to NodeMCU Via Serial Communication
//NodeMCU code

//Include Lib for Arduino to Nodemcu
#include <SoftwareSerial.h>
#include <ArduinoJson.h>

//Include Lib for Blinker
#define BLINKER_WIFI
#include <Blinker.h>

//sensor config
BlinkerNumber HUMI("humi");
BlinkerNumber TEMP("temp");
BlinkerText FIRE("fire");
BlinkerText MQ2("MQ2");
BlinkerNumber Depth("depth");
BlinkerNumber Echo("echo");
BlinkerNumber IR("IR");
BlinkerNumber M("M");
BlinkerNumber F2("F2");
BlinkerButton Button1("btn-1");
BlinkerButton Button2("btn-2");
//D6 = Rx & D5 = Tx
SoftwareSerial nodemcu(D6, D5);
SoftwareSerial arduino(D1, D2);
//Wifi config
char auth[]="f90d68049ada";
char ssid[]="房间";
char pswd[]="13306742122";

float humi_read = 0, temp_read = 0;
String fire_read,MQ2_read;
float echo_read = 0;
double depth_read = 0; 
float IR_read = 0;
int M_read = 0;
int F_read = 0;

int button1,button2;

void heartbeat(){
//  HUMI.print(humi_read);
//  TEMP.print(temp_read);
  FIRE.print(fire_read);
  MQ2.print(MQ2_read);
 // IR.print(IR_read);
}

void rtData()
{
  Blinker.sendRtData("temp",temp_read);
  Blinker.sendRtData("humi",humi_read);
  Blinker.sendRtData("depth",depth_read);
  Blinker.sendRtData("echo",echo_read);
  Blinker.sendRtData("IR",IR_read);
}

void dataStorage()
{
    Blinker.dataStorage("temp", temp_read);
    Blinker.dataStorage("humi", humi_read);
    Blinker.dataStorage("echo", echo_read);
    Blinker.dataStorage("depth", depth_read);
    Blinker.dataStorage("IR",IR_read);
    Blinker.dataStorage("fire",fire_read);
    Blinker.dataStorage("M",M_read);
    Blinker.dataStorage("F2",F_read);
}

void setup() {
  // Initialize Serial port
  Serial.begin(9600);
  nodemcu.begin(9600);
  arduino.begin(9600);
  while (!Serial) continue;
  // Initialize Blinker
  //BLINKER_DEBUG.stream(Serial);
  //BLINKER_DEBUG.debugAll();
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  Blinker.begin(auth,ssid,pswd);
  Blinker.attachHeartbeat(heartbeat);
  Blinker.attachRTData(rtData);
  Blinker.attachDataStorage(dataStorage);
  //BlinkerMIOT.attachQuery(miotQuery);
  Button1.attach(button1_callback);
  Button2.attach(button2_callback);  
}

void loop() {
  
  Blinker.run();
  
  StaticJsonDocument<1000> doc;
  DeserializationError error = deserializeJson(doc,nodemcu);

  if (error) {
    //Serial.println("Invalid Json Object");
    doc.clear();
    return;
  }

  Serial.println("JSON Object Recieved");
  Serial.print("Recieved Humidity:  ");
  float hum = doc["humidity"];
  Serial.println(hum);
  Serial.print("Recieved Temperature:  ");
  float temp = doc["temperature"];
  Serial.println(temp);
  Serial.print("Recieved Fire: ");
  String fire = doc["fire"];
  Serial.println(fire);
  double depth = doc["water_depth"];
  Serial.print("Recieved Water_depth: ");
  Serial.println(depth);
  float echo = doc["echo"];
  Serial.print("Recieved echo distance: ");
  Serial.println(echo);
  String MQ2 = doc["MQ2"];
  Serial.print("Recieved MQ2 : ");
  Serial.println(MQ2);
  int IR = doc["IR"];
  Serial.print("Recieved IR: ");
  Serial.println(IR);
  int M = doc["M"];
  Serial.print("M: ");
  Serial.println(M);
  int F = doc["F"];
  Serial.print("F: ");
  Serial.println(F);
  Serial.println("-----------------------------------------");
  humi_read = hum;
  temp_read = temp;
  fire_read = fire;
  depth_read = depth;
  echo_read = echo;
  MQ2_read = MQ2;
  IR_read = IR;
  M_read = M;
  F_read = F;
  Serial.print("M_read: ");
  Serial.println(M_read);
  //Blinker.delay(2000);
  Serial.println(button2);
  StaticJsonDocument<800> doc2;
  
  doc2["button1"] = button1;
  Serial.print("button1:");
  int tt = doc2["button1"];
  Serial.println(tt);
  doc2["button2"] = button2;
  int bb = doc2["button2"];
  Serial.println(bb);
  serializeJson(doc2,arduino);
  doc2.clear();
  //adelay(600); 
}



void button1_callback(const String & state){
  BLINKER_LOG("get button1 state: ", state);
  if(state == "tap"){
    button1 = 3;
    button2 = 0;
  }
}
void button2_callback(const String & state){
  BLINKER_LOG("get button2 state: ", state);
  if(state == "tap"){
    button2 = 2;
    button1 = 0;
  }
}
