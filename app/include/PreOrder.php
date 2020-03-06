<?php

class PreOrder {
    // property declaration
    private $poid;
    private $travellerName;
    private $country;
    private $endDate;
    private $status;
    private $itemName;
    private $itemCatagory;
    private $price;
    
    public function __construct($poid='', $travellerName='', $country='', $endDate='', $status='', $itemName='', $itemCatagory='', $price='') {
        $this->poid = $poid;
        $this->travellerName = $travellerName;
        $this->country = $country;
        $this->endDate = $endDate;
        $this->status = $status;
        $this->itemName = $itemName;
        $this->itemCatagory = $itemCatagory;
        $this->price = $price;
    }


    # Getter // Setter Methods
    public function getPoid(){
        return $this->poid;
    }
    public function setPoid($poid){
        $this->poid = $poid;
        return $this;
    }


    public function getTravellerName(){
        return $this->travellerName;
    }
    public function setTravellerName($travellerName){
        $this->travellerName = $travellerName;
        return $this;
    }


    public function getCountry(){
        return $this->country;
    }
    public function setCountry($country){
        $this->country = $country;
        return $this;
    }


    public function getEndDate(){
        return $this->endDate;
    }
    public function setEndDate($endDate){
        $this->endDate = $endDate;
        return $this;
    }


    public function getStatus(){
        return $this->status;
    }
    public function setStatus($status){
        $this->status = $status;
        return $this;
    }


    public function getItemName(){
        return $this->itemName;
    }
    public function setItemName($itemName){
        $this->itemName = $itemName;
        return $this;
    }


    public function getItemCatagory(){
        return $this->itemCatagory;
    }
    public function setItemCatagory($itemCatagory){
        $this->itemCatagory = $itemCatagory;
        return $this;
    }


    public function getPrice(){
        return $this->price;
    }
    public function setPrice($price){
        $this->price = $price;
        return $this;
    }
}