class Author:
    def __init__(self, name):
        assert isinstance(name, str) and len(name) > 0
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    _instances = []

    def __init__(self, name, category):
        assert isinstance(name, str) and 2 <= len(name) <= 16
        assert isinstance(category, str) and len(category) > 0
        self._name = name
        self._category = category
        self._articles = []
        self.__class__._instances.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str) and 2 <= len(value) <= 16
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        assert isinstance(value, str) and len(value) > 0
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    @classmethod
    def top_publisher(cls):
        if not cls._instances:
            return None
        return max(cls._instances, key=lambda magazine: len(magazine.articles()))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        return [author for author in set(authors) if authors.count(author) > 2]


class Article:
    def __init__(self, author, magazine, title):
        assert isinstance(title, str) and 5 <= len(title) <= 50
        assert isinstance(author, Author)
        assert isinstance(magazine, Magazine)
        self._title = title
        self._author = author
        self._magazine = magazine
        magazine._articles.append(self)
        author._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        assert isinstance(value, Author)
        self._author = value
        value._articles.append(self)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        assert isinstance(value, Magazine)
        self._magazine = value
        value._articles.append(self)
