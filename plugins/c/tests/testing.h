#include <assert.h>
#include <stdio.h>

typedef struct {
	void (*func)(void);
	const char* name;
} __slh_test_t;


#define __MAX_NUMBER_OF_TESTS 10000
static __slh_test_t __tests[__MAX_NUMBER_OF_TESTS];
static int __number_of_tests = 0;

void __register_test(void (*func)(void), const char* name) {
	assert(__number_of_tests < __MAX_NUMBER_OF_TESTS);
	__tests[__number_of_tests++] = (__slh_test_t){.func=func, .name=name};
}

void __run_all_tests() {
	for (int i = 0; i < __number_of_tests; ++i) {
		__slh_test_t test = __tests[i];
		printf("running %s...", test.name);
		test.func();
		printf(" passed\n");
	}
}

#define TEST(func) \
	void func(void); \
	__attribute__((constructor)) \
	static void register_##func(void) { __register_test(func, #func); } \
	void func(void)


#define MAIN(name) \
	int main() { \
		__run_all_tests(); \
		printf("%s completed successfully\n", #name); \
	}
