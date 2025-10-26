#include "./testing.h"

#include <string.h>

#include "slh/slh.h"

TEST(test_slh_solution_err) {
    slh_solution_t sol = slh_solution_err("message");
    assert(strcmp(sol.err, "message") == 0);
}

TEST(test_slh_solution_answer) {
    slh_solution_t sol = slh_solution_answer(3);
    assert(sol.err == NULL);
    assert(sol.answer == 3);
}

MAIN(test_slh)
