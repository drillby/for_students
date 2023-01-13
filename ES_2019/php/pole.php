<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=;, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
    // indexované pole
    $pole = [1, 2, 3, 4, 5];
    echo $pole[1];

    for ($i=0; $i < count($pole); $i++) { 
        echo $pole[$i];
    }
    
    // asociativní pole ve formátu klíč => hodnota
    $a_pole = array('jedna' => 1, "dva" => 2, "tri" => 3, "ctyri" => 4);
    /*
    identické ke slovníku(dictionary, JSON)
    {
        "klic": "hodnota",
    }
    */
    // echo $a_pole;
    // cyklický výpis hodnot asociaticního pole
    foreach ($a_pole as $key => $value) {
        echo "Klíč ", $key, " má hodnotu ", $value;
        echo "<br>";
    }
    echo $a_pole["dva"];
    echo "<br>";

    foreach ($pole as $key => $value) {
        echo "Klíč ", $key, " má hodnotu ", $value;
        echo "<br>";
    }
    echo "<br>";

    // mix indexovaného a asociativního pole
    // pokud poskytneme klíč použije náš, pokud ne použije index 
    $mix_pole = array(1, 2, "klic_1" => 3, "klic_2" => 4, 5, 6);
    foreach ($mix_pole as $key => $value) {
        echo "Klíč ", $key, " má hodnotu ", $value;
        echo "<br>";
    }
    ?>
</body>
</html>