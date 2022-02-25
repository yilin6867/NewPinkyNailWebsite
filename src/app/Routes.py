import pathlib, os
from flask import current_app, render_template, redirect


@current_app.route("/")
def get_landing():
    return render_template(
        template_name_or_list="content_home.html",
        content="home"
    )


@current_app.route("/<content_type>")
def get_content(content_type):
    if os.path.isfile(current_app.template_folder + "/content_{}.html".format(content_type)):
        return render_template(
            template_name_or_list="content_{}.html".format(content_type),
            content=content_type
        )
    else:
        return redirect("/")


@current_app.route("/site")
def get_site():
    return render_template(
        template_name_or_list="site.html"
    )
