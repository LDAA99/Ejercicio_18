segunda: ejer182.png

ejer182.png: datos182.txt graf2_18.py
	python graf2_18.py

datos182.txt: 18seg
	./18seg >> datos182.txt

18seg: ejer_18seg.cpp
	c++ ejer_18seg.cpp -o 18seg




primera: ejer18.png

ejer18.png: datos18.txt graf18.py
	python graf18.py

datos18.txt: 18
	./18 >> datos18.txt

18: ejer_18.cpp
	c++ ejer_18.cpp -o 18



