класс ComplexNumber:
 """Представляет комплексное число."""

 def __init__ (я, реальный, воображаемый):
 """Инициализирует комплексное число."""
 self.real = настоящий
 self.imag = изображение

 def __str__ (самостоятельно):
 """Возвращает строковое представление комплексного числа."""
 если self.imag >= 0:
 возвращает f"{self.real} + {self.imag}i"
 ещё:
 возвращает f"{self.real} - {-self.imag}i"

 def __добавить__ (себя, другого):
 """Определяет операцию сложения."""
 if isinstance(другое, комплексное число):
 возвращает ComplexNumber(self.real + other.real, self.imag + other.imag)
 ещё:
 raise TypeError("Операнд должен быть комплексным числом.")

 def __mul__(я, другой):
 """Определяет операцию умножения."""
 if isinstance(другое, комплексное число):
 возвращает ComplexNumber(
 self.real * другой.реальный - self.imag * другой.imag,
 self.real * other.imag + self.imag * другое.реальное,
            )
 ещё:
 raise TypeError("Операнд должен быть комплексным числом.")

 def __truediv__ (я, другой):
 """Определяет операцию деления."""
 if isinstance(другое, комплексное число):
 знаменатель = other.real**2 + other.imag**2
 возвращает ComplexNumber(
 (self.real * other.real + self.imag * other.imag) / знаменатель,
 (self.imag * other.real - самость.реальность * other.imag) / знаменатель,
            )
 ещё:
 raise TypeError("Операнд должен быть комплексным числом.")
из complex_number импортируйте ComplexNumber
из регистратора импортировать регистратор


калькулятор классов:
 """Класс калькулятора для комплексных чисел."""

 def __init__(self, регистратор = Нет):
 """Инициализирует калькулятор."""
 self.logger = регистратор или Logger.get_instance()

 добавить определение (self, num1, num2):
 """Сложение комплексных чисел."""
 self.logger.log(f"Сложение: {num1} + {num2}")
 возврат num1 + num2

 умножение определения (self, num1, num2):
 """Умножение комплексных чисел."""
 self.logger.log(f"Умножение: {num1} * {num2}")
 возвращает num1 * num2

 определение деления (self, num1, num2):
 """Деление комплексных чисел."""
 self.logger.log(f"Деление: {num1} / {num2}")
 возврат num1 / num2
ведение журнала импорта


регистратор классов:
 """Класс для логирования."""

 __instance = Нет

 @staticmethod
 def get_instance():
 """Реализация паттерна Singleton."""
 если Logger.__instance равен None:
 Logger.__экземпляр = Logger()
 возвращает регистратор.__экземпляр

 def __init__ (самостоятельно):
 """Инициализирует логгер."""
 logging.basicConfig(имя файла="calculator.log", уровень = logging.ИНФОРМАЦИЯ)

 журнал определения (self, сообщение):
 """Записывает сообщение в лог."""
 logging.info(сообщение)
из калькулятора импортировать калькулятор
from complex_number import ComplexNumber


def get_complex_number():
           """Ввод комплексного числа с консоли."""
    while True:
        try:
            real = float(input("Введите действительную часть: "))
            imag = float(input("Введите мнимую часть: "))
            return ComplexNumber(real, imag)
        except ValueError:
            print(" ввод некоретин . Попробуйте снова.")


def main():
       """Основная функция программы."""
    calculator = Calculator()

    while True:
        print("\nВыберите операцию:")
        print("1 - Сложение")
        print("2 - Умножение")
        print("3 - Деление")
        print("4 - Конецц")

        choice = input("Введи номер операции: ")

 если выбор == "1":
 num1 = get_complex_number()
 num2 = get_complex_number()
 результат = calculator.add(num1, num2)
 print(f"Результат: {result}")
 выбор элифа == "2":
 num1 = get_complex_number()
 num2 = get_complex_number()
 результат = калькулятор.умножьте (num1, num2)
 print(f"Результат: {result}")
 выбор элифа == "3":
 num1 = get_complex_number()
 num2 = get_complex_number()
 попробуй:
 результат = калькулятор.разделите (num1, num2)
 print(f"Результат: {result}")
 кроме ошибки ZeroDivisionError:
 print("Деление на ноль невозможно.")
 выбор элифа == "4":
 перерыв
 ещё:
 print("Некорректный ввод. Попробуй снова.")


if __name__ == "__main__":
 главная()
