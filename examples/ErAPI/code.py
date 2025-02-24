from akenoai import AkenoXToJs

clients = AkenoXToJs(is_err=True)
js = clients.connect()

examples = "print('hello world')"

output = await js.get.create(
    "run",
    api_key="test",
    is_obj=True,
    c=examples,
    bhs="python"
)
print(output)
