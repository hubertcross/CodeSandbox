#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define EXTERNAL -1

typedef struct node {
		struct node *left;
		struct node *right;
		struct node *parent;
		int key;
} node_t;

typedef struct tree {
	node_t *root;
} tree_t;

tree_t * init() {
	/* node_t *root = malloc(sizeof(node_t)); */
	node_t *root = NULL;
	tree_t *tree = malloc(sizeof(tree_t));

	tree->root = root;

	return tree;
}

node_t * treeSearch(node_t *node, int key) {
	// external node (has key of value EXTERNAL
	if (node->key == EXTERNAL) {
		return node;
	}
	if (node->key == key) {
		return node;
	}
	else if (node->key >= key) {
		return treeSearch(node->left, key);
	}
	else {
		return treeSearch(node->right, key);
	}
}

node_t * insert(node_t *root, int key) {
	node_t *w = treeSearch(root, key);

	// while w is internal
	while (w->key != EXTERNAL) {
		w = treeSearch(w->left, key);
	}
	// expand w into internal node with two extenral node children
	// w = malloc(sizeof(node_t));
	w->left = malloc(sizeof(node_t));
	w->right = malloc(sizeof(node_t));
	w->left->key = EXTERNAL;
	w->right->key = EXTERNAL;

	// set up parent pointers
	w->right->parent = w;
	w->left->parent = w;

	w->right->right = NULL;
	w->right->left = NULL;
	w->left->right = NULL;
	w->left->left = NULL;

	// store key in w
	w->key = key;

	return w;
}

void removeNode(node_t *root, int key) {
	node_t *n;
	node_t *tmp;

	n = treeSearch(root, key);

	// if we reached an external, the key does not exist in the tree
	if (n->key == EXTERNAL) {
		// do nothing and return
		return;
	}

	// if n is root node (root node is its own parent)
	if (n == n->parent) {
		if (n->right->key == EXTERNAL && n->left->key == EXTERNAL) {
			n->key = EXTERNAL;
			n->right = NULL;
			n->left = NULL;
			return;
		}
		else if (n->right->key == EXTERNAL && n->left->key != EXTERNAL) {
			n->key = n->left->key;
			n->left = n->left->left;
			return;
		}
		else if (n->left->key == EXTERNAL && n->right->key != EXTERNAL) {
			n->key = n->right->key;
			n->right = n->right->right;
			return;
		}
	}
	// if one child of n is external node
	// we must know which child is the external node so we can work with its sibling
	if (n->left->key == EXTERNAL) {
		// we must know if n is its parent's left or right child
		if (n->parent->left == n) { 
		// if n is its parents left child, link that parent to n's right child
			n->parent->left = n->right;
			n->right->parent = n->parent;
		}
		else if (n->parent->right == n) {
		// if n is its parent's right child, delink n from its parent and child
			n->parent->right = n->right;
			n->right->parent = n->parent;
		}
	}
	else if (n->right->key == EXTERNAL) {
		// remove n and n->left and replace with n->left
		if (n->parent->left == n) { 
			n->parent->left = n->left;
			n->left->parent = n->parent;
		}
		else if (n->parent->right == n) {
			n->parent->right = n->left;
			n->left->parent = n->parent;
		}		
	}
	else if (n->right->key != EXTERNAL && n->right->key != EXTERNAL) {
		// both children of n are internal nodes

		// find the left-most node in n's right subtree
		// (next node after n in an inorder traversal)
		// let this be y
		node_t *y = n->right;
		// find left-most internal node in n's right subtree
		while (y->left->key != EXTERNAL) {
			y = y->left;
		}

		n->key = y->key;
		
		// remove y from the tree
		// replace y with its (external child node)'s sibling
		y->right->parent = y->parent;
		if (y == y->parent->left) {
			y->parent->left = y->right;
		}
		else if(y == y->parent->right) {
			y->parent->right = y->right;
		}
		y = y->right;
	}
}

void inOrder(node_t *node, int depth) {
	int i;
	// printf("wtf");
	if (node == NULL) {
		return;
	}
	inOrder(node->left, depth + 1);
	// visit
	
	if (node->key != EXTERNAL) {
		for (i = 0; i < depth; i++) {
			printf("    ");
		}
		printf("key: %i\n", node->key);
	}
	inOrder(node->right, depth + 1);
}

int main(int argc, char *argv[]) {

	tree_t *tree = init();

	node_t *ptr = tree->root;
	node_t *n;

	// special case for root node
	ptr = malloc(sizeof(node_t));
	ptr->parent = ptr;
	ptr->left = NULL;
	ptr->right = NULL;
	ptr->key = EXTERNAL;

	insert(ptr, 2);
	// printf("ugh: %i\n", ptr->key);
	insert(ptr, 1);
	// printf("ugh: %i\n", ptr->left->key);
	insert(ptr, 3);
	// printf("ugh: %i\n", ptr->right->key);
	insert(ptr, 9);
	insert(ptr, 5);
	insert(ptr, 7);
	// insert(ptr, 2);

	// n = treeSearch(ptr, 2);
	// printf("ugh: %i\n", n->key);

	inOrder(ptr, 0);
	printf("\n\n");
	removeNode(ptr, 2);
	inOrder(ptr, 0);
	printf("\n\n");
	// removeNode(ptr, 7);
	// inOrder(ptr, 0);
	// printf("\n\n");

	// node_t *ugh = treeSearch(ptr, 9);
	// printf("ugh: %i\n", ugh->key);
	// printf("ugh: %x %x\n", ugh->left, ugh->right);
	// printf("ugh: %i %i\n", ugh->left->key, ugh->right->key);

	// ugh = treeSearch(ptr, 5);
	// printf("ugh: %i\n", ugh->key);
	// printf("ugh: %x %x\n", ugh->left, ugh->right);
	// printf("ugh: %i %i\n", ugh->left->key, ugh->right->key);	

	removeNode(ptr, 3);
	inOrder(ptr, 0);
	removeNode(ptr, 5);
	printf("\n\n");
	inOrder(ptr, 0);

	removeNode(ptr, 7);
	printf("\n\n");
	inOrder(ptr, 0);

	// 	ugh = treeSearch(ptr, 9);
	// printf("ugh: %i\n", ugh->key);
	// printf("ugh: %x %x\n", ugh->left, ugh->right);
	// printf("ugh: %i %i\n", ugh->left->key, ugh->right->key);	

	// printf("ugh: %x %i\n", ugh->parent, ugh->parent->key);

	// 	ugh = treeSearch(ptr, 1);
	// printf("ugh: %i\n", ugh->key);
	// printf("ugh: %p %p\n", (void *) ugh->left, (void *) ugh->right);
	// printf("ugh: %i %i\n", ugh->left->key, ugh->right->key);	

	removeNode(ptr, 9);
	printf("\n\n");
	inOrder(ptr, 0);

	// ugh = treeSearch(ptr, 1);
	// printf("ugh: %i\n", ugh->key);
	// printf("ugh: %x %x\n", ugh->left, ugh->right);
	// printf("ugh: %i %i\n", ugh->left->key, ugh->right->key);	

	removeNode(ptr, 1);
	printf("\n\n");
	inOrder(ptr, 0);


	insert(ptr, 2);
	// printf("ugh: %i\n", ptr->key);
	insert(ptr, 1);
	// printf("ugh: %i\n", ptr->left->key);
	insert(ptr, 3);
	// printf("ugh: %i\n", ptr->right->key);
	insert(ptr, 9);
	insert(ptr, 5);
	insert(ptr, 7);
	inOrder(ptr, 0);


}










