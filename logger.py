const int windPin = A1;
const float Vref = 5.0;
const float maxWind = 30.0;   // m/s

const int pyrPin = A2;      
const float maxIrr = 2000.0; 

void setup() {
  Serial.begin(9600);
}

void loop() {
  float voltage_anemo = analogRead(windPin) * (Vref / 1023.0);
  float windSpeed = (voltage_anemo / Vref) * maxWind;

  int adc = analogRead(pyrPin);
  float voltage_pyrano = adc * (Vref / 1023.0);
  float irradiance = (voltage_pyrano / Vref) * maxIrr;

  Serial.print("Wind (m/s): ");
  Serial.println(windSpeed, 2);

  Serial.print(" | Irradiance (W/m^2): ");
  Serial.println(irradiance, 1);


  delay(500);
}
