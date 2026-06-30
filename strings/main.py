from gcdString import solution

def main():
    str1 = "ABCABCABCABCABCABC"
    str2 = "ABCABCABC"
    #s = solution()
    #print(s.gcdOfStrings(str1, str2))
    #as staticmethod decorator is used, we can call the method directly from the class without creating an instance
    #of the class.
    print(solution.gcdOfStrings(str1, str2))
    print(solution.findgcd(20,5))

if __name__ == "__main__":
    main()
