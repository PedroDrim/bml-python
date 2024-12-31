#!/bin/bash
python3 -m unittest -v src/model/SimpleTableAnalysis/SimpleTableAnalysisTest.py 
python3 -m unittest -v src/model/Table/TableTest.py 
python3 -m unittest -v src/model/UserInfo/UserInfoTest.py 

python3 -m unittest -v src/provider/MaxValueAnalysis/MaxValueAnalysisTest.py 
python3 -m unittest -v src/provider/MinValueAnalysis/MinValueAnalysisTest.py 
python3 -m unittest -v src/provider/MeanAnalysis/MeanAnalysisTest.py 
