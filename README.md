## Something about ELGamal ##

### Generate: ###
```
e = Elgamal()
e.generate(512)
p = e.p
g = e.g
y = e.y
# k is secret
k = e.k
```

### Encrypt: ###
```
e = Elgamal(p, g, y)
c1, c2 = e.encrypt(b"i love you")
```

### Decrypt: ###
```
e = Elgamal()
plaintext = e.decrypt(c1, c2, p, k)
```
