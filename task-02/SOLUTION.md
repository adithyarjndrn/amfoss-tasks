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


 Co ordinates: 9°05'38.1"N 76°29'30.8"E
