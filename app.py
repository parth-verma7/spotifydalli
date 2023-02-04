# import os
# import openai
# from flask import Flask, redirect, render_template, request, url_for
# app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")
# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))
#     result = request.args.get("result")
#     return render_template("index.html", result=result)
# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.
# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )


# import os

# import openai
# from flask import Flask, redirect, render_template, request, url_for

# app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Image.create(
#   prompt="a white siamese cat",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']


import os
# file=open('lyrics.txt','r')
# lyrics=file.readlines()
# for lyric in lyrics:
#     pass
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

l = []

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        query = request.form["prompt"]
        response = openai.Image.create(
        prompt=query,
        n=1,
        size="256x256"
        )
        image_url = response['data'][0]['url']
        l.append(image_url)
        # print(image_url)
        return redirect(url_for("index", result=image_url))
    # print(l)
    result = request.args.get("result")
    return render_template("index.html", result=result)

# @app.route("/api/<query>", methods=("GET", "POST"))
# def dalli(query):
#     if request.method == "POST":
#         response = openai.Image.create(
#         prompt=query,
#         n=1,
#         size="256x256"
#         )
#         print(response['data'])
#         image_url = response['data'][0]['url']
#         print(image_url)
#         return redirect(url_for("index", result=image_url))


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
