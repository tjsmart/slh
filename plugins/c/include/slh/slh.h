#include <stdint.h>
#include "slh/ptr.h"

#ifndef SLH_SLH
#define SLH_SLH

typedef struct {
	char* err;
	int64_t answer;
} slh_solution_t;

slh_solution_t slh_solution_err(char* err);
slh_solution_t slh_solution_answer(int64_t answer);

int slh_main(
	int argc,
	char* argv[],
	slh_solution_t (*solution)(const slh_sized_ptr_t*)
);

#endif
