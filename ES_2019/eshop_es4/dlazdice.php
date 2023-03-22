<?php
function zobrazDlazdici($nazev, $cena, $obrazek, $mnozstvi) {
    ?>
    <div class="card">
        <img src="<?php echo $obrazek ?>" style="width:100%">
        <h1><?php echo $nazev ?></h1>
        <p class="price"><?php echo $cena ?> Kč</p>
        <p><?php echo $mnozstvi ?> ks</p>
        <p><button>Přidat do košíku</button></p>
    </div>
    <?php
}
?>