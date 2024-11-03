<?php
$db_hostname = "127.0.0.1";
$db_username = "root";
$db_password = "";
$db_database = "login";
$conn=mysqli_connect($db_hostname,$db_username,$db_password,$db_database);
if(!$conn){
    echo "Connection Failed";
}
else{
    $name=$_POST['name'];
    $pn=$_POST['pn'];
    $age=$_POST['age'];
    $email=$_POST['email'];
    $password=$_POST['password'];
    $sql= "INSERT INTO login_details (name,age,phone_number,email,password) VALUES ($name,$age,$pn,$email,$password)";
    $result=mysqli_query($conn,$sql);
    if(!$result){
        echo "Value Not Entered";
    }
    else{
        echo "Value Entered";
    }
}
?>