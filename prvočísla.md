---
lang: cs
header-includes: |
    \widowpenalties 2 1000 0
    \raggedbottom
---

<!--
TODO
- [ ] VÍCE CITACÍ
- [o] rozšířit paragrafy o historii
    - [o] úvod do historie
    - [ ] přepsat začátek řecka na nový úvod
    - [o] možná citace pro mersenne
- [o] Algoritmy
    - [ ] úvod
    - [ ] přepsat příklad u naivního algoritmu
    - [ ] dopsat RSA algoritmus

- [ ] TODO!!! Read and rewrite like everything
-->

# Úvod
2, 3, 5, 7, každý z nás zná tuto sekvenci čísel jako prvočísla, avšak ne
všichni si uvědomují implikace nedělitelného čísla. Hlavní obor který tento
fakt ovlivňuje je matematika, ale hned další je informatika, přesněji moderní
kryptografie, jejíž nálezy chrání naše osobní informace, by neexistovala bez
velkých prvočísel.

První téma které tato seminární práce ukáže, je definice prvočísel, a jak se v
minulosti měnila, a také jak je spojená s historií "čísla" 1.

Další téma, které ukáže, je jak vygenerovat seznam
prvočísel, od naivního způsobu, až po nejrychlejší způsob.

Projde také způsoby, jak faktorizovat čísla, od jednoduché metody dělení, až po
teoretický kvantový algoritmus.

Též projde důležitý RSA algoritmus, dlouhou dobu používán jako hlavní
kryptografický algoritmus pro https protokol, způsob, jakým generuje klíče, a
také jeho využití.

Všechny algoritmy byly implementovány v Pythonu

# Definice
Dřív než ale budeme pokračovat, musíme vědět co prvočíslo je.

Podle Online Encyklopedie Integrových sekvencí (OEIS) je prvočíslo definováno
takto:
Číslo p je prvočíslo jen tehdy, když je větší než 1 a nemá žádné kladné
dělitele kromě 1 a p. [^7]

Tato definice nebyla v minulosti tolik používána, a fakt jestli by se měla
jednička, také známá jako jednotka, počítat, byl v historii velmi sporný.

## Historie
V minulosti ale nebyla tato definice tak používána. Byla i velmi spojena s
názorem jestli je 1 vůbec číslo. [^1]

### Číslo 1
#### starověké Řecko
V antickém Řecku byly pochyby zda 1 je vůbec číslo, často známé spíš jako
"jednotka", Euklidés, dnes známý jako otec moderní geometrie, definoval číslo
jako množství jednotek, a jednotku "to podle čehož vše existující je jedna";
takže $N = k * 1; k > 1$. [^2]
Podle některých z této doby nebylo ani číslo 2 prvočíslo, ale řada prvočísel
začínala již číslem 3, také známá jako lichá prvočísla. Pouze vzácně byla 1
prvočíslo, například Speusippus považoval 1 za první prvočíslo, dnes známá
jako, nedělitelná čísla tento názor byl však velmi vzácný. Po mnoho let zůstala
jednička pouze jednotkou, a čísla, včetně prvočísel, začínala 2

#### Novověk
##### De Thiende
Středověk je rozdělen na 2 části, před Simonem Stevinem, a po.
Ve své knize "De Thiende" (Desetina) v roce 1585 mimo jiné definoval čísla jako
"jednotka nebo složený násobek jednotek". Desetina také obsahovala první systém
pro psaní desetinných čísel. [^3]

##### Moxon
Tento názor se neusadil hned, i o 100 let později, v prvním matematickém
slovníku, u definice Čísla píše Josef Moxon že obecně akceptována definice
vylučuje 1, Josef ale píše že to se mu nezdá správné: pokud 1 není číslo, pak
$3 - 1$ je pořád 3, což samozřejmě není pravda.
Ve stejném slovníku definuje prvočísla stejným způsobem jako Euklidés, jako to,
co měří pouze jednotka: 2, 3, 5, 7... [^4]

Ale nyní se historie prvního čísla a prvočísel spojí. S prvním matematickým
slovníkem si nebyli někteří matematici jistí co dělat s informací že 1 je
opravdu číslo, někteří ji začali přiřazovat mezi prvočísla, vždyť ji nic
nedělí.

Goldbach, znám pro jeho hypotézu, že každé sudé číslo je součet dvou prvočísel,
považoval 1 za prvočíslo. V korespondenci s Eulerem, kde popisoval svou
hypotézu o součtech prvočísel, použil 1 jako prvočíslo. [^5]

![Část dopisu mezi Goldbachem a Eulerem, kde Goldbach ukazuje příklady své
hypotézy](./pictures/goldbach.png)

