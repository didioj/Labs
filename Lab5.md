# Lab 5:

## Part 1:


## Part 2:

### Makefile:

> block.o:  
>>    cc block.c -c -o block.o -fPIC  
>>    cc -shared block.o -o block.so  
>>    ar qc block.a block.o  
>>    cc ../program.c block.a -o static_block.out  
>>    cc ../program.c block.so -o dynamic_block.out -Wl,-rpath .

> clean:  
>>    rm \*.o  
>>    rm \*.a  
>>    rm \*.so  
>>    rm \*.out  

### CMakeFile:

cmake_minimum_required(VERSION 3.0)  

project(Blocks)  

add_library(staticblocks STATIC block.c)  

add_library(dynamicblocks SHARED block.c)  

add_executable(program1 ../program.c)  

add_executable(program2 ../program.c)  

target_link_libraries(program1 dynamicblocks)  

target_link_libraries(program2 staticblocks)  
