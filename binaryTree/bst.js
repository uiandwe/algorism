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
            return this.search(node.getLeft(), key);
        }
        else{
            return this.search(node.getRight(), key);
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

    delete(node, key, parent){
        if(node.key == key){
            //no child
            if(node.getLeft() == null && node.getRight() == null){
                if(parent.getLeft().key == key){
                    parent.setLeft(null);
                }
                else{
                    parent.setRight(null);
                }
                return node = null;
            }
            //two child
            else if(node.getLeft() != null && node.getRight() != null){

            }
            //one child
            else{
                var new_child_node = null;

                if(node.getLeft() != null){
                    new_child_node = node.getLeft();
                }
                else{
                    new_child_node = node.getRight();
                }

                if(parent.getLeft().key == key){
                    parent.setLeft(new_child_node);
                }
                else{
                    parent.setRight(new_child_node);
                }

                return node = null;
            }


        }

        if(node.key < key){
            return this.delete(node.getLeft(), key, node);
        }
        else{
            return this.delete(node.getRight(), key, node);
        }
    }
}

console.log("bst");
var bst = new binarySearchTree(10);
console.log(bst);
console.log("---------------------------------");
console.log(bst.insert(bst, 11));
console.log("---------------------------------");
console.log(bst.insert(bst, 9));
console.log("---------------------------------");
console.log(bst.insert(bst, 12));
console.log("---------------------------------");



console.log(bst.search(bst, 12));
console.log("---------------------------------");
console.log(bst.search(bst, 15));
console.log("---------------------------------");


console.log("---------------delete-------------");
console.log(bst.delete(bst, 11, null));
console.log(bst);

// console.log(bst.delete(bst, 12, null));
// console.log(bst);
