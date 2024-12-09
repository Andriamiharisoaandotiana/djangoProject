def main():
    username ="andotiana"
    name = input ('entrer votre nom ')
    date = int(input ('entrer votre jour de naissance '))
    age = 45
    magie = age + date
    if magie>50 and name == username :
        print("tu es magic haha")
    else:
        print("you've lost the magic")
    fonction_ternaire =("you've lost the magic in you", "tu es magic") [magie>50 and name == username]
    #otran io satri true 1 d false 0  d par ordre chronologique 0 aloh zay vo 1

    print("hello "+ name+ " you are",age)
    print("hello "+ name+ " you are "+ str(age) , magie , fonction_ternaire, len(name))


# +=(zao = zao+ x)  -=   != ==  <   >   and|or reo tpk dia miasa daholo aty

if __name__ == '__main__':
    main()
    online_players = ["lebron ", "james ", "curry "]
    print(online_players)