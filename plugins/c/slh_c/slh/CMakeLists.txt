include_directories(${CMAKE_SOURCE_DIR}/include)
file(GLOB SLH_LIBRARIES RELATIVE ${CMAKE_SOURCE_DIR}/lib ${CMAKE_SOURCE_DIR}/lib/*.a)
link_libraries(${SLH_LIBRARIES})
