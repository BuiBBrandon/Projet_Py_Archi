import click
import uuid
import pickle

from dataclasses import dataclass


#Objet classe
@dataclass
class Todo:
    id: int
    task: str

monPass = "BD_Tache/"

@click.group()
def cli():
    pass

#Créer une tache et la stock dans un fichier
#Nom de la tache. 
#Prompt oblige à l'utilisateur de rentrer un paramètre
#--task --> permet d'associer le paramètre à
@cli.command()
@click.option('--task', prompt='Task')
def create(task: str):
    todo = Todo(id=uuid.uuid4().int, task=task)
    click.echo(todo)
    with open(monPass+str(todo.id)+".p","wb") as fileNam:
        pickle.dump(todo,fileNam)
    
#Affiche toute les taches du fichier
@cli.command()
@click.option('--id', required = True)
def affiche_tache(id: int):
    with open(monPass+str(id),"rb") as f:
        todo = pickle.load(f)
    click.echo(todo)


    

