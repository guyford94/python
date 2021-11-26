

def get_password_from_user():
    password = input("Enter your password :")
    return password


def check_length(password):
    str_password = str(password)
    password_length = 0
    for char in str_password:
        password_length = password_length +1
    if(password_length < 5):
        return 0
    if(password_length < 7):
        return 5
    else:
        return 10


def check_diversity(password):
    def_password = password
    special_character_list = '[@_!#$%^&*()"<>?/\|}{~:]'
    number_flag = False
    letter_flag = False
    upper_letter_flag = False
    special_character_flag = False
    for char in def_password:
        if(char.isdigit()):
            number_flag = True
        if(char .isalpha()):
            letter_flag = True
        if(char .isupper()):
            upper_letter_flag = True
        if(char in special_character_list):
            special_character_flag = True
    return sum_diversity(number_flag, letter_flag, upper_letter_flag, special_character_flag)


def sum_diversity(number_flag, letter_flag, upper_letter_flag, special_character_flag):
    if(number_flag and letter_flag and upper_letter_flag and special_character_flag):
        return 10
    if(number_flag and letter_flag and upper_letter_flag):
        return 7
    if(number_flag and letter_flag):
        return 5
    if(letter_flag):
        return 3
    else:
        return 0


def check_common_words(password):
    common_words_list = ['abc', 'qwerty', 'love']
    password_as_string = str(password)
    start_of_password = password_as_string[0:8]
    for i in common_words_list:
        if(i in password_as_string):
            return 0
        if(start_of_password == 'password'):
            return 0
    return 10


def calculate_the_password_strength(length_score, diversity_score, common_words_score):
    return ((length_score + diversity_score + common_words_score)/3)


def print_password_strength(password_strength):
    if(password_strength < 5):
        print('your password is : Weak')
        return
    if(password_strength < 7):
        print('your password is : Medium')
        return
    if(password_strength < 9):
        print('your password is : Strong')
        return
    else:
        print('your password is : Very Strong')
        return


def main():
    password = get_password_from_user()
    length_score = check_length(password)
    diversity_score = check_diversity(password)
    common_words_score = check_common_words(password)
    password_strength = calculate_the_password_strength(length_score, diversity_score, common_words_score)
    print_password_strength(password_strength)


if __name__ == "__main__":
    main()
