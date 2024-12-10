T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    
    max_profit = 0
    max_price = 0
    
    # 뒤에서부터 앞으로 진행
    for price in reversed(prices):
        # 현재까지의 최대 가격과 비교
        if price > max_price:
            max_price = price
        else:
            # 현재 가격으로 사서 max_price에 팔 때의 이익을 더함
            max_profit += max_price - price
            
    print(max_profit)