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
        return render(request, "encyclopedia/not_found.html", {
            "title": title
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })


def search(request):
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
    return render(request, "encyclopedia/new_entry_creation.html")
