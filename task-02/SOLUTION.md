# Open Terminal

cd ~/Desktop

mkdir Coordinate-Location

mkdir North

echo 9° > NDegree.txt

echo 5' > NMinutes.txt

echo 38.1"N > NSeconds.txt

car N* > NorthCoordinate.txt

mv NorthCoordinate.txt /home/pegasus/Desktop/Coordinates-Location

mv NorthCoordinate.txt North.txt

rmdir North

mkdir East

echo 76° > EDegree.txt

echo 29' > EMinutes.txt

echo 30.8" > ESeconds.txt

car E* > EastCoordinate.txt

mv EastCoordinate.txt /home/pegasus/Desktop/Coordinates-Location

mv EastCoordinate.txt East.txt

rmdir East

cat East.txt North.txt > Location-Coordinante.txt                                      

![Screenshot from 2021-10-10 22-23-10](https://user-images.githubusercontent.com/89097182/136742249-a02b863c-fa28-4ca6-b931-911e141d2743.png)


 Co ordinates: 9°05'38.1"N 76°29'30.8"E
