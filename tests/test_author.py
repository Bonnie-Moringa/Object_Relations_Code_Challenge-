from lib.models.author import Author
from lib.models.magazine import Magazine

def test_author_can_add_article():
    author = Author(name="Test Author")
    author.save()
    mag = Magazine(name="Test Mag", category="Science")
    mag.save()
    article = author.add_article(mag, "Amazing Science")
    assert article.title == "Amazing Science"
    assert article.author_id == author.id
