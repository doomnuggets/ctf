# Hacky Easter 2017 Teaser challenges


Main challenge site as located here: https://hackyeaster.hacking-lab.com/teaser/


## Riddle 1

https://hackyeaster.hacking-lab.com/teaser/#riddle1

Reverse the string.

```
python -c "print 'MBD2A \!ysaep ,ysaE'[::-1]"
```

Output:

```
Easy, peasy! A2DBM
```

First flag is `A2DBM`


## Riddle 2

https://hackyeaster.hacking-lab.com/teaser/#riddle2

Base64 decode the string.

```
echo -n 'UGllY2Ugb2YgY2FrZSEgWlhHSUQ=' | base64 -d
```


Output:

```
Piece of cake! ZXGID
```

Second flag is `ZXGID`


## Riddle 3

https://hackyeaster.hacking-lab.com/teaser/#riddle3

What you first see:

```
One for free here: 404 - not found!
```

What you see after pressing `ctrl` + `a`:

```
One for free here: 404 - not found! XIZLS
```

Third flag is `XIZLS`


## Riddle 4

https://hackyeaster.hacking-lab.com/teaser/#riddle4

Looks like a packed javascript blob. Unpack it with http://jsbeautifier.org/

Before:
```
eval(function(p,a,c,k,e,d){e=function(c){return c};if(!''.replace(/^/,String)){while(c--){d[c]=k[c]||c}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('0(\'1\');',2,2,'alert|VYGY6'.split('|'),0,{}))
```

After unpacking:

```
alert('VYGY6');
```

Fourth flag is `VYGY6`


## Riddle 5

https://hackyeaster.hacking-lab.com/teaser/#riddle5

Looks like a bunch of MD5 hashes.

```
3a3ea00cfc35332cedf6e5e9a32e94da
9d5ed678fe57bcca610140957afab571
f09564c9ca56850d4cd6b3319e541aee
5dbc98dcc983a70728bd082d1a47546e
7fc56270e7a70fa81a5935b72eacbe29
```

Bruteforce the hashes and combine the outcome.

```
3a3ea00cfc35332cedf6e5e9a32e94da : E
9d5ed678fe57bcca610140957afab571 : B
f09564c9ca56850d4cd6b3319e541aee : Q
5dbc98dcc983a70728bd082d1a47546e : S
7fc56270e7a70fa81a5935b72eacbe29 : A
```

Fifth flag is `EBQSA`


## Riddle 6

https://hackyeaster.hacking-lab.com/teaser/#riddle6

Morse code!

```
--- -. . / -- --- .-. . / .... . .-. . ---... / .--- .- --- -- -.--
```

Decodes to:

```
ONE MORE HERE: JAOMY
```

Sixth flag is `JAOMY`


## Riddle 7


https://hackyeaster.hacking-lab.com/teaser/#riddle6

Welp, what is that? It could be an encoding which doesn't touch special chars.
Caeser Cipher?

```
Hwldp wx, Euxwh! QYAVL
```

Brute it:

```
hwldp wx, euxwh! qyavl
gvkco vw, dtwvg! pxzuk
fujbn uv, csvuf! owytj
etiam tu, brute! nvxsi   <------- maybe?
dshzl st, aqtsd! muwrh
crgyk rs, zpsrc! ltvqg
bqfxj qr, yorqb! ksupf
apewi pq, xnqpa! jrtoe
zodvh op, wmpoz! iqsnd
yncug no, vlony! hprmc
xmbtf mn, uknmx! goqlb
wlase lm, tjmlw! fnpka
vkzrd kl, silkv! emojz
ujyqc jk, rhkju! dlniy
tixpb ij, qgjit! ckmhx
shwoa hi, pfihs! bjlgw
rgvnz gh, oehgr! aikfv
qfumy fg, ndgfq! zhjeu
petlx ef, mcfep! ygidt
odskw de, lbedo! xfhcs
ncrjv cd, kadcn! wegbr
mbqiu bc, jzcbm! vdfaq
lapht ab, iybal! ucezp
kzogs za, hxazk! tbdyo
jynfr yz, gwzyj! sacxn
ixmeq xy, fvyxi! rzbwm
```

`etiam tu, brute!` looks the most promising. The rest of the bruteforced combinations are garbage
so I assume this is the flag we are looking.

Seventh flag is `NVXSI`


## Riddle 8

ASCII table to the rescue - or rather a python oneliner:

```
python -c 'print "".join([chr(int(c)) for c in "84 97 107 101 32 116 104 105 115 58 32 71 89 53 84 70".split(" ")])'
```

output:

```
Take this: GY5TF
```

Eigth flag is `GY5TF`


## Riddle 9

Took me way longer than it should have.
The leading `/` and the word `bit` suggests that it's a `bit.ly` link.

```
bit.ly/2mi4AMj
```

This leads us to a `let me google that for you` page where the flag is typed in.

Ninth flag is `5DFME`


## Riddle 10

No comment? Comments are usually not visible - inspect the html source code.

```
<p>No comment.<!-- A43JN --></p>
```

tenth flag is `A43JN`


## Riddle 11

Unicode! Looks like only two types of chars are used in this encoding. Is it binary?

