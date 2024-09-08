import markdown
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content is None:
        return None
    else:
        return markdowner.convert(content)


def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"Entry '{title}' was not found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })


def search(request):
    if request.method == 'POST':
        input_entry = request.POST['q']
        recommendations = []
        for entry in util.list_entries():
            if input_entry.lower() in entry.lower():
                recommendations.append(entry)
        return render(request, 'encyclopedia/recommendations.html', {
            'recommendations': recommendations,
            'input_entry': input_entry
        })


def new_entry(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/new_entry_creation.html")
    else:
        new_title = request.POST['title']
        new_content = request.POST['content']
        title_flag = util.get_entry(new_title)
        if title_flag:
            return render(request, "encyclopedia/error.html", {
                "message": f"This entry '{new_title}' is already exist"
            })
        else:
            util.save_entry(new_title, new_content)
            html_content = convert_md_to_html(new_title)
            return render(request, "encyclopedia/entry.html", {
                "title": new_title,
                "content": html_content
            })


def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })


def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
