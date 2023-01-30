import json
import re
from urllib.request import Request, urlopen
from pathlib import Path

def dl_from_danbooru_link(url, output_dir, dl_captions=False):
    pass

def dl_from_danbooru_id(id, output_dir, custom_name=None, dl_captions=False):
    number_regex = re.compile(r"\d+")

    if not number_regex.match(id):
        raise Exception(f"Error while trying to download from Danbooru: ID {id} is not a number")

    url = f"https://danbooru.donmai.us/posts/{id}.json"
    
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        post_data = urlopen(request).read().decode("utf-8")
        post_data = json.loads(post_data)

        # Get the file url
        file_url = post_data["file_url"]
        
        # Download the file
        file_name = file_url.split("/")[-1] # Get the file name from the url
        file_name = custom_name if custom_name else file_name
        file_path = Path(output_dir) / file_name # TODO: add extension

        request = Request(file_url, headers={"User-Agent": "Mozilla/5.0"})

        file_path.write_bytes(urlopen(request).read())

        # Download the captions
        if dl_captions:
            tags = post_data["tag_string"]
            tags = _tags_string_to_list(tags)
            tags = ",".join(tags)
            tags_path = file_path.with_suffix(".txt")
            tags_path.write_text(tags)

    except Exception as e:
        raise Exception(f"Error while trying to download from Danbooru: {e}")

def _tags_string_to_list(tags_string):
    # Split the string by spaces
    tags = tags_string.split(" ")
    # Replace all _ with spaces
    tags = [tag.replace("_", " ") for tag in tags]

    return tags