Oproti tomu francouzský mnich Marin Mersenne, znám pro Mersennova prvočísla ji
nezapočítal do svého originálního seznamu.

### Základní věta aritmetiky
Dnes již známá informace, že každé přirozené číslo větší než 1 se dá rozložit
na součin prvočísel, nebyla ve středověku příliš prozkoumána. Až matematik Carl
Friedrich Gauss, ve své knize "Disquisitiones Arithmeticae" (Aritmetická
Diskuze) popsal tuto větu, a dodal i částečný důkaz. [^6]

### Moderní historie
V dnešní době jednička není prvočíslo, ale na přelomu 19. a 20. století to
nebylo tak jasné: OEIS sekvence A008578 označuje "prvočísla na začátku 20.
století", včetně 1. [^8]
V Encyclopaedia Britannica, 9. edice, profesor Arthur Cayley definoval
prvočíslo jako to co není produktem násobku. Současně dá jako příklad prvních 5
prvočísel podle moderní definice. Později ale nazve číslo 1 prvočíslem.
V 11. edici, vydané o 20 let později, jsou ale prvočísla definována pomocí
moderní definice.

I přes to, že 1 nebyla vždy považována většinou matematiků jako prvočíslo, byla
určitá část přesvědčena že je prvočíslo. Dnes je tato sekvence známa jako
nesložená čísla.

# Algoritmy
## Vypočítání prvočísel
V minulosti byla prvočísla zjišťována ručně, kdy po dlouhých večerech počítali
matematici dělitele, nebo pomocí speciálních algoritmů pro kontrolu zda je
číslo prvočíslo (o nich později)

### Naivní způsob
První způsob jak je vypočítat, takzvaný "naivní" algoritmus, by bylo pro každé
číslo zkusit jej postupně vydělit s každým známým prvočíslem. Pokud ho
žádné nedělí, pak je to prvočíslo. Pokud ale ano, pak nezkoušíme dělitelnost s
žádným dalším prvočíslem, ale rovnou se přesuneme k dalšímu číslu v řadě.

Například, pokud už známe prvočísla 2, 3 a 5, a teď kontrolujeme 7, pak budeme
postupovat takto:
Zkusíme dělitelnost 2. Není dělitelné, a tak pokračujeme dál.
Kontrolujeme pak dělitelnost 3, také není, stejně jako 5.
Zkontrolovali jsme všechna teď známá prvočísla, a protože 7 není dělitelná
žádným z nich, přidáme ji do seznamu nám známých prvočísel.

Nyní máme prvočísla 2, 3, 5 a 7, a kontrolujeme číslo 8:
Zkusíme dělitelnost 2
dělí, protože 2 * 4 = 8, a tak hned přestáváme a pokračujeme dál k 9.

Tento způsob je sice velmi jednoduchý pro malá prvočísla a pochopitelný
pro člověka, ale bohužel velmi neefektivní pro větší čísla, kdy počet kroků pro
kontrolu každého čísla roste exponenciálně, a je tím pádem nejpomalejší ze
všech zmíněných algoritmů.

způsob jak tento algoritmus implementovat:
```py
def checking(n: int) -> list[int]:      # definice funkce, vstup je n, neboli
                                        # maximální číslo které zkontrolovat
    primes = [2]                        # seznam prvočísel udržován
    for i in range(3, n, 2):            # začne odpočítávat od 3 do n, po 2
        for prime in primes:            # pro každé známé prvočíslo
            if i % prime == 0:          # pokud je prvočíslo dělitelem,
                                        # skončíme
                break
        else:
            primes.append(i)            # jinak přidá nově nalezené prvočíslo
                                        # do seznamu
    return primes
```


#### Eratosthenovo síto
Druhý způsob, jak je vypočítat, údajně známý již od 3. století před Kristem, je
Eratosthenovo síto. Je efektivnější než naivní algoritmus, protože místo toho
aby kontrolovalo dělitele pro každé číslo jednotlivě, rovnou odebere všechny
násobky nově zjištěného prvočísla.

Začneme se seznamem čísel od 2 do určitého limitu.
První číslo je prvočíslo, a tak ho vyjmeme ze seznamu.
Vyjmeme také všechny jeho násobky.
Tyto 2 kroky opakujeme dokud jsme nevyčerpali celý seznam.

Například začneme se seznamem od 2 do 10.
2 3 4 5 6 7 8 9 10

2 je prvočíslo, a tak vyjmeme všechny jeho násobky
3 5 7 9

3 je prvočíslo, a tak vyjmeme všechny jeho násobky
5 7

