<?php

# MINDY STILL WORKING ON TIS

// require_once 'include/common.php';

// $email = $_POST["email"];
// $password = $_POST["password"];

// $dao = new UserDAO();
// $user = $dao -> retrieve($email);

// if ($user == null || ($user->getPassword() != $password)) {
//     echo '<h1>Login Failed. Please try again!</h1>';
//     echo '<a href="./login.html">Back to login page</a>';
// }
// else {

//     $_SESSION["name"] = $user->getName();
//     $_SESSION["userid"] = $user->getUserid();

//     if ($_POST["user-type"] == "requester") {
//         $_SESSION["user-type"] = $_POST["user-type"];
//         header("Location: requester.html");
//     }

//     elseif ($_POST["user-type"] == "traveller") {
//         $_SESSION["user-type"] = $_POST["user-type"];
//         header("Location: traveller.html");
//     }
// }


######################### ORIGINAL #########################


 $email = $_POST["email"];
 $password = $_POST["password"];
// $user_type = $_POST["user-type"];
 
 if (empty($email) || empty($password)) {
     echo '<h1>No user ID or password</h1>';
    exit;
 }

//  elseif (empty($user_type)) {
//      echo '<h1>User type not selected!</h1>';
//  }

 else {
    # validate userid and password
    if(//$user_type == 'requester' && 
    $email == 'requester@smu.com' && $password == '123' ) {
        header ('Location: requester.html');
        exit;
    }
    elseif(//$user_type == 'traveller' && 
    $email == 'traveller@smu.com' && $password == '123') {
        header ('Location: traveller.html');
        exit;
    }
    else {
        echo '<h1>Login Failed. Please try again!</h1>';
        echo '<a href="login.html">Back to login page</a>';
    }
 }

     
?>