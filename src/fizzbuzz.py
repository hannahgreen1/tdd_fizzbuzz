def fizz_buzz(number):
    if not number:
        return f"invalid number {number}"
    elif number %15 == 0:
        return 'fizzbuzz'
    elif number %3 == 0:
        return 'fizz'
    elif number %5 == 0:
        return 'buzz'
    return str(number)