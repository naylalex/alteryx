def accumulated_sum(i):
    i = int(i)
    if i < 0:
        raise Exception("Unsupported value.")
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return i + accumulated_sum(i-1)

if __name__ == "__main__":
    import sys
    print(accumulated_sum(sys.argv[1]))

