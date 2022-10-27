



# def buildIncFunction(inc):
    
#     def incValue(value):
#         return inc+value

#     return incValue

# def buildIncFunction(inc):
#     dataset = [...]
#     return lambda value:inc+value

buildIncFunction = lambda inc:lambda value:inc+value

def main():
    inc = buildIncFunction(2)

    i = inc(3) # 5
    print(i)
if __name__=='__main__':
    main()
