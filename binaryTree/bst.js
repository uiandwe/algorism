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

        if(key < node.key){
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

        if(key < node.key){
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
                if(parent.getLeft() != null && parent.getLeft().key == key){
                    parent.setLeft(null);
                }
                else{
                    parent.setRight(null);
                }
            }
            //two child
            else if(node.getLeft() != null && node.getRight() != null){
                var new_child_node = node.getRight();
                var parent_node = null;
                while(true){
                    if(new_child_node.getLeft() == null){
                        break;
                    }
                    else{
                        parent_node = new_child_node;
                        new_child_node = new_child_node.getLeft();
                    }
                }

                if(parent_node != null){
                    if(new_child_node.getRight() != null){
                        parent_node.setLeft(new_child_node.getRight());
                    }
                    else{
                        parent_node.setLeft(null);
                    }
                }

                new_child_node.setLeft(node.getLeft());
                if(parent_node != null){
                    new_child_node.setRight(node.getRight());
                }

                if(parent != null){
                    if(parent.getLeft() != null && parent.getLeft().key == key){
                        parent.setLeft(new_child_node);
                    }
                    else{
                        parent.setRight(new_child_node);
                    }
                }
                else{
                    node = new_child_node;
                    return node;
                }


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

                if(parent.getLeft() != null &&  parent.getLeft().key == key){
                    parent.setLeft(new_child_node);
                }
                else{
                    parent.setRight(new_child_node);
                }

            }

            return node = null;
        }

        if(key < node.key){
            return this.delete(node.getLeft(), key, node);
        }
        else{
            return this.delete(node.getRight(), key, node);
        }
    }
}

console.log("bst");
var bst = new binarySearchTree(20);
console.log(bst);
console.log("---------------------------------");
console.log(bst.insert(bst, 11));
console.log("---------------------------------");
console.log(bst.insert(bst, 9));
console.log("---------------------------------");
console.log(bst.insert(bst, 12));
console.log("---------------------------------");
console.log(bst.insert(bst, 25));
console.log("---------------------------------");
console.log(bst.insert(bst, 22));
console.log("---------------------------------");
console.log(bst.insert(bst, 30));
console.log(bst.insert(bst, 28));
console.log(bst.insert(bst, 26));
console.log(bst.insert(bst, 27));
console.log("---------------------------------");


console.log("---------------search-------------");
console.log(bst.search(bst, 12));
console.log("---------------------------------");
console.log(bst.search(bst, 15));
console.log("---------------------------------");


console.log("---------------delete-------------");

// console.log(bst.delete(bst, 12, null));
// console.log(bst);

// console.log(bst.delete(bst, 11, null));
// console.log(bst);

console.log(bst = bst.delete(bst, 20, null));
console.log("---------------------------------");
console.log(bst);


