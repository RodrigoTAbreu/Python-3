unconfirmed_users = ['ana','beatriz','joao','pedro']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print('Verificando usuários: {}'.format(current_users.title()))
    confirmed_users.append(current_users)

print('\nOs seguintes usuários foram confirmados:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())