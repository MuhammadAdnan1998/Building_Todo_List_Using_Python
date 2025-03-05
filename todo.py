import click # to create a cli
import json # to save and load tasks from a file
import os # to check if the file exists

Todo_File = "todo.json"

def load_tasks():
    if os.path.exist(Todo_File):
        return []
    with open(Todo_File, "r") as file:
        return json.load(file)
    
    def save_tasks(tasks):
        with open (Todo_File, "w") as file:
            json.dump(tasks, file,indent=4)


@click.group()
def cli():
    """Simple todo- List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added sucessfully to the list: {task}")
    

@click.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks added yet")
        return
    
    for index, task 



cli.add_command(add)

if __name__ == "__main__":
    cli()