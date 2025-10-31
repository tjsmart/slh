cmake_minimum_required(VERSION 3.21)
project(slh VERSION 0.0.0 LANGUAGES C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_C_STANDARD_REQUIRED ON)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_library(
	slh STATIC
	src/input.c
	src/list.c
	src/ptr.c
	src/slh.c
	src/vec.c
)
target_include_directories(slh PUBLIC include)

add_subdirectory(tests)
