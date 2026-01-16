# MAGI_Project 
MAGI like artifitial neural network 

## Requirements 
python 3.13.5 
numpy 
matplotlib 

## TODO List 
- [X] Forward propogaition 
- [ ] Backward propogation 
- [ ] Weights update 
- [X] Input/Output System 
- [X] File saving system 
- [X] File loading system 
- [ ] API for AI talking with each other 
- [ ] __UI__ 
- [X] Lineart 
- [ ] Technical art
- [ ] Visual interface 
- [ ] finish todo list 

## Thery
В ходе исследования я выяснил что присутствие нескольки параметров на входе не имеет значения в виду вида раскрытия формулы в вид системы:
$
(x_1 + x_2 + ... + x_n) * \sum\limits_1^a w_{1.a} * \sum\limits_1^b w_{2.b} * ... \sum\limits_1^c w_{layersCount-1.c} + w_{layersCount.1}\\
(x_1 + x_2 + ... + x_n) * \sum\limits_1^a w_{1.a} * \sum\limits_1^b w_{2.b} * ... \sum\limits_1^c w_{layersCount-1.c} + w_{layersCount.2}\\
...\\
(x_1 + x_2 + ... + x_n) * \sum\limits_1^a w_{1.a} * \sum\limits_1^b w_{2.b} * ... \sum\limits_1^c w_{layersCount-1.c} + w_{layersCount.d}
$
с условием отсутствия прямого сложения весов из-за присутствия функции активации ограничивающей возможные сдвиги значений. Это приводит к выводу что входной слой суммируеться и количество параметров на нём не играет роли

_Из разряда шизо теорий, из-за особенностей строения этого типа нейроных сетей(один вход много выходов, как и у реальных нейронов человеческого мозга) их можно использовать как наборы отдельных типов нейронов. Правда могут быть проблемы с оучаемостью и вообще мои слова всерёз воспринимать нельзя_

## Sorces
https://proceedings.neurips.cc/paper/2015/file/3e15cc11f979ed25912dff5b0669f2cd-Paper.pdf
https://arxiv.org/pdf/2004.03333
https://arxiv.org/pdf/1308.3432
https://arxiv.org/pdf/2110.06804
https://www.computeroptics.ru/KO/PDF/KO48-4/480412.pdf

### Write/Read file explain 
4 states of BinInt (00[0], 01[1], 10[-0], 11[-1])
"-0" - is usless, then I will use it for cut the layers in neural network.

_fill char_
    write BinInt's vlues until char value is fill (8 bits => 4 BinInt valus)
    if reach the end of layer write "10" or "-0"(in my interpritation) value and continue filling
    if finished filling values shift all bits to the left edge of char

_write in file_
    just save list of char values in file "file_name.AI"

_read from file_
    create list of char values from file
    start filling layer by reading high 2 bits of first char and write them in layer
    if "10" cut and start new layer
    erase/ignore last layer

### API explain 

