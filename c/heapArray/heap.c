#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Implement HEAP with array
functions:
swapNodes
heapRemoveMin
heapInsert
 */

typedef struct node {
		int key;
		int element;
} node_t;

void swapNodes(node_t *a, node_t *b) {
	node_t tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}

// used during removeMin
node_t * heapRemoveLast(node_t *arrayHead, int *currentLength) {
	arrayHead = realloc(arrayHead, sizeof(node_t) * ((*currentLength) - 1));
	*currentLength = *currentLength - 1;
	return arrayHead;
}

/*
 * Remove root node and maintain/restore binary tree structure and heap-order property
*/
node_t * removeMin(node_t *arrayHead, int *currentLength) {
	// currentLength is number of elements, so arrayHead[*currentLength] will seg fault
	node_t *s;
	node_t *r; // pointers
	node_t *min = malloc(sizeof(node_t));
	int r_index = 0;
	// Edge case, heap is empty
	if (*currentLength == 0) {
		return NULL;
	}

	min->key = arrayHead[0].key;
	min->element = arrayHead[0].element;
	// if root has no children (its index * 2 is greater than currentLength) - we're done
	if (*currentLength == 1) {
		return min;
	}

	// First, copy the last node to the root
	arrayHead[0] = arrayHead[*currentLength - 1];
	// Remove the last node
	arrayHead = heapRemoveLast(arrayHead, currentLength);

	while (r_index < *currentLength) {
		r = &arrayHead[r_index];

		if ( (2 * r_index + 1) == *currentLength - 1) {
			// then r only has a left child and it's the last node!
			// point s to r's left child
			printf("Node with index %i has only a left child or is last node.\n", 2*r_index+1);
			s = &arrayHead[(2 * r_index + 1)];
			r_index = 2 * r_index + 1;
		}
		else if ( (2 * r_index + 2) <= *currentLength - 1 ) {
			printf("r's left: %i\n", arrayHead[2 * r_index + 1].key);
			printf("r's right: %i\n", arrayHead[2 * r_index + 2].key);

			// then r has two children, need to find the smallest of them
			// and swap if its key is less than r's key
			// if the left child is greater than the right ...
			if (arrayHead[2 * r_index + 1].key > arrayHead[2 * r_index + 2].key) {
				printf("r's left and right children: %i .. %i\n", arrayHead[2 * r_index + 1].key, arrayHead[2 * r_index + 2].key);
				// make s point to the right child
				s = &arrayHead[2 * r_index + 2];
				r_index = 2 * r_index + 2;
			}
			else {
				// otherwise make s point to the left child
				s = &arrayHead[2 * r_index + 1];
				r_index = 2 * r_index + 1;
			}
		}
		else {
			// we're at a leaf node,  this will let us out of the loop
			r_index = *currentLength;
		}
		// if r's key is greater than s's key, swap r and s
		if (r->key > s->key) {
			swapNodes(r, s);
		}
	}

	return min;
}

node_t * heapInsert(node_t *arrayHead, int *currentLength, int key, int element) {
	// first add a spot for the new element
	// printf("New array length: %i\n", *currentLength);
	arrayHead = realloc(arrayHead, sizeof(node_t) * ((*currentLength) + 1));
	arrayHead[*currentLength].key = key; // last element of array of n elements
	arrayHead[*currentLength].element = element;

	// now the new element is inserted at the tail of the array
	// need a loop to heap-bubble it up
	// this wont run for first node to be inserted since i would be 1
	// in pseudo code i/2 should be floor'd but C's integer division doesnt require this
	int i = *currentLength;
	node_t tmp;
	while (i > 0 && arrayHead[i/2].key > arrayHead[i].key ) {
		// as long as the current node's key is less than its parent, swap their places
		swapNodes(&arrayHead[i/2], &arrayHead[i]);
		i = i/2; // mover follows the new node that is bubbling up!
	}
	(*currentLength) = (*currentLength) + 1; // we grew the number of elements by 1

	return arrayHead;
}

int main(int argc, char *argv[]) {
	printf("Hubert's binary heap implementation\n");
	int currentLength = 0;
	node_t *nodeArray;
	node_t *min;

	// populate the tree with some random data
	nodeArray = heapInsert(nodeArray, &currentLength, 4, 4);
	nodeArray = heapInsert(nodeArray, &currentLength, 5, 5);
	nodeArray = heapInsert(nodeArray, &currentLength, 3, 5);
	nodeArray = heapInsert(nodeArray, &currentLength, 1, 5);
	nodeArray = heapInsert(nodeArray, &currentLength, 9, 5);
	nodeArray = heapInsert(nodeArray, &currentLength, 0, 5);
	nodeArray = heapInsert(nodeArray, &currentLength, 2, 5);
	nodeArray = heapInsert(nodeArray, &currentLength, 10, 5);

	printf("currentLength: %i ", currentLength);

	int i;
	for (i = 0; i < currentLength; i++) {
		printf("Heap array node %i has key: %i ... element: %i\n\n", i, nodeArray[i].key, nodeArray[i].element);
	}

	min = removeMin(nodeArray, &currentLength);
	// int i;
	for (i = 0; i < currentLength; i++) {
		printf("Heap array node %i has key: %i ... element: %i\n\n", i, nodeArray[i].key, nodeArray[i].element);
	}

	printf("Minimum key and element removed: %i and %i\n\n", min->key, min->element);
}










