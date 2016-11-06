class node{
    constructor(key){
        this.key = key;
    }

    getKey(){
        return this.key;
    }

}

class binarySearchTree extends node{
    constructor(left, right){
        this.left = left;
        this.right = right;
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

    insert(key){

    }
}

console.log("bst");