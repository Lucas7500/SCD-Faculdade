Considere que existe um recurso compartilhado (um ArrayList) que irá conter uma relação de números e será alimentado por diversas threads.

Crie uma classe chamada Aula, que possa ser utilizada para instanciar objetos do tipo Thread, que irão receber uma uma lista (List ou ArrayList) como argumento do construtor.  Além da lista, deverá receber dois parâmetros: número inicial e quantidade de números

No método Run, escreva código para adicionar os números à lista (começando do número inicial e incrementando de 1 em 1 até chegar à quantidade).

No programa principal crie uma lista e, no mínimo, três threads da classe Aula. Execute as três threads e, após a conclusão das três, mostre os elementos da lista. Há alguma incoerência, porquê?

Responda a pergunta no campo de texto desta tarefa.

Minha Resposta: Há sim incoerência em algumas das vezes que se executa o código. Por se tratar de threads, a natureza da operação é concorrente e a ordem da execução dessas threads não se é garantida, fazendo com que a ordem dos números dentro da lista seja arbitrário, mas isso não é tudo. Além disso, a classe ArrayList é uma classe que não é thread-safe, isto é, ela não possui as tratativas que seriam necessárias num contexto multi-thread e isso resulta em situações de inconsistência dos dados, em que a mesma instância de ArrayList é modificada por mais de uma thread ao mesmo tempo e, por fim, uma thread acaba sobrescrevendo a operação da outra.