Přeskočíme 2 kroky, protože 5 a 7 nejsou násobky sebe sama a tím pádem jsou
prvočísla.

Konečný seznam všech prvočísel menších než 10 je 2 3 5 7

Implementace:
```py
def sieve_eratosthenes(n: int) -> list[int]:
    nums = [True] * n                           # vytvoří seznam, každý element
                                                # reprezentuje zda je jeho
                                                # korespondující číslo prvočíslo
    primes = []
    for i in range(2, n):                       # prochází každým číslem v
                                                # seznamu
        if nums[i]:                             # pokud je zrovna kontrolované
                                                # číslo prvočíslo:
            primes.append(i)                    # nalezli jsme prvočíslo,
                                                # přídáme ho do seznamu
            for j in range(i**2, n, i):         # všechny násobky označit jako
                                                # složené číslo
                nums[j] = False
    return primes
```

#### Sundaramovo síto
V roce 1934 objevil indický student S. P. Sundaram nový způsob jak
vypočítat prvočísla. Závisí na lichosti valné většiny prvočísel, a že se dají
zapsat tvarem $2k + 1; k \in N$.
Začíná podobně jako Eratosthenovo síto, začne se se seznamem všech čísel od 1
do n. Poté se vyjmou všechna čísla tvaru $i + j + 2ij$ kde $i \in N \land j
\in Z \land i >= j$.
Tímto nám vyšly všechny hodnoty k, stačí pouze vložit do výše popsané rovnice a
vyjdou nám všechna prvočísla

Důkaz že všechny vyjmuté hodnoty opravdu jsou kompozitní je tento:
pokud $q$ je liché přirozené číslo tvaru $2k + 1$, pak je vyjmuto pouze když
$k = i + j + 2ij$
$q = 2(i + j + 2ij) + 1$
$q = 2i + 2j + 4ij + 1$
$q = (2i + 1)(2j + 1)$
Liché přirozené číslo je vyjmuto pouze pokud má celočíselné liché dělitele.

Implementace:
```py
def sieve_sundaram(n: int) -> list[int]:
    k = (n-1)//2                            # maximální hodnota k
    nums = [True] * k                       # stejné jako eratosthenovo síto,
                                            # každé číslo reprezentuje zda je
                                            # prvočíslo nebo ne
    for i in range(1, k):                   # projde všechny možnosti pro i + j 2ij
        j = i
        while (i + j + 2*i*j) < k:
            nums[i + j + 2*i*j] = False
            i += 1
    primes = [2]                            # vygeneruje seznam prvočísel ze
                                            # seznamu hodnot k
    for i in range(1, k):
        if nums[i]:
            primes.append(2*i+1)
    return primes
```


#### Atkinovo síto
Tento algoritmus byl stvořen matematiky Arthurem Oliverem Lonsdale Atkinem (A.O.L.
Atkin) a Danielem Juliem Bernsteinem (djb) v roce 2003. Atkinovo síto je dodnes
nejrychlejší algoritmus na bázi síta, s asymptotickou složitostí `O(n)`, a v
některých variacích `O(n/log(log n))`. Eratosthenova a Sundaramova síta mají
`O(n log(log n))` a `O(n log(n))`, v tomto pořadí.

Všechny části tohoto algoritmu byly dokázány v jejich vědecké práci "Prime
sieves using binary quadratic forms"[^9]
```py
def sieve_atkin(n: int) -> list[int]:
    nums = [False] * (n+1)
    for x in range(1, math.isqrt(n)):
        for y in range(1, math.isqrt(n)):

            # věta 6.1
            num = 4*x**2 + y**2
            if num <= n and (num % 12 == 1 or num % 12 == 5):
                nums[num] = not nums[num]

            # věta 6.2
            num = 3*x**2+y**2
            if num <= n and num % 12 == 7:
                nums[num] = not nums[num]

            # věta 6.3
            num = 3*x**2 - y**2
            if x > y and num <= n and num % 12 == 11:
                nums[num] = not nums[num]

    # odebrání druhých mocnin čísel ze seznamu prvočísel
    for x in range(5, int(math.sqrt(n))):
        if nums[x]:
            for y in range(x**2, n, x**2):
                nums[y] = False

    return [2, 3] + [prime for prime in range(5, n) if nums[prime]]
```

### Mersennova prvočísla
Toto jsou prvočísla tvaru $2^n-1$. Pokud n je kompozitní, pak je i $2^n-1$,
tudíž jsou Mersennova prvočísla často psána formou $2^p-1$, kde p je prvočíslo.
Pokud n je kompozitní, pak platí
$2^{ab}-1 = (2^a - 1) * (\sum_{n=0}^{b-1} 2^{na})$
například pro exponent 4: \break
$2^4-1 = (2^2-1)*(1+2^2)$

