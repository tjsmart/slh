#include "./testing.h"

#include "slh/list.h"

TEST(test_slh_list_create_node) {
    slh_node_t *node = slh_list_create_node(-1);
    assert(node->value == -1);
    assert(node->next == NULL);
    slh_list_free(node);
}

TEST(test_slh_list_end) {
    slh_node_t *node1 = slh_list_create_node(1);
    slh_node_t *node2 = slh_list_create_node(2);
    slh_node_t *node3 = slh_list_create_node(3);

    node1->next = node2;
    node2->next = node3;

    assert(slh_list_end(node1) == node3);
    assert(slh_list_end(node2) == node3);
    assert(slh_list_end(node3) == node3);

    slh_list_free(node1);
}

TEST(test_slh_list_end_handles_null) { assert(slh_list_end(NULL) == NULL); }

TEST(test_slh_list_prepend) {
    slh_node_t *node = NULL;
    for (int i = 99; i >= 0; --i) {
        slh_list_prepend(&node, i * i);
    }

    int i = 0;
    while (node != NULL) {
        assert(node->value == i * i);
        node = node->next;
        i++;
    }

    assert(i == 100);

    slh_list_free(node);
}

TEST(test_slh_list_append) {
    slh_node_t *node = NULL;
    for (int i = 0; i < 100; ++i) {
        slh_list_append(&node, i * i);
    }

    int i = 0;
    while (node != NULL) {
        assert(node->value == i * i);
        node = node->next;
        i++;
    }

    assert(i == 100);

    slh_list_free(node);
}

void assert_values_are_incrementing(slh_node_t *node) {
    static int i = 0;
    assert(node->value == i++);
}

TEST(test_slh_list_map) {
    slh_node_t *node = NULL;
    for (int i = 0; i < 100; ++i) {
        slh_list_append(&node, i);
    }

    slh_list_map(node, assert_values_are_incrementing);
    slh_list_free(node);
}

TEST(test_slh_list_sort) {
    slh_node_t *node = NULL;
    for (int i = 99; i > -1; --i) {
        slh_list_append(&node, i);
    }

    slh_list_sort(&node);

    int i = 0;
    while (node != NULL) {
        assert(node->value == i);
        node = node->next;
        i++;
    }

    assert(i == 100);

    slh_list_free(node);
}

TEST(test_slh_list_size) {
    slh_node_t *node = NULL;
    assert(slh_list_size(node) == 0);
    for (int i = 1; i <= 100; ++i) {
        slh_list_append(&node, i);
        assert(slh_list_size(node) == i);
    }

    slh_list_free(node);
}

TEST(test_slh_list_index) {
    slh_node_t *node = NULL;
    for (int i = 0; i < 100; ++i) {
        slh_list_append(&node, i);
    }

    int i = 0;
    for (; i < 100; ++i) {
        slh_node_t *node_at_index = slh_list_index(node, i);
        assert(node_at_index->value == i);
        if (i == 99) {
            assert(node_at_index->next == NULL);
        } else {
            assert(node_at_index->next->value == i + 1);
        }
    }
    assert(i == 100);

    slh_list_free(node);
}

TEST(test_slh_list_find) {
    slh_node_t *node = NULL;
    for (int i = 0; i < 10; ++i) {
        slh_list_append(&node, i);
    }

    int32_t value = 0;

    bool find_value(slh_node_t * node) { return node->value == value; };

    value = 5;
    auto found_node = slh_list_find(node, find_value);
    assert(found_node != NULL);
    assert(found_node->value == 5);

    value = 10;
    found_node = slh_list_find(node, find_value);
    assert(found_node == NULL);

    found_node = slh_list_find(NULL, find_value);
    assert(found_node == NULL);

    slh_list_free(node);
}

TEST(test_slh_list_contains) {
    slh_node_t *node = NULL;
    for (int i = 0; i < 10; ++i) {
        slh_list_append(&node, i);
    }

    auto value = slh_list_contains(node, 5);
    assert(value == true);

    value = slh_list_contains(node, 10);
    assert(value == false);

    value = slh_list_contains(NULL, 1);
    assert(value == false);

    slh_list_free(node);
}

MAIN(test_list)
