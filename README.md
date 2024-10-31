# Proof-of-Concept

Systemspecifikation: Säker IoT-lösning för Temperaturövervakning
1. Systemarkitektur

Virtuell Sensor: En Python-skript som simulerar en temperaturgivare. Den genererar slumpmässiga temperaturvärden mellan 20 och 30 grader Celsius och publicerar dessa till en MQTT-broker.
MQTT Broker (Mosquitto): Broker-mjukvaran Mosquitto används för att hantera och vidarebefordra data från sensorn. Den är konfigurerad för att ta emot meddelanden från klienten via en icke-krypterad MQTT-anslutning (port 1883) under testning. I ett produktionssystem skulle vi använda TLS för att skydda överföringen.

2. Kommunikationsflöde

Protokoll: Sensordata skickas över MQTT-protokollet från den virtuella sensorn till MQTT-brokern.
Dataöverföring: Den virtuella sensorn publicerar temperaturdata till ämnet sensor/temperature var 5
sekund. MQTT-brokern tar emot dessa meddelanden och gör dem tillgängliga för abonnenter.
Säker kommunikation: Under testningen körs anslutningen utan TLS. I en riktig miljö skulle TLS tillämpas för att skydda överföringen.

3. Säkerhetsåtgärder

MQTT Autentisering: MQTT-brokern använder ett autentiseringssystem med användarnamn och lösenord för att begränsa åtkomst till legitima enheter.
TLS-Kryptering (i produktion): För att skydda dataintegritet och konfidentialitet skulle TLS användas, vilket krypterar data mellan sensorn och brokern. I ett produktionssystem skulle vi lyssna på port 8883 (standardport för MQTT över TLS).

4. Cyber Resilience Act (CRA)-krav

Säkerhet-by-design:
Inbyggda säkerhetsfunktioner: Systemet är byggt med autentisering från start och är designat för att enkelt kunna utökas med TLS-kryptering i produktion för att skydda data mot obehörig åtkomst.
Rollbaserad åtkomst: En vidareutvecklad version skulle tillåta olika behörighetsnivåer för användare och administratörer.
Uppdaterbarhet:
Säkerhetsuppdateringar: Systemet skulle vara designat för att kunna uppdateras med säkerhetsfixar och förbättringar. Detta kan implementeras genom att konfigurera MQTT-brokern och IoT-enheter för att stödja OTA-uppdateringar.
Sårbarhetshantering:
Identifiering och hantering av sårbarheter: Regelbundna säkerhetsrevisioner och penetrationstester skulle utföras för att identifiera svagheter. Om en sårbarhet upptäcks kan MQTT-brokern snabbt konfigureras om eller uppdateras för att åtgärda hotet.

5. Framtida förbättringar

Implementering av ett larmsystem som varnar administratören om temperaturvärdena överstiger en viss gräns.
Utökad användarhantering med olika åtkomsträttigheter.
Ökad skalbarhet genom att integrera med molnbaserade tjänster för realtidsanalys och rapportering.
