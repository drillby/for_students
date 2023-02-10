<?php
    if($_POST == []){
        die("Script nelze volat přímo");
    }
    if($_SERVER["REQUEST_METHOD"] == "POST") {
        foreach ($_POST as $key => $value) {
            echo $key, " ", $value, "<br>";
        }
    }
    else{
        die("Špatný druh požadavku");
    }
    if ($_POST["uname"] == ""){
        echo "Žádná hodnota uživatelského jména";
    }
    ?>