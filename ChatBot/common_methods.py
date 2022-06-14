import urllib.request


def load_photo(film, upload):
    url = film.photo
    img = urllib.request.urlopen(url).read()
    out = open("img.jpg", "wb")
    out.write(img)
    out.close()
    photo = upload.photo_messages('img.jpg')

    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    return attachment
