# 38. Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв"".(Задание из семинара)

text = "Привет, меабв! ааааа вабв, ааа! Вабв, абв"
text = text.split()
new_text = []

for i in range(len(text)):
    if "абв" not in text[i]:
        new_text.append(text[i])

print(" ".join(new_text))