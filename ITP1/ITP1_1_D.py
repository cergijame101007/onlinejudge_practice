n = int(input())

if (0 <= n < 86400):
    hour = int(n/3600)
    minute = int((n%3600)/60)
    second = int(n % 60)
    print(f"{hour}:{minute}:{second}")