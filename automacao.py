#include <DHT.h>

// Define o pino onde o sensor DHT está conectado
#define DHTPIN 2     

// Escolhe o tipo de sensor: DHT11 ou DHT22
#define DHTTYPE DHT22   

// Define o pino do relé
#define RELEPIN 8

// Inicializa o sensor DHT
DHT dht(DHTPIN, DHTTYPE);

// Parâmetros de controle
float temperaturaLimite = 30.0; // Limite de temperatura em graus Celsius
float umidadeLimite = 40.0;     // Limite de umidade em %

void setup() {
  Serial.begin(9600);          // Inicializa a comunicação serial
  dht.begin();                 // Inicializa o sensor DHT
  pinMode(RELEPIN, OUTPUT);    // Configura o pino do relé como saída
  digitalWrite(RELEPIN, HIGH); // Mantém o relé desligado inicialmente (Nível HIGH para desativado)
}

void loop() {
  // Lê a temperatura e umidade do sensor DHT
  float umidade = dht.readHumidity();
  float temperatura = dht.readTemperature();

  // Verifica se a leitura do sensor é válida
  if (isnan(umidade) || isnan(temperatura)) {
    Serial.println("Falha na leitura do sensor!");
    return;
  }

  // Exibe os valores lidos
  Serial.print("Umidade: ");
  Serial.print(umidade);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" *C");

  // Lógica de controle da irrigação
  if (umidade < umidadeLimite && temperatura > temperaturaLimite) {
    // Condições de clima seco: ativa a irrigação
    digitalWrite(RELEPIN, LOW);  // Ativa o relé (Nível LOW para ativado)
    Serial.println("Irrigação ativada!");
  } else {
    // Mantém a irrigação desativada
    digitalWrite(RELEPIN, HIGH); // Desativa o relé (Nível HIGH para desativado)
    Serial.println("Irrigação desativada.");
  }

  // Tempo de espera antes da próxima leitura (exemplo: 10 segundos)
  delay(10000);
}
