current_users = ['admin','pedro','ana','ester','MARIA','tamires']
new_users = ['carla','maria','ana','carlos','josue','moises']



for nome in new_users:
    if nome in current_users:
        print(f"{nome}. Você deve informar um novo nome de usuário.")
    else:
        print(f"Nome {nome} está disponível.")