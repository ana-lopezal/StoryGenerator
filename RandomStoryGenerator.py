# Importing random module
import random
## Creación de vector de iniciación de historia
Sentence_starter = ['Erase una vez', ' En un mundo muy lejano', 'En el comienzo de los tiempos', 'Hace 100 años']

## Creación de vector donde especifica el personaje
character = [' vivía un Rey.',' había un panadero llamado Jack.',
             ' vivía un granjero.', ' existía José, un caballero.']

## Creación de vector que indica el tiempo del día en el cual se lleva acabo la historia.
time = [' En un día normal por la mañana', ' En una noche fría y solitaria']

## Creación de vector que indica hacia donde va el personaje
story_plot = [' iba caminando hacia', ' iba a comer en un lugar mágico hacia']

## Creación de vector que especifica lugar
place = [' las montañas', ' el jardín', ' el castillo']

 ## Creación de vector que especifica personaje secundario 
second_character = [ ' cuando vió un caballo', ' cuando vió una princesa', ' cuando vió un perro']

## Creación de vector de edad del personaje secundario
age = [', que parecía no tener más de 25 años,', ', que se veía de una edad bastante avanzada,', 
       ', que se veía como si nunca hubiera descansado en su vida,', ', que parecía estar en una edad madura,' ]

## Creación de vector con la acción del personaje secundario
work = [' buscando algo con mucho esmero.', ' cavando un gran pozo.', ' corriendo de la forma más veloz que hubiera visto jamás.', 
        ' saltar sin control.']

## Print de la historia
print(random.choice(Sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_plot)+
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))