Toto však neznamená že všechna prvočísla vedou k Mersennovým prvočíslům, hned
11 vede ke kompozitnímu:
$2^11-1 = 2047 = 23 * 89$

Již zmíněný francouzský mnich Marin Mersenne publikoval v roce 1644 "Cogitata
Physico-Mathematica", kde vypsal seznam exponentů pro které si myslel že
$2^n-1$ je prvočíslo:
2, 3, 5, 7, 13, 17, 19, 31, 67, 127, 257
Až k 19 to byly v té době známé exponenty, 31 byla správně přidána, ale 67 a
257 nevedou k prvočíslům. Též byly vynechány 89 a 107.

Dnes jsou Mersennova prvočísla prvních 6 největších prvočísel, a to díky
Lucas-Lehmerovu testu prvočíselnosti a Great Internet Mersenne Prime Search
(GIMPS).

#### Lucas-Lehmerův test prvočíselnosti
V roce 1878, po 19 letech testování prvočíselnosti $2^127-1$, vyvinul Édouard
Lucas a v 1930 dokázal správnost Derrick Henry Lehmer tento test prvočíselnosti.

Test pro $M = 2^p-1$ probíhá takto:
Pokud $s_{p-2} \equiv 0 (mod M)$, pak je M prvočíslo
hodnoty $s_i$ se vypočítají tímto způsobem:
pokud $i = 0$: s = 4
jinak $s = s^2_i-1 - 2$

V implementacích jsou hodnoty s vypočítány modulo M, protože jinak by s zabralo
příliš velkou část paměti.

Jsou možné i alternativní počáteční hodnoty s, například 10 nebo 52 [^10]

Implementace tohoto testu, vstup je exponent p:
```py
def lucas_lehmer(p: int) -> bool:
    s = 4
    M = 2**p - 1
    for _ in range(p - 2):
        s = ((s * s) - 2) % M
    if s == 0:
        return True
    else:
        return False
```

#### GIMPS
Tento test byl dlouho používán organizací GIMPS, která využívá počítače
dobrovolníků pro zjištění nových Mersennových prvočísel. Dnes používá hlavně
Fermatův test prvočíselnosti, pro pravděpodobná prvočísla.
Ten tvrdí že pro každé prvočíslo bude platit $a^{p-1} \equiv 1 (mod p)$ pro
všechny $a \nmid p$.

V roce 2018 objevili $2^{82589933}-1$, největší prvočíslo, s 24 milionů číslic.
Každý kdo má počítač může pomoci, stačí jenom stáhnout Prime95 či mprime a
nechat ho běžet na vašem počítači. [^11]

## Kryptografie
Velmi důležitý obor pro moderní existenci na internetu. Dnes používané
algoritmy používají asymetrickou kryptografii. To znamená že pro zašifrování se
použije jeden klíč, a pro dešifrování zase jiný: "public" a "private" klíče.

Asymetrická kryptografie je důležitá pro to, že pokud by se používala
symetrická, musí odesílatel a příjemce mít stejný klíč. Dostat klíč k příjemci
bez toho aby ho dostal někdo jiný je prakticky nemožné. Také známé jako
"problém dvou armád", kde se 2 armády musí domluvit na útoku na město, ale musí
svou komunikaci vést přes toto město, což ale riskuje že posel bude odhalen a
městští ozbrojenci budou vědět o útoku.

### RSA
Jeden z nejpoužívanějších asymetrických kryptografických algoritmů, pojmenován
podle jeho tvůrců - Ron Rivest, Adi Shamir a Leonard Adleman.
Funguje tak, že najde 3 přirozená čísla $n, e, d$ aby platilo pro kterékoliv
číslo $m$: $(m^e)^d \equiv m (mod n)$

`n` a `e` patří do public klíče, zatímco `d` bude private klíč.
Pro zašifrování převedeme naši zprávu do číselné formy a vypočítáme formu $m^e
mod n$
Pro dešifrování stačí pouze vypočítat $(m^e mod n)^d mod n$

Alternativní využití by bylo pro potvrzení pravosti elektronických zpráv:
Pokud vyměníme funkce klíčů, a zašifrujeme naši zprávu pomocí našeho private
klíče, pak kdokoli může využít náš public klíč, dešifrovat naši zprávu, a
zkontrolovat validitu dešifrované zprávy.

