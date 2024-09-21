gasto_dia= []

meta_diaria = float(input('Coloque sua meta diaria aqui: '))
print('')

if meta_diaria > 0:
    print('Quando finalizar o dia, digite 0')
    print('')

    while True:
        gasto_do_dia= float(input('Coloque oq vc for gastando ao longo do dia aqui: '))
        print('')
        
        if gasto_do_dia == 0:
            break
        
        gasto_dia.append(gasto_do_dia)
    
    if sum(gasto_dia) < meta_diaria:
        print('Ótimo, vc se manteve abaixo da sua meta diária! Guarde o resto do dinheiro para investimentos futuros')
        print('')
        print(f'Sua meta: R$ {meta_diaria:.2f}')
        print('')
        print(f'Seu gasto do dia: R$ {sum(gasto_dia):.2f}')

    elif sum(gasto_dia) == meta_diaria:
        print('Cuidado! Você gastou exatamente sua meta, tente gastar menos no próximo dia!')
        print('')
        print(f'Sua meta: R$ {meta_diaria:.2f}')
        print('')
        print(f'Seu gasto do dia: R$ {sum(gasto_dia):.2f}')

    else:
        print('Você gastou mais do que sua meta! Faltará dinhheiro para os próximos dias por conta do seu deslize')
        print('')
        print(f'Sua meta: R$ {meta_diaria:.2f}')
        print('')
        print(f'Seu gasto do dia: R$ {sum(gasto_dia):.2f}')

else:
    print('Não pretende gastar nada hoje? Muito bem!')