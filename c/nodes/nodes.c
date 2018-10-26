#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
		char *name;
		struct node **neighbors;
		int numberOfNeighbors;
} node_t;

node_t * createNewNode(char *name) {
	node_t * newNode = malloc(sizeof(node_t));
	newNode->name = malloc(strlen(name) + 1); // iirc strlen doesnt count \0
	newNode->numberOfNeighbors = 0;
	newNode->neighbors = malloc(sizeof(node_t));
	strcpy(newNode->name, name);
	return newNode;
}

void addNodeNeighbor(node_t *target, char *name) {
	// alloc for newNeighbor node_t
	node_t *newNeighbor = createNewNode(name);

	printf("newNeighbor: %s\n", newNeighbor->name);
	// target->neighbors[0] = newNeighbor;
	// printf("reallocing %i bytes\n", sizeof(node_t *) * (target->numberOfNeighbors + 1)); 
	target->neighbors = realloc(target->neighbors, sizeof(node_t *) * (target->numberOfNeighbors + 1));
	target->neighbors[target->numberOfNeighbors] = newNeighbor;
	(target->numberOfNeighbors)++;
}

int main(int argc, char *argv[]) {

	printf("Hello world\n");

	node_t **nodes; // array of pointers to all the nodes

	nodes = malloc(sizeof(node_t *) * 1000); // safe side
	int numberOfNodes;

	
	int i, j;
	node_t *ptr;

	char *string = malloc(sizeof(char) * 100);
	for (i = 0; i < 10; i++) {
		sprintf(string, "top level %i", i);
		ptr = createNewNode(string);
		printf("top level: %s\n", string);
		nodes[i] = ptr;
		numberOfNodes++;
		sprintf(string, "second level %i", i);
		for (j = 0; j < 3; j++) {
			addNodeNeighbor(ptr, string);
		}
	}

		printf("number of top level nodes: %i\n", numberOfNodes);

	for (i = 0; i < numberOfNodes; i++) {
		printf("top level node: %s\n", nodes[i]->name);
		for (j = 0; j < nodes[i]->numberOfNeighbors; j++) {
			printf("descendant node: %s\n", nodes[i]->neighbors[j]->name);
		}
	}
}