#### Vygenerování klíčů
$n, e a d$ se vypočítají pomocí 2 náhodných velkých prvočísel, `p` a `q`.
$n = p * q$
$\lambda(n) = nejmenší společný násobek p-1 a q-1$
vybrat `e`, tak aby $1 < e < \lambda(n)$ a zároveň $e$ a $\lambda(n)$ jsou
nesoudělná čísla (mají pouze jednoho společného dělitele - 1)
vypočítat `d` aby $d * e \equiv 1 (mod \lambda(n))$
To se může zjednodušit na
$d * e = k * \lambda(n) + 1; k \in Z$
$d * e - k * \lambda(n) = 1$, Bézoutova rovnost
`d` můžeme vypočítat pomocí rozšířeného Euklidova algoritmu pro $a = e; b =
\lambda(n)$, to celé modulo $(p-1)(q-1)$
Ten, jak jméno naznačuje, rozšiřuje Euklidův algoritmus pro nalezení největšího
společného dělitele.
Zde použitý je napsán rekursivním způsobem:
$gcd_0 = a$
$gcd_1 = b$
$d_0 = 1$
$d_1 = 0$
$k_0 = 0$
$k_1 = 1$
...
$r_{i+1} = r_{i-1} - q_ir_i$
$s_{i+1} = s_{i-1} - q_is_i$
$t_{i+1} = t_{i-1} - q_it_i$

Implementace:
```py
def extended_euclid(a: int, b: int) -> tuple[int, int, int]:
    # největší společný dělitel nalezen
    if b == 0:
        return a, 1, 0
    gcd, new_k, new_d = extended_euclid(b, a % b)
    d = new_d
    k = new_k - (a // b) * new_d
    return gcd, d, k


def generate_rsa_keys(p: int, q: int) -> tuple[int, int, int]:
    n = p*q
    phi = math.lcm(p-1, q-1)
    e = 0
    for i in range(2, phi):
        if math.gcd(phi, i) == 1:
            e = i
            break
    d = extended_euclid(e, phi)[1] % ((p-1)*(q-1))
    return n, e, d
```

#### Důkaz
Důkaz, že $(m^e)^d = m (mod pq)$ pro všechny hodnoty m, pokud p a q jsou různá
prvočísla a e, d splňují podmínku $ed \equiv 1 (mod \lambda(pq))$ závisí na
Fermatovu testu prvočíselnosti, pospaném výše.

Protože $\lambda(pq) = nejmenší\:společný\:násobek(p-1, q-1)$, a dělitelné
$p-1$ a $q-1$, můžeme napsat že $ed - 1 = h(p - 1) = k(q - 1)$ pro přirozená
čísla `h` a `k`.

Pro kontrolu zda $m^{ed} \equiv m (mod pq)$, stačí zkontrolovat zda jsou
ekvivalentní pro $mod p$ a $mod q$ samostatně

Pro $m^{ed} \equiv m (mod p)$:
1. Pokud $m \equiv 0 (mod p)$, m je násobek p, takže $m^{ed}$ je násobek $p$. Tím
    pádem $m^{ed} \equiv 0 \equiv m (mod p)$
2. Pokud $m \nequiv 0 (mod p)$:
    $m^{ed} = m^{ed-1}m = m^{h(p-1)}m = (m^{p-1})^hm \equiv 1^hm \equiv m (mod
    p)$ kde jsme použili Fermatův teorém abychom nahradili $m^{p-1} (mod p)$ s
    1.

Důkaz, že $m^{ed} \equiv m (mod q)$ je velmi podobný:
1. Pokud $m \equiv 0 (mod q)$, $m^{ed}$ je násobek q. Takže $m^{ed} \equiv 0
   \equiv m (mod q)$.
2. Pokud $m \nequiv 0 (mod q)$,
    $m^{ed} = m^{ed-1}m = m^{k(q-1)}m = (m^{q-1})km \equiv 1^km \equiv m (mod
    q)$.

Tudíž, pro kterékoliv celé číslo `m`, a pro taková celá čísla `e`, `d`, že $ed
\equiv 1 (mod \lambda(pq))$ platí
$$(m^e)^d \equiv m (mod pq)$$

## Algoritmy faktorizace
Opak vygenerování prvočísel je faktorizace čísel. I když nemá tolik využití, je
pořád užitečná pro nalezení odmocnin, největšího společného dělitele a
nejmenšího společného násobku.
U větších čísel, a hlavně u poloprvočísel - číslo které je součinem právě 2
prvočísel - jsou ale moderní algoritmy příliš pomalé na to aby byly
použitelné. Tohoto faktu využívá RSA a všechny podobné kryptografické
algoritmy.

