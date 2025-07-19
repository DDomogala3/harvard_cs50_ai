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
    path_dict = {}
    
    while frontier.empty() == False:
        if frontier.empty():
            raise Exception("no solution")
        #Choose a node from the frontier
        node = frontier.remove()
        
        
        
        num_explored += 1
        
        if node.parent == None:
            path_dict[node.state] = (None, node.action)

        else:
            path_dict[node.state] = (node.parent.state, node.action)
        source_key = list(path_dict.keys())[0]
        target_state = list(path_dict.keys())[-1]
        print(path_dict[target_state][0])
        #print(source)
        #path_dict.update(nodenode.parent)
        key_list = []
        value_list = []
        path_concept = []
        for key,value in reversed(path_dict.items()):
        	#first_key = list(path_dict.keys)[0]
        	key_list.append(key)
        	value_list.append(value)
                #path_concept.append(value)
        	if key == source:
        		#key_list.append(key)
        		break
        		#key_list.append(key)
        	
        		
                
        
        #if target_key, source key 
        #create for loop to find path
        #add values in dictionary to path
        #if actor A and actor B starred in movie X together
        #add connection
        #walk back path to find movie connections
        
        for i in key_list:
            path_concept.append(path_dict[i])
                
        if node.state == goal:
            print("found")
            actions = []
            cells = []
            
            first_path = []
            zero_list = []
            
            #return node.state
            
            while node.parent is not None:
                first_tuple = (node.action,node.state)
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
                
                path_list = []
                
           # while node != start:
            #    path_list.append(node)
             #   node = node.parent   
            #path_list.append(start)
            print(node.state)
            #print(node.parent.state)
            print(start.state)
            print("this is the key list %s." %(key_list))
            print("this is the path concept %s." %(path_concept))
            print("The path concept length is %d." % (len(path_concept)))
                          
             
            actions.reverse()
            cells.reverse()
            print(actions)
            print(cells)
            solution = (actions, cells)
            first_path.append(first_tuple)
            #path_dict.update(first_path)
            print(path_dict)
            #print(first_path)
            print(first_path)
            
            if len(first_path) == 0:
                return path
            else:
               return first_path
        #return first_path
                 
        explored.add(node.state)
        explored.add(node.action)
    
        
        for movie_id, person_id in neighbors_for_person(node.state):
            #print(person_id)
            if not frontier.contains_state(person_id) and person_id not in explored:
                child = Node(state=person_id, parent = node, action = movie_id)
                frontier.add(child)
                
                    #print(explored.state)
                path = []
                source_path = (child.action, child.state)
                child_states = []
                child_states.append(child.state)
                    #print(child.state)
                    #print(source_path)
                path.append(source_path)
                
       
                
        
                    
                    
 
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
