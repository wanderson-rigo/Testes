original = "2023320470"
invertida = original[::-1] # Slice notation list[<start>:<stop>:<step>]
print(original)
print(invertida)

subtracao = []
for index in range(len(original)):
    o = original[index]
    i = invertida[index]
    r = abs(int(o) - int(i))
    subtracao.append(r)

print(subtracao)
s = ''.join([str(n) for n in subtracao])
print(s)
print(sum(subtracao))



original = "2023328432"
invertida = original[::-1]
print(original)

print(invertida)

subtracao = [abs(int(o) - int(i)) for o, i in zip(original, invertida)]
s = ''.join(map(str, subtracao))
print(subtracao)
print(s)
print(sum(subtracao))