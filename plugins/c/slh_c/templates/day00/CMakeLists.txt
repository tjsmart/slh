add_executable(part1 part1.c)
set_target_properties(
	part1 PROPERTIES RUNTIME_OUTPUT_DIRECTORY
	${CMAKE_CURRENT_SOURCE_DIR}
)
