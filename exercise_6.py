def main ():
    import user_prompts
    
    triple = []
    while True:
        quit = user_prompts.get_yn("Do you want to quit")
        if quit:
            break
        value = user_prompts.get_float("Enter a number")
        triple.append(value)
        if len(triple)>= 3:
            if len(triple) > 3:
                del triple[0]
            average = sum(triple)/3
            print(f"The average of the last three entries is {average:.2f}")
main()