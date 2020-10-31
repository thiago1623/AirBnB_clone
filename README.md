[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]

<div align="center"><img src="images/gif2.gif" width="500" height="450"/>

# AirBnB Clone :fast_forward:

This repository contains the first phase of a student project to build a clone of the AirBnB website. This stage implements a command line interpreter to manage AirBnB objects. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

# USAGE :link:

</div>

1. Clone the repository.
   
2. Execute the command:

````
 $ ./console.py
````
3. When this command is run the following prompt should appear:
 
````diff
(hbnb)
````
4. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

---
<div align="center">

## COMMANDS  :open_file_folder:

</div>

| Command             | Description                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| create :pencil2:    | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id                                      |
| show :eyes:         | Prints the string representation of an instance based on the class name and id                                          |
| destroy :fire:      | Deletes an instance based on the class name and id                                                                      |
| all :crystal_ball:  | Prints all string representation of all instances based or not on the class name                                        |
| update :point_up_2: | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
| quit :end:          | Exit the program                                                                                                        |
| help :shell:        | Display help documentation of every command                                                                             |
	
## Example how to use

- all:crystal_ball:
```
(hbnb) all MyModel
** class doesn't exist **
```
- show :eyes:
````
(hbnb) show BaseModel 
** instance id missing **
````
````
(hbnb) show BaseModel Holberton
** no instance found **
````
- create :pencil2:
````
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
````
- all:crystal_ball:
````
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
````
- show :eyes:
````
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
````
- destroy :fire:
````
(hbnb) destroy
** class name missing **
````
- update :point_up_2:
````
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
````
- show :eyes:
````
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
````
- create :pencil2:
````
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
````
- all :crystal_ball:
````
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
````
- show :eyes:
````
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
````

```
(hbnb) 
```

### AUTHORS 
* [Santiago Trujillo](https://github.com/thiago1623) :guitar:
* [Laura Perez](https://github.com/lperezcas16) :smile_cat:

[contributors-shield]: https://img.shields.io/github/contributors/thiago1623/AirBnB_clone?style=flat-square
[contributors-url]: https://github.com/thiago1623/AirBnB_clone/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/thiago1623/AirBnB_clone.svg?style=flat-square
[forks-url]: https://github.com/thiago1623/AirBnB_clone/network/members
[stars-shield]: https://img.shields.io/github/stars/thiago1623/AirBnB_clone.svg?style=flat-square
[stars-url]: https://github.com/thiago1623/AirBnB_clone/stargazers
[issues-shield]: https://img.shields.io/github/issues/thiago1623/AirBnB_clone?style=flat-square
