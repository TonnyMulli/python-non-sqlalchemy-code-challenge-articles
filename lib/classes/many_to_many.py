class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title length must be between 5 and 50 characters.")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

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
        if not self.articles():
            return None
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name length must be between 2 and 16 characters.")
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")
        if not category:
            raise ValueError("Category must not be empty.")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name length must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        if not value:
            raise ValueError("Category must not be empty.")
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
        if not Article.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()))
