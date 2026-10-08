import json
import glob

# Находим все JSON файлы в текущей папке
files = glob.glob('*.json')
# Исключаем итоговый файл, чтобы не зациклиться
files = [f for f in files if f != 'merged.json']

result = []

for file in sorted(files):  # sorted для одинакового порядка
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            result.append(data)
            print(f"✓ Добавлен: {file}")
    except Exception as e:
        print(f"✗ Ошибка в файле {file}: {e}")

# Сохраняем результат
with open('merged.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\n✓ Готово! Всего записей: {len(result)}")