### Naivní způsob
První a velmi jednoduchý způsob by bylo postupně dělit dané číslo dokud nevyjde
1, a zjistit faktory ze seznamu dělitelů. Jelikož faktory mohou být jenom
prvočísla, první optimalizace je dělit pouze prvočísly. A protože nemohou být
více než jeden dělitel větší než $\sqrt(n)$ stačí jenom zkontrolovat všechna
menší prvočísla.
Implementace tohoto způsobu, využijeme Atkinovo síto pro vygenerování všech
prvočísel na začátku.
```py
def naive_factorize(n: int) -> list[int]:
    primes = sieve_atkin(int(math.sqrt(n)+1))
    factors = []
    while n != 1:
        # pokud nejsou menší prvočísla, pak musí být n prvočíslo
        if not primes:
            factors.append(n)
            break

        # pokud nejmenší prvočíslo dělí n, přidáme ho do seznamu faktorů a
        # vydělíme n
        if n % primes[0] == 0:
            factors.append(primes[0])
            n //= primes[0]

        # jinak ho ignorujeme
        else:
            primes.pop(0)
    return factors
```

Hlavní nevýhoda tohoto způsobu je že je potřeba vědět všechna potřebná
prvočísla hned na začátku. Další je že ne všechna vygenerovaná prvočísla jsou
potřeba, například u mocnin 2 je vygenerována spousta prvočísel i když by
stačila samotná 2.

Vyřešit tento problém by šlo tím, že nové prvočíslo vygenerujeme jen když ho
budeme potřebovat.
Takto upravený algoritmus by mohl být implementován takto:
```py
def naive_factorize_2(n: int) -> list[int]:
    primes = [2]
    factors = []
    square_root = int(math.sqrt(n))+1
    while n != 1:
        # ekvivalent vygenerování pouze prvočísel menších než √n
        if primes[-1] >= square_root:
            factors.append(n)
            break

        # pokud nejnověji vygenerované prvočíslo dělí n, přidáme ho do seznamu
        # faktorů a vydělíme n
        if n % primes[-1] == 0:
            factors.append(primes[-1])
            n //= primes[-1]

        # jinak vygenerujeme nové prvočíslo
        else:
            # začneme s i o jedno větší než největší prvočíslo
            i = primes[-1]+1
            # poté aplikujeme stejný proces u naivního způsobu při generování
            # prvočísel
            while True:
                for prime in primes:
                    if i % prime == 0:
                        break
                else:
                    primes.append(i)
                    break
                i += 1
    return factors
```
Další způsob jak tento algoritmus optimalizovat by bylo ignorovat všechna sudá
čísla když hledáme nové prvočíslo, ale cíl této práce není ukázat optimalizace.

### Fermatova metoda faktorizace
Všechna lichá kompozitní čísla jdou zapsat jako rozdíl dvou druhých mocnin:
$n = p * q = a^2 - b^2$
$n = (a+b)(a-b)$
Jelikož nejmenší faktor je vždy 1, pak $a-b = 1$ => $a = b+1$ => $n = 2a+1$ =>
$a = \frac{n-1}{2}$

Tudíž
$n = (\frac{p+q}{2})^2 - (\frac{p-q}{2})^2$
Fermatova metoda spočívá v tom, že se pokusíme uhodnout hodnotu `a`, a pak
zkontrolovat zda $\sqrt{a^2 - n}$ je celé číslo: pokud je, našli jsme faktory:
$a - b$ a $a + b$
```py
def fermat(n: int) -> list[int]:
    # první tip na hodnotu a
    a = math.ceil(math.sqrt(n))

    # zkontrolujeme zda a*a-n je druhá mocnina
    b2 = a*a - n
    b = int(math.sqrt(b2))
    while b*b != b2:

        # aktualizujeme hodnotu a, a zkoušíme znova
        a += 1
        b2 = a*a - n
        b = int(math.sqrt(b2))

    return [a-b, a+b]
```
Tento algoritmus faktorizace může být velmi rychlý, za podmínky že rozdíl mezi
`p` a `q` není příliš velký.

### Pollardova $p-1$ metoda
Je velká šance, že minimálně jeden faktor $d^k$ který dělí $p-1$ je maximálně B
(B-hladká čísla). V roce 1974 nalezl matematik John Pollard metodu pro nalezení
takových faktorů.

Závisí na Fermatovu teorému, také znám jako Fermatův test prvočíselnosti.
$a^{p-1} = 1 (mod p)$ pokud jsou `a` a `p` vzájemně nesoudělná.
To také znamená že $a^{(p-1)^{k}} \equiv a^{k(p-1)} \equiv 1 (mod p)$

Takže pro každé M s $p-1 \mid M$ víme že $a^M \equiv 1$. To znamená že $a^M - 1
= p * r$, a kvůli tomu $p \mid nsd(a^M - 1, n)$.

