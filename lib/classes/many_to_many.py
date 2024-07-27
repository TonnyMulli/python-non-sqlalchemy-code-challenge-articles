class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = self._validate_title(title)
        self.author = self._validate_author(author)
        self.magazine = self._validate_magazine(magazine)
        Article.all.append(self)

    @staticmethod
    def _validate_title(title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title length must be between 5 and 50 characters.")
        return title

    @staticmethod
    def _validate_author(author):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        return author

    @staticmethod
    def _validate_magazine(magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        return magazine

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable.")


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not name:
            raise ValueError("Name cannot be empty.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable.")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):

        articles = self.articles()
        if not articles:
            return None

        magazine_categories = [article.magazine.category for article in articles]
        return list(set(magazine_categories))


class Magazine:
    all = []

    def __init__(self, name: str, category: str) -> None:
        if not (2 <= len(name) <= 16):
            raise ValueError("Name length must be between 2 and 16 characters.")
        if not category:
            raise ValueError("Category cannot be empty.")

        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 2 <= len(value) <= 16:
            raise ValueError("Name must be a string with length between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        contributing_authors = [author for author in set(authors) if authors.count(author) > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        max_articles = max(map(len, (magazine.articles() for magazine in cls.all)))
        return next((magazine for magazine in cls.all if len(magazine.articles()) == max_articles), None)
