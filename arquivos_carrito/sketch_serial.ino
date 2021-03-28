
int E1 = 14;   // velocidade motor 1
int E2 = 15;   // velocidade motor 2
int M1 = 16;   // direção motor 1 - DIREITA
int M2 = 17;   // direção motor 2 - ESQUERDA



char a = 0;

void setup(void) {
  // put your setup code here, to run once:


  int i;
  for (i = 14; i <= 17; i++)
    pinMode(i, OUTPUT);

  Serial.begin(9600);


}

void cima(int a)
{

  analogWrite(E1, a);
  digitalWrite(M1, LOW);
  analogWrite(E2, a);
  digitalWrite(M2, LOW);

  delay (1000);  // Procedimento de parada
  analogWrite(E1, 0);
  analogWrite(E2, 0);


}

void baixo(int a)
{

  analogWrite(E1, a);
  digitalWrite(M1, HIGH);
  analogWrite(E2, a);
  digitalWrite(M2, HIGH);

  delay (1000);
  analogWrite(E1, 0);
  analogWrite(E2, 0);
  

}

void esq(int a)
{

  analogWrite(E1, a);
  digitalWrite(M1, HIGH);
  analogWrite(E2, a);
  digitalWrite(M2, LOW);

  delay (1000);
  analogWrite(E1, 0);
  analogWrite(E2, 0);
  

}

void dir(int a)
{

  analogWrite(E1, a);
  digitalWrite(M1, LOW);
  analogWrite(E2, a);
  digitalWrite(M2, HIGH);

  delay (1000);
  analogWrite(E1, 0);
  analogWrite(E2, 0);


}



void loop(void) {
  // put your main code here, to run repeatedly:


  if (Serial.available()) {

    int val = Serial.read();


    switch (val)

    {
      case '0':
        cima(const int 150);
        break;

      case '1':
        baixo(const int 150);
        break;

      case '2':
        esq(const int 150);
        break;

      case '3':
        dir(const int 150);
        break;


    }


  }



}