Takže, pokud $p-1$ pro faktor $p$ z $n$ dělí $M$, můžeme zjistit faktor pomocí
Euklidova algoritmu.

Je jasné, že to nejmenší $M$ které je násobek každého B-hladkého čísla je
nejmenší společný násobek všech čísel od 1 do B.

Pokud $p-1 \mid M$ pro všechny prvočíselné faktory $p$ z $n$, pak $nsd(a^M - 1,
n) = n$, v tomto případě jsme nezjistili faktor, a tak se pokusíme vypočítat
společný dělitel několikrát, zatímco spočítáme $M$

Některá kompozitní čísla ale nemají B-hladká čísla pro malá B, například
$150391373107279 = 1002583 * 150003913$, obě prvočísla.

Implementace, se začátečním $B=10$:
```py
def pollard_p_minus_1(n: int) -> list[int]:
    B = 10
    g = 1
    primes = sieve_atkin(n)
    while B <= 1000000 and g < n:
        a = 2 + random.randint(0, n-3)
        g = math.gcd(a, n)
        if g > 1:
            return [g, n//g]

        # výpočet a^M
        for p in primes:
            if p >= B:
                continue

            p_power = 1
            while p_power * p <= B:
                p_power *= p
            a = int(math.pow(a, p_power)) ** n

            g = math.gcd(a-1, n)
            if (g > 1 and g < n):
                return [g, n//g]
        B *= 2
    return []
```
Bohužel tento algoritmus závisí na pravděpodobnosti, a tak je šance že nenajde
ani jeden faktor.

### Pollardův Rho algoritmus
Další algoritmus pro faktorizaci, nalezen znovu Johnem Pollardem.

Nechť prvočíselná faktorizace čísla $n$ je $n = p * q$
Tento algoritmus využívá pseudo-náhodné sekvence 
${x_i} = {x_0, f(x_0), f(f(x_0)), ...}$, kde $f$ je polynomiální funkce,
většinou $f(x) = (x^2 + c) mod n)$, kde $c = 1$

Tato sekvence nám nic neříká, ale využijeme ji pro sekvenci ${x_i mod p}$,
jelikož $f$ je polynomiální funkce, a všechny hodnoty budou menší než $p$, v
určitém bodě se začne cyklit. Pravděpodobně v $\sqrt{p}$

![Michał Strojnowski, Public domain, via Wikimedia
Commons](./pictures/Rho-pollard.png)

Je ale jeden problém, jak můžeme použít sekvenci ${x_i mod p}$ když ani neznáme
$p$? Vše co potřebujeme znát, je kde se cyklí. A to se dá zjistit velmi
jednoduše: V sekvenci ${x_i mod p}_{i<=j}$ je cyklus pouze když jsou 2 index
$s, t <= j$ takové, že $x_s \equiv x_t (mod p)$.
Tuto rovnici přepíšeme na $x_s - x_t \equiv 0 (mod p)$. Což je to stejné jako
$p \mid nsd(x_s - x_t, n)$

Tudíž, pokud najdeme takové indexy $s, t$, aby $g = nsd(x_s - x_t, n) > 1$,
našli jsme cyklus, a zároveň faktor $g$.
Je také možné že $g = n$, v tom případě musíme zopakovat algoritmus s jinými
parametry, například jiné $x_0$, jinou konstantu $c$ ve funkci $f$

Pro nalezení tohoto cyklu můžeme použít jakýkoliv algoritmus pro hledání cyklů.

#### Floydův "želva a zajíc" algoritmus
Tento algoritmus najde cyklus pomocí 2 ukazatelů: želvy a zajíce. Pohybují se
po sekvenci různě rychle, želva pouze o jednu hodnotu, zatímco zajíc o 2.
Cyklus bude nalezen tehdy, když se zajíc a želva potkají.

Implementace pomocí tohoto algoritmu:
```py
def f(x: int, c: int, mod: int):
    return ((x*x % mod) + c) % mod


def rho_turtle_hare(n: int, x0: int = 2, c: int = 1) -> list[int]:
    turtle = x0
    hare = x0
    g = 1
    while g == 1:
        turtle = f(turtle, c, n)
        hare = f(f(hare, c, n), c, n)
        g = math.gcd(abs(turtle-hare), n)
    return [g, n//g]
```

#### Brentův algoritmus
Tento algoritmus je variace algoritmu želvy a zajíce, ale místo toho abychom
ukazatele posouvali o 1 a 2, posouváme je o mocniny 2.

