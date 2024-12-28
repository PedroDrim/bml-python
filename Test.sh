#!/bin/bash
python3 -m unittest -v src/model/SimpleTableAnalysisTest.py 
python3 -m unittest -v src/model/TableTest.py 
python3 -m unittest -v src/model/UserInfoTest.py 

python3 -m unittest -v src/provider/MaxValueAnalysisTest.py 
python3 -m unittest -v src/provider/MinValueAnalysisTest.py 
python3 -m unittest -v src/provider/MeanAnalysisTest.py 
