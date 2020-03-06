<?php

class Joined {
    // property declaration
    private $poid;
    private $requesterid;
    private $paidStatus;
    
    public function __construct($poid='', $requesterid='', $paidStatus='') {
        $this->poid = $poid;
        $this->requesterid = $requesterid;
        $this->paidStatus = $paidStatus;
    }


    # Getter // Setter Methods
    public function getPoid(){
        return $this->poid;
    }
    public function setPoid($poid){
        $this->poid = $poid;
        return $this;
    }


    public function getRequesterid(){
        return $this->requesterid;
    }
    public function setRequesterid($requesterid){
        $this->requesterid = $requesterid;
        return $this;
    }


    public function getPaidStatus(){
        return $this->paidStatus;
    }
    public function setPaidStatus($paidStatus){
        $this->paidStatus = $paidStatus;
        return $this;
    }
}

?>