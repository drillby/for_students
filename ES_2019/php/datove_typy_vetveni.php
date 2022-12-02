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
    // základní datové typy
    $promenna = 40;
    $promenna_2 = "Text";
    $promenna_3 = true;
    $promenna_4 = 26.12;

    // přetypování
    $int_to_str = strval($promenna_4);
    $str_to_int = intval($int_to_str);

    // var_dump vs. echo
    var_dump($int_to_str);
    echo $promenna;
    ?>
    <!-- 
        můžeme rozdělovat php bloky,
        hodnoty proměnných zůstanou
    -->
    <?php
    echo $promenna_2;
    // vypsání hodnoty proměnné do stringu
    echo "<h1>$promenna</h1>";
    
    // základní podmínka
    if ($promenna_3) {
        echo "promenna_3 je true.";
    }
    else {
        echo "promenna_3 je false.";
    }

    // složená podmínka
    // && - logický AND
    // || - logický OR
    // ! - logická negace
    //if ($promenna > 30 && $promenna_2 == "Text") {
    if ($promenna > 30 || $promenna_2 == "Text") {
        echo "Podmínka je splněna";
    }
    else {
        echo "Podmínka není splněna";
    }
    ?>

    <?php
    // rozdělení php bloku uprostřed podmínky
    if ($promenna_3) {
        ?>
        <h3>Proměnná 3 je true</h3>
        <?php
    }
    else {
        ?>
        <h3>Proměnná 3 je false</h3>
        <?php
    }
    ?>
    <?php
    // if - else if - else
    if ($promenna < 20) {
        echo "Menší než 20";
    }
    else if ($promenna >= 20 && $promenna <= 40) {
        echo "Proměnná je v rozsahu 20 až 40";
    }
    else {
        echo "Větší než 40";
    }
    
    // vnořování podmínek
    if ($promenna_3){
        if(!$promenna_3){
            echo "";
        }
    }
    ?>
</body>
</html>