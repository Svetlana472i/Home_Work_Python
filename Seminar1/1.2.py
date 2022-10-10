# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
num=[0,1]
for j in num:
    for k in num:
        for n in num:
                result = not(j and k and n) == (not j) or (not k) or (not n)
                if not result :
                   print('x=',j,'y=',k,'z=',n, 'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно','(',result,')')
                else:
                   print('x=',j,'y=',k,'z=',n, 'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно','(',result,')')