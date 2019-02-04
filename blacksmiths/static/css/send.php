<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'vendor/mpest/functions.php';
require_once 'vendor/mpest/phpmailer/PHPMailerAutoload.php';

#Vars
$emailsTo = array(
    'leadgreen2018@gmail.com',
);
$site = $_SERVER['SERVER_NAME'];


#Get
$name = getVariablePOST('name');
$phone = getVariablePOST('phone');
$comment = getVariablePOST('comment');

if(empty($phone)){
    header('Location: index.php');
    exit;
}


#Send mail
$message = '';
$message .= 'Имя: '.$name."<br>";
$message .= 'Телефон: '.$phone."<br>";
$message .= 'Комментарий: '.$comment."<br>";
$message .= 'Сайт: '.$site."<br>";
$message .= 'IP: '.getUserIP()."<br>";

$mail = new PHPMailer;
$mail->CharSet = "UTF-8";
$mail->setFrom('noreply@'.$site);

foreach($emailsTo as $emailTo){
    $mail->addAddress($emailTo);
}

$mail->isHTML(true);
$mail->Subject = 'Новая заявка с сайта: '.$site;
$mail->Body = $message;
$mail->send();
#/Send mail


#Redirect
header('Location: success.php');