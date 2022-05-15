# README
Labolatorium RTA praca domowa 

# Instalacja projektu 
## Utworzenie obrazu Dockerowego
Aby stworzyć obraz Docker i włączyć aplikacje należy wywołać poniższe komendy w przestrzeni projektowej 

```
docker build -t myimage .    
docker run -p 5004:5004 -d myimage
```
## Endpoints
Aby otrzymać predykcje klasy dla zbioru 'Irys' należy wygnerować link z parametrami podanymi w linku 
```
http://127.0.0.1:5004/predict?petal_length=1&sepal_length=1
```
