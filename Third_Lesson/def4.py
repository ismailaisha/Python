from jinja2 import Environment, FileSystemLoader

users = [
    {"name": "Aisha", "email": "aisha@example.com"},
    {"name": "Denis", "email": "denis@example.com"},
    {"name": "Maria", "email": "maria@example.com"}
]

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.html")

result = template.render(users=users)

print(result)