Decode the first byte to see which unicode char stands for `0` or `1`.

`10111100` doesn't decode to a letter, so I assume it's the other way around.
`01000011` decodes to `C` (in other words the spooky ghosts are `0` and the alien heads are `1`)

With this information we can then take it to our beloved python3.

```python3
import binascii

x = '👻👽👻👻👻👻👽👽👻👽👻👻👽👽👽👽👻👽👻👻👽👽👽👻👻👽👻👻👻👽👽👽👻👽👻👽👻👻👽👻👻👽👻👻👻👻👻👽👻👽👻👽👻👽👻👻👻👽👻👽👻👻👽👽👻👻👽👻👻👻👻👽👻👻👽👻👻👻👻👻👻👽👻👻👽👽👽👻👻👻👽👽👻👽👻👽👻👽👻👽👽👻👻👻👻👽👻👻👻👽👽👽👻👽👻👻👽👻👽👽'
zero = '👻'
one = '👽'
for c in x:
    if c == zero:
        bin_str += '0'
    else:
        bin_str += '1'

print binascii.unhexlify('%x', % int(bin_str, 2))
```

Output:

```
CONGRATS! N5XGK
```

Eleventh flag is `N5XGK`


## Riddle 12

It's XOR.

I wrote the following script to solve it:

```python

values = '697c611778601371647d12177e7d060572'
actual_values = [values[i] + values[i+1] for i in range(0, len(values), 2)]

keys = '3133333731333337313333373133333731'
actual_keys = [keys[i] + keys[i+1] for i in range(0, len(keys), 2)]

print ''.join([chr(int(value, 16) ^ int(key, 16)) for key, value in zip(actual_keys, actual_values)])
```

Output:

```
XOR IS FUN! ON52C
```

Twelvth flag is `ON52C`


## Riddle 13

Ceasar Cipher - again?!


```
urer lbh tb: mjx4e
tqdq kag sa: liw4d
spcp jzf rz: khv4c
robo iye qy: jgu4b
qnan hxd px: ift4a
pmzm gwc ow: hes4z
olyl fvb nv: gdr4y
nkxk eua mu: fcq4x
mjwj dtz lt: ebp4w
livi csy ks: dao4v
khuh brx jr: czn4u
jgtg aqw iq: bym4t
ifsf zpv hp: axl4s
here you go: zwk4r   <----- yup
gdqd xnt fn: yvj4q
fcpc wms em: xui4p
ebob vlr dl: wth4o
dana ukq ck: vsg4n
czmz tjp bj: urf4m
byly sio ai: tqe4l
axkx rhn zh: spd4k
zwjw qgm yg: roc4j
yviv pfl xf: qnb4i
xuhu oek we: pma4h
wtgt ndj vd: olz4g
vsfs mci uc: nky4f
```

Thirteenth flag is `ZWK4R`


## Riddle 14

A hex dump? Decode the hex blob and store it as a new binary file. It's a `PNG`, open it (preferably in a image editor because it's tiny) to see the flag.

Fourteenth flag is `AGBTC`


## Riddle 15

It's regex, match the pattern and print out the match groups in the form of `$2E$44`.
This pattern yields the following match groups:

1. `FR`
2. `ID`
3. `AY THE THIRTEE`
4. `N`
5. `TH, 4:00 PM`

Assemble the pieces and you get the flag.

Fifteenth flag is `IDEN4`


## Riddle 16

It's Base85, decode it and win.

```
This is the last one! DFMFZ
```

Sixteenth flag is `DFMZ`


# Last Challenge

We now have [all the flags](flags) required to solve the final challenge. Our task is to
decode the flags (or fragments), but the order of the fragments also needs to be fixed.


The first thing that came to mind was `BRUTEFORCE ALL THE THINGS` - but I later realized
it's gonna take a while to bruteforce a 16 long key combination. Long story short, I
solved it by only bruteforcing a limited range of keys (like 1 - 4), then removing those
decoded results from the rest of the key pool.

This is the script I came up with and used to complete the challenge.

```python
#!/usr/bin/env python2
import sys
import math
import itertools
import multiprocessing
from multiprocessing.pool import ThreadPool as Pool

import anybase32

# Pre solved order as the keys were bruteforced partially and populated part by
# part.
L1 = ['N5XGK', 'IDEN4', 'ZXGID', 'ON52C', 'A43JN', 'VYGY6', 'JAOMY', 'GY5TF',
      'EBQSA', '5DFME', 'ZWK4R', 'AGBTC', 'A2DBM', 'NVXSI', 'DFMFZ', 'XIZLS']

def detect_the_thing(combo):
    dec = anybase32.decode(''.join(combo))
    try:
        dec.decode('ascii')
        return combo, dec
    except UnicodeDecodeError:
        pass

total_count = str(math.factorial(len(L1)))
pool = Pool(multiprocessing.cpu_count()*2)

for count, combo in enumerate(pool.imap_unordered(detect_the_thing, itertools.permutations(L1, len(L1)))):
    if combo:
        print combo
    sys.stderr.write(' '.join(('\r'*30, str(count), 'of', total_count, ' ')))
```
