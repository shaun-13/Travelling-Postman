<?php
spl_autoload_register(function($class) {  
    require_once "$class.php"; 
});

session_start();

# Function that checks if any of the values in assoc array is empty
function checkEmpty($value_array) {
    $error_array = array();
    foreach ($value_array as $key => $value) {
        if ($value == "") {
            $error_array[] = "blank " . $key; 
        }
    }

    return $error_array;
}


function isMissingOrEmpty($name) {
    if (!isset($_REQUEST[$name])) {
        return "missing $name";
    }

    // client did send the value over
    $value = $_REQUEST[$name];
    if (empty($value)) {
        return "blank $name";
    }
}

# this is better than empty when use with array, empty($var) returns FALSE even when
# $var has only empty cells
function isEmpty($var) {
    if (isset($var) && is_array($var))
        foreach ($var as $key => $value) {
            if (empty($value)) {
               unset($var[$key]);
            }
        }

    if (empty($var))
        return TRUE;
}

// function TokenValidation() {
//     $token = '';
//     $errors = array();
//     if  (isset($_REQUEST['token'])) {
//         $token = $_REQUEST['token'];
//         if (empty($token)) {
//             $errors[] = "blank token";
//         } else {
//             $valid = verify_token($token);
//             if(!$valid){
//                 $errors[] = "invalid token";
//     }
//         }

//     } else {
//         $errors[] = "missing token";
//     }

//     return $errors;
// }

// Common validation for JSON
function JsonCommonValidation($fields){

    $errors = [];
    
    // sort the fields array in ascending order (by field name)
    if (count($fields)!=1){
        sort($fields);
    }
    
    // if r={} is passed in
    if (isset($_REQUEST['r'])){
        $fields_found = json_decode($_REQUEST['r']);
    } elseif(count($fields) == 1){
        // if only one parameter is to be checked
        return 'missing '. $fields[0];
    }else{
        foreach ($fields as $field){
            $errors[] = 'missing '. $field;
        }
        return $errors;
    }
    
    // if only one parameter is to be checked
    if (count($fields)==1){
        if (empty((array) $fields_found)){
            return 'missing '. $fields[0];
        }else{
            $fields_found_array = (array)$fields_found;
            if ( empty(trim($fields_found_array[$fields[0]]))){
                return 'blank '. $fields[0];
            }
        }
    }
    
    // if multiple parameters are to be checked
    foreach ($fields as $field){
        if (!isset($fields_found->$field)){
            $errors[] = 'missing '. $field;
        }elseif (empty(trim($fields_found->$field))){
            $errors[] = 'blank '. $field;
        }
    }
    return $errors;
}


?>