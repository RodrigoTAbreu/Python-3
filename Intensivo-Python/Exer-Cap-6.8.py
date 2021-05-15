dog = {
    'tutor':'Rafa',
    'raça':'Poodle'
}
cat = {
    'tutor':'Camila',
    'raça':'ciamez'
}
bird = {
    'tutor':'jose',
    'raça':'pombo'
}
pets = []
pets.append(cat)
pets.append(dog)
pets.append(bird)

for animal in pets:
    print('\tO nome do tutor é: {}'.format(animal['tutor'].title()))
    print('\tA raça do animal é: {}\n'.format(animal['raça'].title()))