print('Как вас зовут?')
name = input()
print ('Здравйвуйте,', name)
print('Сколько вам лет?')
A = input ()
print ('Ваш любимый цвет? (1 – красный, 2 – зеленый, 3 – синий)')
color = int (input())
print ('Ваша любимая музыка? (1 – классика, 2 – поп-музыка, 3 – рок)')
music = int (input())
print ("Ваше любимое время года? (1 – осень, 2 – зима, 3 – весна, 4 – лето")
time = int (input())
print ("Ваш любимый жанр фильма? (1 - боевик, 2 - детектив, 3 - ужасы")
film = int (input())
print ("Смотрите ли вы twitch? (1 - Да, 2 - Нет")
twitch = int (input())
print ("Любите ли вы кушать? (1 - Да, 2 - Нет")
eda = int (input())
print ("Имеете ли вы вредные привычки? (1 - Да, 2 - Нет")
B = int (input())
print ("Любите ли вы природу? (1 - Да, 2 - Нет")
life = int (input())
if (color == 2 or color == 1) and (music == 1) and (time == 2) and (film == 3 or film == 1) and (twitch == 1) and (eda == 1) and (B == 2) and (life == 1 or life == 2):
    print ('Мы с вами подружимся!')
elif color == 3:
elif music == 3:
elif time == 2 or time == 3:
elif film == 3:
elif twitch == 1:
elif eda == 1 or eda == 2:
elif B == 1 or B == 2:
print ('Возможно мы с тобой подружимся')
else:
    print ('Мы с вами не подружимся!')
