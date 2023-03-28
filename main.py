from livereload import Server, shell
from jinja2 import Environment, FileSystemLoader, select_autoescape


def rebuild():
    template_page = 'template.html'
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template(template_page)
    rendered_page = template.render()
    
    with open('index.html', 'w', encoding="utf-8") as file:
        file.write(rendered_page)


def main():
    rebuild()

    server = Server()

    server.watch('template.html', rebuild)

    server.serve(root='.')


if __name__ == '__main__':
    main()
