import json

from first_part.models import Author, Quote


if __name__=="__main__":
    with open('json_files/author.json', encoding='UTF-8') as fd:
        data = json.load(fd)
        for el in data:
            author = Author(
                fullname=el.get('fullname'),
                born_date=el.get('born_date'),
                born_location=el.get('born_location'),
                description=el.get('description')
                )
            author.save()
    
    with open('json_files/quotes.json', encoding='UTF-8') as fd:
        data = json.load(fd)
        for el in data:           
                author,*_ = Author.objects(fullname=el.get('author'))
                quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
                
                quote.save()
