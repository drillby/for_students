CREATE TABLE Produkt (
    nazev char(40) PRIMARY key,
    cena float,
    mnozstvi int,
    popis text,
    obrazek text
);

INSERT INTO Produkt (nazev, cena, mnozstvi, popis, obrazek)
VALUES
(
    "Bezdrátová sluchátka",
    799.0, 5,
    "Designová sluchátka s pohodlnými polstrovanými náušníky",
    "https://xeon.spskladno.cz/~podrazky/eshop_es4/imgs/bezdratova_sluchatka.webp"
)