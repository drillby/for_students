<?php
    function zobrazProdukt($nazev, $cena, $mnozstvi, $popis, $obrazek)
    {
        ?>
        <div class="produkt-page">
            <table>
                <tr>
                    <td>
                        <img src="<?php echo $obrazek ?>" alt="">
                    </td>
                    <td>
                        <div class="produkt-texty">
                            <h1><?php echo $nazev ?></h1>
                            <h3 class="cena"><?php echo $cena ?></h3>
                            <h3><?php echo $mnozstvi ?></h3>
                            <button>Přidat do košíku</button>
                        </div>
                    </td>
                </tr>
            </table>
        <p><?php echo $popis ?></p>
    </div>
        <?php
    }
?>