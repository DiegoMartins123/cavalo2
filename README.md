##Atividade realizada na aula dia 29-05 criando a implementação do Passeio do Cavalo com backtracking

Esta implementação do Passeio do Cavalo utiliza a técnica de tentativa e erro, também conhecida como backtracking, para encontrar um caminho em que o cavalo percorra todas as casas do tabuleiro exatamente uma vez. O tabuleiro é representado por uma matriz de tamanho *n x n*, onde cada posição recebe um número indicando a ordem em que foi visitada.

O cavalo se move conforme as regras do xadrez, com oito possibilidades de movimento em "L". A função tenta movimentar o cavalo a partir de uma posição inicial e, caso encontre um caminho válido, imprime a solução com a sequência de movimentos; caso contrário, informa que não há solução.

Inicialmente, o código é testado com tabuleiros pequenos, como *5x5*, e depois pode ser usado em tamanhos maiores, como *6x6* ou *8x8*, embora a complexidade aumente significativamente.
