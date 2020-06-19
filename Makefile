CC=gcc
CCFLAGS=-Wall -Wextra -Wpedantic
CXX=g++
CXXFLAGS=-Wall -Wextra -Wpedantic
GTEST_LDFLAGS=-L/usr/local/lib -lgtest_main -lpthread -lgtest -lpthread
INCLUDE=-I src

.PHONY=clean test

all: bin/test_suite

bin/test_suite: test/test_suite.cpp src/problem-01-01.c src/problem-01-02.c
	$(CXX) $(CXXFLAGS) test/test_suite.cpp -o bin/test_suite $(INCLUDE) $(GTEST_LDFLAGS)

clean:
	rm -f bin/* obj/*

test: bin/test_suite
	bin/test_suite

