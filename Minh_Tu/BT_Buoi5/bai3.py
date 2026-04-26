try:
    #nhap nam sinh
    year_of_birth = int(input('nhap nam sinh: '))
    current_year = 2026
    if year_of_birth > current_year:
        raise ValueError('Năm sinh không thể lớn hơn năm hiện tại')
    elif year_of_birth <= 0:
        raise ValueError('Năm sinh không được nhỏ hơn 0')   
except ValueError as e:
    print('Issue: ', e)
else:
    age = current_year - year_of_birth
    print('so tuoi hien tai:', age)
