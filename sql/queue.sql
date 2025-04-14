DROP TABLE vlastnictvo IF EXISTS;
CREATE TABLE vlastnictvo (
    username TEXT PRIMARY KEY,
    den INTEGER DEFAULT 0,
    Krysodlacia INTEGER DEFAULT 0,
    Moc INTEGER DEFAULT 0,
    Obria INTEGER DEFAULT 0,
    Jed INTEGER DEFAULT 0,
    Slzy INTEGER DEFAULT 0,
    Krv INTEGER DEFAULT 0,
    Plesen INTEGER DEFAULT 0,
    Sliz INTEGER DEFAULT 0,
    Sliny INTEGER DEFAULT 0,
    Koza INTEGER DEFAULT 0,
    Bulvy INTEGER DEFAULT 0,
    Krystal INTEGER DEFAULT 0,
    Ligusticum INTEGER DEFAULT 0,
    Mixtura INTEGER DEFAULT 0,
    Nigrumteum INTEGER DEFAULT 0,
    Piesok INTEGER DEFAULT 0,
    Roh INTEGER DEFAULT 0,
    Turmericum INTEGER DEFAULT 0,
    Zlazy INTEGER DEFAULT 0,
    Zobak INTEGER DEFAULT 0,
    NamiesaneElixiry 
);
CREATE TABLE elixiry (
    den INTEGER,
    elixir TEXT,
    priznaky TEXT
);

INSERT INTO elixiry
VALUES 
    (1, 'Nadeje', 'Prdenie Zrenice Ze vyrazka'),
    (2, 'Sily', 'Kychanie Triaska Trpnutie'),
    (3, 'Mudrosti', 'Trpnutie M koza Ze vyrazka'),
    (3, 'Nehy', 'Triaska Trpnutie M koza'),
    (4, 'Strachu', 'Kychanie Kaslanie Chlpy dup'),
    (4, 'Lasky', 'Triaska Ce nechty Prdenie'),
    (5, 'Bojovnosti', 'Triaska M koza Ze vyrazka'), 
    (5, 'Odvahy', 'Ce nechty Zrenice Ze vyrazka'),
    (6, 'Ohavnosti', 'Ce nechty Prdenie Ze vyrazka'), 
    (6, 'Smrti', 'Kaslanie Triaska Ce nechty'),
    (7, 'Zivota', 'Kychanie Triaska M koza'), 
    (7, 'Krasy', 'Trpnutie Prdenie Zrenice'),
    (8, 'Poznania', 'Kychanie Kaslanie Triaska'), 
    (8, 'Mladosti', 'Kychanie Trpnutie Zrenice'),
    (9, 'Stastia', 'Triaska Prdenie Zrenice'), 
    (9, 'Pomatenosti', 'Kychanie Kaslanie Ce nechty'),
    (10, 'Lenivosti', 'Kychanie Triaska Zrenice'), 
    (10, 'Radosti', 'Trpnutie Ce nechty Ze vyrazka'),
    (11, 'Rychlosti', 'Kychanie Chlpy dup Ze vyrazka'),
    (11, 'Spanku', 'Triaska Prdenie M koza');


CREATE TABLE namiesaneElixiry (
    username TEXT PRIMARY KEY,
    Nadeje BIT DEFAULT 0,
    Sily BIT DEFAULT 0,
    Mudrosti BIT DEFAULT 0,
    Nehy BIT DEFAULT 0,
    Strachu BIT DEFAULT 0,
    Lasky BIT DEFAULT 0,
    Bojovnosti BIT DEFAULT 0,
    Odvahy BIT DEFAULT 0,
    Ohavnosti BIT DEFAULT 0,
    Smrti BIT DEFAULT 0,
    Zivota BIT DEFAULT 0,
    Krasy BIT DEFAULT 0,
    Poznania BIT DEFAULT 0,
    Mladosti BIT DEFAULT 0,
    Stastia BIT DEFAULT 0,
    Pomatenosti BIT DEFAULT 0,
    Lenivosti BIT DEFAULT 0,
    Radosti BIT DEFAULT 0,
    Rychlosti BIT DEFAULT 0,
    Spanku BIT DEFAULT 0
)
    

    rozvrhElixiry = [
    "Nádeje",
    "Sily",
    "Mudrosti, Nehy",
    "Strachu, Lasky"    ,
    "Bojovnosti, Odvahy",
    "Ohavnosti, Smrti",
    "Života, Krásy",
    "Poznania, Mladosti",
    "Štastia, Pomatenosti",
    "Lenivosti, Radosti",
    "Rýchlosti, Spánku",
]
