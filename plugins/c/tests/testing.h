#ifndef SLH_TESTING_H
#define SLH_TESTING_H

#include <asm-generic/ioctls.h>
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <sys/ioctl.h>
#include <unistd.h>

typedef struct {
    void (*func)(void);
    const char *name;
} __slh_test_t;

#define __MAX_NUMBER_OF_TESTS 10000
static __slh_test_t __tests[__MAX_NUMBER_OF_TESTS];
static int __number_of_tests = 0;

void __register_test(void (*func)(void), const char *name) {
    assert(__number_of_tests < __MAX_NUMBER_OF_TESTS);
    __tests[__number_of_tests++] = (__slh_test_t){.func = func, .name = name};
}

void __run_all_tests() {
    for (int i = 0; i < __number_of_tests; ++i) {
        __slh_test_t test = __tests[i];
        printf(" [%d/%d] %s...", i + 1, __number_of_tests, test.name);
        test.func();
        printf(" passed\n");
    }
}

unsigned short __terminal_width() {
    struct winsize w;
    return ioctl(STDOUT_FILENO, TIOCGWINSZ, &w) != -1 ? w.ws_col : 0;
}

void __print_banner(char *name) {
    const auto width = __terminal_width();
    if (width == 0) {
        printf("%s\n", name);
        return;
    }
    char banner[width + 1];
    banner[width] = '\0';
    memset(banner, '-', width);
    memcpy(banner, name, strlen(name));
    printf("%s\n", banner);
}

#define TEST(func)                                                             \
    void func(void);                                                           \
    __attribute__((constructor)) static void register_##func(void) {           \
        __register_test(func, #func);                                          \
    }                                                                          \
    void func(void)

#define MAIN(name)                                                             \
    int main() {                                                               \
        __print_banner(#name);                                                 \
        __run_all_tests();                                                     \
    }

#endif // SLH_TESTING_H
