#include "./testing.h"

#include "slh/vec.h"

TEST(test_slh_vec_create_empty) {
    int *vec = slh_vec_create(0, sizeof(int));
    assert(vec != nullptr);
    assert(slh_vec_cap(vec) == 0);
    assert(slh_vec_size(vec) == 0);
}

TEST(test_slh_vec_create) {
    int *vec = slh_vec_create(10, sizeof(int));
    assert(vec != nullptr);
    assert(slh_vec_cap(vec) == 10);
    assert(slh_vec_size(vec) == 0);
    slh_vec_free(vec);
}

TEST(test_slh_vec_resize_no_change) {
    int *vec = slh_vec_create(10, sizeof(int));
    assert(vec != nullptr);
    assert(slh_vec_cap(vec) == 10);

    int *new_vec = slh_vec_resize(vec, 10);
    assert(new_vec == vec);
    assert(slh_vec_cap(new_vec) == 10);
    slh_vec_free(vec);
}

TEST(test_slh_vec_shrink) {
    int *vec = slh_vec_create(10, sizeof(int));
    assert(vec != nullptr);
    assert(slh_vec_cap(vec) == 10);

    int *new_vec = slh_vec_resize(vec, 5);
    assert(new_vec == vec);
    assert(slh_vec_cap(new_vec) == 5);
    slh_vec_free(vec);
}

TEST(test_slh_vec_grow) {
    int *vec = slh_vec_create(0, sizeof(int));
    assert(vec != nullptr);
    assert(slh_vec_cap(vec) == 0);

    int *new_vec = slh_vec_resize(vec, 100);
    assert(slh_vec_cap(new_vec) == 100);
    slh_vec_free(vec);
}

TEST(test_slh_vec_append) {
    int *vec = slh_vec_create(0, sizeof(int));
    assert(vec != nullptr);
    assert(slh_vec_size(vec) == 0);

    for (int i = 0; i < 10; i++) {
        auto value = i * i;
        vec = slh_vec_append(vec, &value);
    }

    for (int i = 0; i < 10; i++) {
        assert(vec[i] == i * i);
    }
    slh_vec_free(vec);
}

TEST(test_slh_vec_find) {
    int *vec = slh_vec_create(10, sizeof(int));
    for (int i = 0; i < 10; i++) {
        vec = slh_vec_append(vec, &i);
    }

    for (int i = 0; i < 10; i++) {
        auto value = slh_vec_find(vec, &i);
        assert(value == i);
    }

    assert(slh_vec_find(vec, &(int){-1}) == -1);
    assert(slh_vec_find(vec, &(int){10}) == -1);

    slh_vec_free(vec);
}

MAIN(test_vec)
