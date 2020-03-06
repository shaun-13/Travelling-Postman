<?php

class Product {
    // property declaration
    private $name;
    private $category;
    
    public function __construct($name='', $category='') {
        $this->name = $name;
        $this->category = $category;
    }


    # Getter // Setter Methods
    public function getName(){
        return $this->name;
    }
    public function setName($name){
        $this->name = $name;
        return $this;
    }


    public function getCategory(){
        return $this->category;
    }
    public function setCategory($category){
        $this->category = $category;
        return $this;
    }
}

?>