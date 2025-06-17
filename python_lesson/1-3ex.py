def f3_1(text,startswith):
    ans = text.find(startswith)
    if ans != 1:
        ans = text[ans:]
        print(ans)
    return ans

assert f3_1("12345678","3") == "345678"

def f3_2(text):
    ans = text.find("社")
    result = text[:ans+1]+'-'+text[ans+1:]
    print(result)
    return result

assert f3_2("株式会社A") == "株式会社-A"