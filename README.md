# Перезагрузка компьютеров из списка через 60 секунд
Использовано:
- Python 3.10.2
- Pyinstaller 4.10
- Немножечко мозгов и скилла

---

Клонирование:
```
git clone https://github.com/JDM170/comp_auto_restart.git --recurse-submodules
```

---

Запуск:
```
python main.py
```

---

Сборка (без UPX):
```
pyinstaller --clean --console --onefile --name comp_auto_restart main.py
```

Сборка (с UPX):
```
pyinstaller --clean --console --onefile --upx-dir=upx\ --name comp_auto_restart main.py
```
