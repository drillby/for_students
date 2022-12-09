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
    // for cyklus 
    for ($i=0; $i <= 10; $i++) {
        ?>
        <h1><?php echo $i ?></h1>
        <?php
    }
    ?>
<br>
    <?php
    // while cyklus
    $a = 0;
    while ($a <= 10) {
        ?>
        <h1><?php echo $a ?></h1>
        <?php
        $a++; // ! nezapomenout na zvetnutí iterační proměnné
    }
    ?>
    <br>
    <?php
    // for cyklus s break příkazem
    for($i=0; $i<=10; $i++) {
        // pokud i==6, cyklus končí
        if($i == 6){
            break;
        }
        echo $i;
    }
    ?>
    <br>
    <?php
    // for cyklus s continue příkazem
    for($i=0; $i<=10; $i++) {
        // pokud i==6, vypíše se "šest"
        if($i == 6){
            echo "šest";
            continue; // continue přeskočí zbytek cyklu a začne novou iteraci
        }
        echo $i;
    }
    ?>
    <br>
    <?php
    $i=0;
    // while cyklus s break 
    while($i<=10) {
        if($i == 6){
            break;
        }
        echo $i;
        $i++;
    }
    ?>
    <br>
    <?php
    $i=0; 
    // while cyklus s continue
    while($i<=10) {
        if($i == 6){
            echo "šest";
            $i++; // ! nutné zvednout hodnotu iterační porměnné, jinak se bude i==6 navždy
            continue;
        }
        echo $i;
        $i++;
    }
    ?>
    <br>
    <!-- generace tabulky pomocí php -->
    <table>
    <?php
    // cyklicky vytvoříme řádek
    for($radek=0; $radek <= 5; $radek++){
        ?>
        <!-- tvorba řádku -->
        <tr>
            <?php
            // cyklicky vytvoříme sloupce
            for($sloupec=0; $sloupec <= 5; $sloupec++){
                ?>
                <!-- tvorba sloupce tagem td -->
                <td style="color: green;"><?php echo $radek, ":", $sloupec ?></td>
                <?php
            }
            ?>
        </tr>
        <?php
    }
    ?>
    </table>
    <br>
    <?php
    $variable = ["text", "text_2", "text_3"];
    // foreach cyklus, samotnou hodnotu v poli si hlídá cyklus sám
    foreach ($variable as $key => $value) {
        echo $value, " ";
    }
    echo "<br>";
    // narozdíl od for cyklu, kde k hodnotě musíme přistupovat přes index
    for($i=0;$i < count($variable); $i++) {
        echo $variable[$i], " ";
    }
    ?>
</body>
</html>