```py
def rho_turtle_hare_brent(n: int, x0: int = 2, c: int = 1) -> list[int]:
    turtle = x0
    hare = f(x0, c, n)
    g = 1

    l = 1

    while g == 1:
        # želva se posune na místo zajíce
        turtle = hare

        # zajíc se posune o l míst
        for _ in range(l):
            hare = f(hare, c, n)

            g = math.gcd(abs(turtle-hare), n)
            if g > 1:
                break
        l *= 2

    return [g, n//g]
```

### Shorův algoritmus
Toto je teoretický algoritmus pro kvantové počítače, dnes zatím nevyužitý pro
faktorizaci větších čísel. Redukuje problém faktorizace na problém nalezení
řádu prvku.

Nejdříve zjistí zda je $n$ sudé, pokud ano, pak jsme nalezli dělitel: 2.
Pokud není, pak vybere náhodné číslo $2 <= a < n$
Je možné najít jeden z faktorů spočítáním jejich nejmenšího společného
dělitele, pokud není 1.

Pokud jsme doteď nenašli faktor, pak to znamená že $a$ a $n$ jsou nesoudělná, a
zde využije algoritmus kvantové subrutiny, a najde řád $r$ z $a$, což znamená
že $a^r \equiv 1 (mod n)$.
Z tohoto můžeme vědět že $n \mid a^r-1$, což může být rozděleno jako rozdíl
dvou mocnin: $n \mid (a^{r/2}+1)(a^{r/2}-1)$
Bohužel toto nefunguje pro liché $r$, takže by algoritmus musel vypočítat $r$
znovu s jinou hodnotou $a$.
Dále ale budeme počítat se sudou hodnotou $r$.
$n \nmid a^{r/2} - 1$, jelikož by to implikovalo že řád $a$ je $r/2$ a ne $r$.
Je možné, že $n \mid a^{r/2} + 1$ je pravda, pokud ano, pak je možné zjistit
faktor $n$, spočítáme $d = nsd(n, a^{r/2} - 1)$. Pokud $d = 1$, pak $n \mid
a^{r/2} + 1$ je pravda, a nejsme schopní najít netriviální faktor pomocí $a$, a
algoritmus musí zkusit znovu s jinou hodnotou $a$.
Pokud ale $d != 1$, našli jsme faktor $n$, a algoritmus skončí.

# Závěr
V této seminární práci jsme prošli historii prvočísel, jak se měnila jejich
definice a názor, jak je spojená s jednotkou, zda patří mezi ně ži nikoli.
Dále jsme si ukázali některé algoritmy pro vygenerování prvočísel a mohli jsme
vidět jejich efektivitu.
Další čemu jsme věnovali pozornost, je RSA algoritmus pro zašifrování, jak
funguje, jak vygeneruje klíče, a jak ho využít pro bezpečnou komunikaci.
Poslední, co jsme si ukázali bylo, jak toto zašifrování prolomit, jak kvantové
počítače mohou být nebezpečné pro soukromou komunikaci.

Veškerý kód v této práci můžete najít na https://github.com/vodam46/prvocisla

# Poděkování
Tato práce by nebyla nikdy dokončena bez pomoci mojí milované přítelkyně, která
často kontrolovala určité části zda jsou čitelné pro normálního člověka a našla
spoustu gramatických chyb. Bohužel, všichni jsme lidé, a tak některé stále
zůstaly.


[^1]: https://cs.uwaterloo.ca/journals/JIS/VOL15/Caldwell1/cald5.pdf
[^2]: https://farside.ph.utexas.edu/books/Euclid/Elements.pdf
[^3]: https://thalesandfriends.org/wp-content/uploads/2012/03/stevin_dismes.pdf
[^4]: https://quod.lib.umich.edu/e/eebo/A51541.0001.001/
[^5]: http://eulerarchive.maa.org/correspondence/letters/OO0765.pdf
[^6]: Gauss, C.F. (1986). Congruences of The First Degree. In: Disquisitiones
      Arithmeticae. Springer, New York, NY.
      https://doi.org/10.1007/978-1-4939-7560-0_2
[^7]: OEIS Foundation Inc. (2023), The prime numbers, Entry A000040 in The
      On-Line Encyclopedia of Integer Sequences, https://oeis.org/A000040.
[^8]: OEIS Foundation Inc. (2023), Prime numbers at the beginning of the 20th
      century (today 1 is no longer regarded as a prime)., Entry A008578 in The
      On-Line Encyclopedia of Integer Sequences, https://oeis.org/A008578.
[^9]: A.O.L. Atkin, D.J. Bernstein, Prime sieves using binary quadratic forms,
    Math. Comp. 73 (2004), 1023-1030. http://cr.yp.to/papers/primesieves.pdf
[^10]: https://oeis.org/A018844
[^11]: https://www.mersenne.org/
