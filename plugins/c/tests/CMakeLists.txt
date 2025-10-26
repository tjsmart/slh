file(GLOB TEST_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/test_*.c")

foreach(TEST_FILE ${TEST_SOURCES})
	# Get the base name of the test file (e.g., test_slh.c -> test_slh)
	get_filename_component(TEST_NAME ${TEST_FILE} NAME_WE)

	add_executable(${TEST_NAME} ${TEST_FILE})
	target_link_libraries(${TEST_NAME} PRIVATE slh)
	target_include_directories(${TEST_NAME} PRIVATE ../include)
endforeach()
