#include <stdint.h>

#ifndef SLH_LIST
#define SLH_LIST

typedef struct slh_node_t {
	int32_t value;
	struct slh_node_t* next;
} slh_node_t;

slh_node_t* slh_list_create_node(int32_t value);

slh_node_t* slh_list_end(slh_node_t* node);

void slh_list_append(slh_node_t** node, int32_t value);

void slh_list_map(slh_node_t* node, void(*map)(slh_node_t*));

void slh_list_print(slh_node_t* node);

void slh_list_sort(slh_node_t** head);

#endif
