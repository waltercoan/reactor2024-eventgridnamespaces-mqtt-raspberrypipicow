# Raspberry Pi Pico W conectado ao Azure Event Grid Namespaces

[![Tecnologias](https://skillicons.dev/icons?i=azure,python,raspberrypi)](https://skillicons.dev)

## [Link: Gravação da Palestra](https://www.youtube.com/watch?v=YE3TbdKq-Ew)
## [Slides](slides/2024-01-18-Reactor-EventGridNamespacesMQTT-v3.pdf)

- Protocolo MQTT
- Linguagem Python
- Biblioteca umqtt.simple MQTTClient
  - [umqtt](https://mpython.readthedocs.io/en/master/library/mPython/umqtt.simple.html)

## Processo
1. Criar os certificados CA autoassinados conforme as instruções no tutoral [Certificado Cliente](https://learn.microsoft.com/en-us/azure/event-grid/mqtt-publish-and-subscribe-portal#generate-sample-client-certificate-and-thumbprint?WT.mc_id=IoT-MVP-5003638)
2. Ao criar o certificado para o dispositivo modificar o comando do passo 2 ou 4 para:
```
step certificate create client2-authn-ID client2-authn-ID.pem client2-authn-ID.key --ca C:/Users/walte/.step/certs/intermediate_ca.crt --ca-key C:/Users/walte/.step/secrets/intermediate_ca_key --no-password --insecure --not-after 2400h --kty=RSA
```
3. Converter o certificado e a chave privada para o formato binário DER
```
openssl x509 -outform der -in client2-authn-ID.pem -out client2.crt
```
```
openssl rsa -outform der -in client2-authn-ID.key -out client2.key
```
4. Os arquivos client2.crt e client2.key deve ser carregados para a pasta raiz do Raspberry Pi Pico W
5. Versão do MicroPython v1.22.1 on 2024-01-05; Raspberry Pi Pico W with RP2040 
6. Instalar os pacotes
   - micropython-umqtt.simple (versão 1.3.4)