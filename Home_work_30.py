from abc import ABC, abstractmethod


class PalindromeStrategy(ABC):
    """Абстрактный интерфейс для всех стратегий проверки палиндромов."""
    
    @abstractmethod
    def is_palindrome(self, text: str) -> bool:
        """
        Проверяет, является ли текст палиндромом.
        
        Args:
            text: Строка для проверки
            
        Returns:
            bool: True, если строка является палиндромом, иначе False
        """
        pass


class SingleWordPalindrome(PalindromeStrategy):
    """Конкретная реализация стратегии для проверки одиночных слов."""
    
    def is_palindrome(self, text: str) -> bool:
        """
        Проверяет, является ли отдельное слово палиндромом (без учета регистра).
        
        Args:
            text: Слово для проверки
            
        Returns:
            bool: True, если слово является палиндромом, иначе False
        """
        # Приводим к нижнему регистру и сравниваем с перевернутой строкой
        text = text.lower()
        return text == text[::-1]


class MultiWordPalindrome(PalindromeStrategy):
    """Конкретная реализация стратегии для проверки многословных выражений."""
    
    def is_palindrome(self, text: str) -> bool:
        """
        Проверяет, является ли выражение палиндромом, игнорируя пробелы и регистр.
        
        Args:
            text: Выражение для проверки
            
        Returns:
            bool: True, если выражение является палиндромом, иначе False
        """
        # Удаляем пробелы и приводим к нижнему регистру
        text = text.lower().replace(" ", "")
        return text == text[::-1]


class PalindromeContext:
    """Класс, отвечающий за использование текущей стратегии."""
    
    def __init__(self, strategy: PalindromeStrategy = None):
        """
        Инициализирует контекст с опциональной стратегией.
        
        Args:
            strategy: Начальная стратегия проверки палиндромов
        """
        self.strategy = strategy
    
    def set_strategy(self, strategy: PalindromeStrategy) -> None:
        """
        Устанавливает новую стратегию.
        
        Args:
            strategy: Новая стратегия проверки палиндромов
        """
        self.strategy = strategy
    
    def check(self, text: str) -> bool:
        """
        Проверяет, является ли текст палиндромом, используя установленную стратегию.
        
        Args:
            text: Текст для проверки
            
        Returns:
            bool: True, если текст является палиндромом, иначе False
        """
        if self.strategy is None:
            raise ValueError("Стратегия не установлена")
        return self.strategy.is_palindrome(text)


class PalindromeFacade:
    """Фасад для упрощения работы с проверкой палиндромов."""
    
    def __init__(self):
        """Инициализирует фасад с контекстом и стратегиями."""
        self.context = PalindromeContext()
        self.single_word_strategy = SingleWordPalindrome()
        self.multi_word_strategy = MultiWordPalindrome()
    
    def check_palindrome(self, text: str) -> bool:
        """
        Определяет, какое правило проверки применить и проводит проверку.
        
        Args:
            text: Текст для проверки
            
        Returns:
            bool: True, если текст является палиндромом, иначе False
        """
        # Определяем стратегию на основе количества слов
        if len(text.split()) > 1:
            self.context.set_strategy(self.multi_word_strategy)
        else:
            self.context.set_strategy(self.single_word_strategy)
        
        # Выполняем проверку с выбранной стратегией
        return self.context.check(text)


if __name__ == "__main__":
    facade = PalindromeFacade()
    
    # Тест 1: Одиночное слово-палиндром
    word = "Шалаш"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # True

    # Тест 2: Одиночное слово не палиндром
    word = "Питон"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # False

    # Тест 3: Многословное выражение-палиндром
    phrase = "А роза упала на лапу Азора"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}")  # True

    # Тест 4: Многословное выражение не палиндром
    phrase = "Привет мир"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}")  # False

    # Тест 5: Одно слово с разными регистрами
    word = "РадаР"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # True

    # Тест 6: Сложная фраза с пробелами
    phrase = "Я иду с мечем судия"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}")  # True
