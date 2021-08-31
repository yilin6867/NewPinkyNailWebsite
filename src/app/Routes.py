import pathlib
from flask import current_app, render_template, redirect


@current_app.route("/")
def get_landing():
    return render_template(
        template_name_or_list="content_home.html"
    )


@current_app.route("/<content>")
def get_content(content):
    html_file = current_app.template_folder + "/content_{}.html".format(content)
    if pathlib.Path.is_file(html_file):
        return render_template(
            template_name_or_list=html_file
        )
    else:
        return redirect("/")


@current_app.route("/site")
def get_site():
    return render_template(
        template_name_or_list="site.html"
    )
