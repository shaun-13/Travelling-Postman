<?php

 $userid = $_POST['userid'];
 $password = $_POST['password'];
 $user_type = $_POST['user-type'];
 
 if (empty($userid) || empty($password)) {
     echo '<h1>No user ID or password</h1>';
    exit;
 }

 elseif (empty($user_type)) {
     echo '<h1>User type not selected!</h1>';
 }

 else {
    # validate userid and password
    if($user_type == 'requester' && $userid == 'requester@smu.com' && $password == '123') {
        header ('Location: requester.html');
        exit;
    }
    elseif($user_type == 'traveller' && $userid == 'traveller@smu.com' && $password == '123') {
        header ('Location: traveller.html');
        exit;
    }
    else {
        echo '<h1>Login Failed. Please try again!</h1>';
        echo '<a href="./index.html">Back to login page</a>';
    }
 }

     
?>