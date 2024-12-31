#!/bin/bash
python3 -m unittest -v src/model/exception/BenchmarkException/BenchmarkExceptionTest.py 
python3 -m unittest -v src/model/exception/DataReaderException/DataReaderExceptionTest.py 
python3 -m unittest -v src/model/exception/InvalidParameterException/InvalidParameterExceptionTest.py 

python3 -m unittest -v src/model/BenchmarkOutput/BenchmarkOutputTest.py 
python3 -m unittest -v src/model/DataReader/DataReaderTest.py 
python3 -m unittest -v src/model/TableAnalysis/TableAnalysisTest.py 
python3 -m unittest -v src/model/TimeFormat/TimeFormatTest.py 
python3 -m unittest -v src/model/UserInfo/UserInfoTest.py 

#python3 -m unittest -v src/provider/MaxValueAnalysisTest.py 
#python3 -m unittest -v src/provider/MinValueAnalysisTest.py 
#python3 -m unittest -v src/provider/MeanAnalysisTest.py 
