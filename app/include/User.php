<?php

class User {
    // property declaration
    private $userid;
    private $name;
    private $travellerid;    
    private $requesterid;
    private $password;
    private $email;
    
    public function __construct($userid='', $name='', $travellerid='', $requesterid='', $password='', $email='') {
        $this->userid = $userid;
        $this->name = $name;
        $this->travellerid = $travellerid;
        $this->requesterid = $requesterid;
        $this->password = $password;
        $this->email = $email;
    }
    
    public function authenticate($enteredPwd) {
        return password_verify ($enteredPwd, $this->password);
    }

    # Getter // Setter Methods
    public function getUserid(){
        return $this->userid;
    }
    public function setUserid($userid){
        $this->userid = $userid;
        return $this;
    }


    public function getName(){
        return $this->name;
    }
    public function setName($name){
        $this->name = $name;
        return $this;
    }

    
    public function getTravellerid(){
        return $this->travellerid;
    }
    public function setTravellerid($travellerid){
        $this->travellerid = $travellerid;
        return $this;
    }


    public function getRequesterid(){
        return $this->requesterid;
    }
    public function setRequesterid($requesterid){
        $this->requesterid = $requesterid;
        return $this;
    }


    public function getPassword(){
        return $this->password;
    }
    public function setPassword($password){
        $this->password = $password;
        return $this;
    }


    public function getEmail(){
        return $this->email;
    }
    public function setEmail($email){
        $this->email = $email;
        return $this;
    }
}

?>