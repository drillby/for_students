<?php
function zobrazDlazdici($nazev, $cena, $obrazek, $mnozstvi) {
    ?>
    <div class="dlazdice">
        <img class="dlazdice-img" src="<?php echo $obrazek ?>"alt="">
        <div class="nazev-cena-wrapper">
            <h3 class="dlazdice-nazev"><?php echo $nazev ?></h3>
            <h4 class="dlazdice-cena"><?php echo $cena ?> Kč</h4>
        </div>
    </div>
    <?php
}
?>

