def solve_captcha(captcha):
    intcaptcha = [int(d) for d in str(captcha)]
    result = [x for ctr, x in enumerate(intcaptcha) if x == intcaptcha[(ctr + 1) % len(intcaptcha)]]
 
    return sum(result)