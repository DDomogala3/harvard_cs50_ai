import csv
import sys
#states are people, actions are movies
from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    #from the Duck, for each node check if it's the goal, then add it to the path and keep making nodes
    
    num_explored = 0
    #neighbors_data_source = neighbors_for_person(source)
    
    start = Node(state = source, parent = None, action = None)
    frontier = QueueFrontier()
    frontier.add(start)
    explored = set()
    goal = target
    path = []
    #print(goal)
    #the start node is always going to be the source
    while frontier.empty() == False:
        if frontier.empty():
            raise Exception("no solution")
        #Choose a node from the frontier
        node = frontier.remove()
        #print(node.state)
        num_explored += 1
    
        if node.state == goal:
            print("found")
            actions = []
            cells = []
            
            first_path = []
            return node.state
            while node.parent is not None:
                first_tuple = (node.state,node.action)
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
                print("found")
                print(first_tuple)
                return actions
            actions.reverse()
            cells.reverse()
            solution = (actions, cells)
            first_path.append(first_tuple)
            print(first_path)
            return first_path
            
        explored.add(node.state)
    
        
        for movie_id, person_id in neighbors_for_person(source):
                #print(person_id)
            if not frontier.contains_state(person_id) and person_id not in explored:
                child = Node(state=person_id, parent = node, action = movie_id)
                frontier.add(child)
                explored.add(child.state)
                    #print(explored.state)
                source_path = (child.action, child.state)
                child_states = []
                child_states.append(child.state)
                    #print(child.state)
                    #print(source_path)
                
                    
                path.append(source_path)
                #return path
        
        child_state_list = []
        for i,j in path:
            child_state_list.append(j)
            #if j == target:
                    #print("found!")
                    #print(j)
                    #print(child_state_list.index(j))
                
                    
      
        
                
                            
        #node_2 = frontier.remove()
        #print(node_2.state)
        #return path
    
                
        
                    
                    
 
    raise NotImplementedError
    
    


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
