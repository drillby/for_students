<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    // include "neexistuje.php";
    // require "neexistuje.php";
    include "menu.html";
    ?>
    <h1>Hlavní stránka</h1>
    <?php
    require "menu.html";

    /* 
    login systém
    */

    /*
    heslo = "password123"
    */
    $heslo = "Password123";
    $sifra_heslo = sha1($heslo);
    echo $heslo, " ", $sifra_heslo;
    $_SESSION["username"] = "pepík";
    $_SESSION["je_prihlasen"] = TRUE;
    ?>
</body>
</html>