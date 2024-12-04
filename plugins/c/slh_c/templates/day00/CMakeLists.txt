add_executable(day00_part0 part0.c)
set_target_properties(
	day00_part0 PROPERTIES
	RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
	OUTPUT_NAME part0
)
