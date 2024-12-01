#include <stddef.h>

#ifndef SLH_PTR
#define SLH_PTR

typedef struct {
	char* ptr;
	size_t size;
} slh_sized_ptr_t;

slh_sized_ptr_t slh_sized_ptr_create(size_t size);

#endif
