from typing import Generator

def eratosthenovo_sito(max: int) -> Generator[int, int, None]:
    max += 1
    sito = [True] * max

    for i in range(2, max):
        if sito[i]:
            for j in range(i**2, max, i):
                sito[j]=False
    
    for i in range(2, max):
        if sito[i]:
            yield i