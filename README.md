# Задача о 100 узниках и 100 ящиках

В тюрьме находятся 100 узников, приговоренных к казни. Начальник тюрьмы предлагает им последний шанс избежать наказание
Узники пронумерованы от 1 до 100, а в отдельной комнате стоит шкаф со 100 ящиками. В каждый ящик случайным образом кладут по одному номеру от 1 до 100. Т.е. в каждом ящике свой уникальный номер.
Узники по одному входят в комнату с ящиками и каждый может открыть и проверить любой ящик но не более половины ящиков.
После каждого узника ящики остаются в прежнем состоянии.
Если каждый из узников найдёт в одном из 50 ящиков свой номер, то все узники будут помилованы, если хотя бы один узник не найдёт свой номер, все узники будут казнены.
Прежде чем первый узник войдёт в комнату, узники могут обсудить стратегию, но не могут общаться во время игры.


## Стратегия и шансы

Если выбирать ящики случайным образом, тогда шанс, что абсолютно всем повезет примерно равен 0,0000000000000000000000000000008

Но есть стратегия которая может улучшить шансы до 30% и даже выше!

Стратегия: Сначала открывает ящик со своим номером. Если в нем другой номер, тогда открывает ящик с номером который он только что вытащил, и так далее...

Проверим это!
Возьмем 100 тюрем по 100 узников в каждой. И смоделируем эту стратегию

