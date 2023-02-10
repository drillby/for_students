<?php
function vypis_text($text)
{
    echo $text;
}

function validace_vstupu($vstup){
    return !($vstup == "");
}

function secti($cislo_1, $cislo_2){
    return $cislo_1 + $cislo_2;
}

function secti_2($cislo=20){
    echo 20 + $cislo;
}

$vysledek = secti(2, 3);

vypis_text(secti(2, 3));

secti_2();

$username = "Pepa";
$pw = "Heslo";
if (validace_vstupu($username) && validace_vstupu($pw)){
    echo "Přihlášen";
}
?>