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
    include "menu.html";
    ?>
    <h1>Stránka produktu</h1>
    <?php
    include "vars.php";
    if($c) {
        for ($i=0; $i < $a; $i++) { 
            echo $b, "<br>";
        }
    }
    else {
        echo "Podmínka je false";
    }
    if ($_SESSION["je_prihlasen"]) {
        echo "Uživatel ", $_SESSION["username"], " je přihlášen.";
    }
    else {
        echo "Přihlášení se nezdařilo";
    }
    ?>
</body>
</html>