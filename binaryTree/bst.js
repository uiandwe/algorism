"use strict";

class tree{
    constructor(key){
        this.key = key;
        this.left = null;
        this.right = null;
    }

    getKey(){
        return this.key;
    }

    setKey(key){
        return this.key = key;
    }

    getLeft(){
        return this.left;
    }

    getRight(){
        return this.right;
    }

    setLeft(left){
        return this.left = left;
    }

    setRight(right){
        return this.right =right;
    }


}

class binarySearchTree extends tree{

    constructor(key) {
        super(key);

    }

    search(node, key){
        if(node == null){
            return undefined;
        }

        if ( node.key == key){
            return node;
        }

        if(node.key < key){
            return search(node.getLeft(), key);
        }
        else{
            return search(node.getRight(), key);
        }
    }

    insert(node, key){
        if(node == null){

            var new_node = new binarySearchTree();
            new_node.setKey(key);
            return new_node;
        }

        if(node.key < key){
            node.setLeft(this.insert(node.getLeft(), key));
            return node;
        }
        else{
            node.setRight(this.insert(node.getRight(), key));
            return node;
        }
    }
}

console.log("bst");
var bst = new binarySearchTree(10);
console.log(bst);
console.log(bst.insert(bst, 11));
console.log(bst.insert(bst, 9));
console.log(bst.insert(bst, 12));

console.log(bst.search(bst, 14));