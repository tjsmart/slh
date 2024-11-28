cmake_minimum_required(VERSION 3.21)
project(slh VERSION 0.0.0 LANGUAGES C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_library(slh STATIC src/slh.c)
target_include_directories(slh PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
