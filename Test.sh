#!/bin/bash
coverage run -m unittest -v \
            src/model/exception/BenchmarkException/BenchmarkExceptionTest.py \
            src/model/exception/DataReaderException/DataReaderExceptionTest.py \
            src/model/exception/InvalidParameterException/InvalidParameterExceptionTest.py \
            src/model/BenchmarkOutput/BenchmarkOutputTest.py \
            src/model/DataReader/DataReaderTest.py \
            src/model/TableAnalysis/TableAnalysisTest.py \
            src/model/TimeFormat/TimeFormatTest.py \
            src/model/UserInfo/UserInfoTest.py \
            src/provider/BenchmarkMeasure/BenchmarkMeasureTest.py \
            src/provider/LanguageSortAnalysis/LanguageSortAnalysisTest.py \
            src/provider/MergeSortAnalysis/MergeSortAnalysisTest.py \
            src/provider/QuickSortAnalysis/QuickSortAnalysisTest.py \
            src/provider/SummaryAnalysis/SummaryAnalysisTest.py \
            src/provider/TableReader/TableReaderTest.py 
