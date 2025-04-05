#!/bin/bash
python3 -m unittest -v src/model/exception/BenchmarkException/BenchmarkExceptionTest.py 
python3 -m unittest -v src/model/exception/DataReaderException/DataReaderExceptionTest.py 
python3 -m unittest -v src/model/exception/InvalidParameterException/InvalidParameterExceptionTest.py 

python3 -m unittest -v src/model/BenchmarkOutput/BenchmarkOutputTest.py 
python3 -m unittest -v src/model/DataReader/DataReaderTest.py 
python3 -m unittest -v src/model/TableAnalysis/TableAnalysisTest.py 
python3 -m unittest -v src/model/TimeFormat/TimeFormatTest.py 
python3 -m unittest -v src/model/UserInfo/UserInfoTest.py 

python3 -m unittest -v src/provider/BenchmarkMeasure/BenchmarkMeasureTest.py 
python3 -m unittest -v src/provider/LanguageSortAnalysis/LanguageSortAnalysisTest.py
python3 -m unittest -v src/provider/MergeSortAnalysis/MergeSortAnalysisTest.py 
python3 -m unittest -v src/provider/QuickSortAnalysis/QuickSortAnalysisTest.py 
python3 -m unittest -v src/provider/SummaryAnalysis/SummaryAnalysisTest.py 
python3 -m unittest -v src/provider/TableReader/TableReaderTest.py 