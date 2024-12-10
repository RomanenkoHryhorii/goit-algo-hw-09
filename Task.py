def find_coins_greedy(amount):
    """
    Жадібний алгоритм для видачі решти.
    
    Args:
        amount (int): Сума решти для видачі.
    
    Returns:
        dict: Словник з номіналами монет та їх кількістю.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin
    
    return result

def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для мінімізації кількості монет.
    
    Args:
        amount (int): Сума решти для видачі.
    
    Returns:
        dict: Словник з номіналами монет та їх кількістю.
    """
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціалізація масиву для динамічного програмування
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    # Обчислення мінімальної кількості монет
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    # Відновлення складу монет
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin
    
    return result

# Приклади використання
print("Жадібний алгоритм для 113:")
print(find_coins_greedy(113))

print("\nДинамічне програмування для 113:")
print(find_min_coins(113))

# Тестування продуктивності
import timeit

def performance_test(amount):
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    dp_time = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    
    print(f"\nПродуктивність для суми {amount}:")
    print(f"Жадібний алгоритм: {greedy_time:.6f} секунд")
    print(f"Динамічне програмування: {dp_time:.6f} секунд")

# Тести для різних сум
performance_test(113)
performance_test(1000)
performance_test(10000)