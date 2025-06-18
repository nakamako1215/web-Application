def f3_1(text,startswith):
    ans = text.find(startswith)
    if ans != 1:
        ans = text[ans:]
        print(ans)
    return ans

assert f3_1("12345678","3") == "345678"
def f3_2(text):
    if "株式会社" in text:
        index = text.find("株式会社")
        before = text[:index]
        after = text[index + len("株式会社"):]
        
        if before and after:
            return before + '-' + "株式会社" + '-' + after
        elif before:
            return before + '-' + "株式会社"
        elif after:
            return "株式会社" + '-' + after
        else:
            return "株式会社"
    else:
        return text
assert f3_2("株式会社A") == "株式会社-A"

def f3_3(li):
    return [f"{x:.2f}" for x in li]
       
     