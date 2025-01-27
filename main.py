from sanic import Sanic
from sanic.response import json, text

app = Sanic("WebTask")

@app.post("/submit")
async def get_answers_and_print(request):
    username = request.form.get("username")
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    question3 = request.form.get('question3')
    print(username,question1,question2,question3)
    calculateddata = 1 ## do_something
    return json({
        "status": "success",
        "data": calcuateddata
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)