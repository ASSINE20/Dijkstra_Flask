from flask import Flask, request, render_template,redirect, url_for
import dijkstra

app = Flask(__name__)

# définir les distances entre les villes ici, sous forme de dictionnaire
distance_villes = {
        "Dakar":{},
        "Rufisque":{"Dakar":13 , "Thiès":46 , "Mbour": 73},
        "Tivaouane":{"Thiès":28 , "Kébémer":65 , "Mbacké":115},
        "Thiès":{"Bambey":51, "Mbour":51},
        "Mbour":{"Fatick":64},
        "Fatick":{"Kaolack":45},
        "Louga":{"Kébémer":40, "Saint-Louis":71, "Linguère":126},
        "Linguère":{},
        "Kébémer":{},
        "Dagana":{"Saint-Louis":128, "Podor":77},
        "Podor":{},
        "Saint-Louis":{},
        "Matam":{"Podor":242, "Bakel":155, "Linguère":225},
        "Bakel":{},
        "Kidira":{"Bakel":64, "Goudiri":69},
        "Goudiri":{},
        "Mbacké":{"Kébémer":100, "Diourbel":40},
        "Diourbel":{"Bambey":24, "Kaolack":67},
        "Bambey":{},
        "Kaolack":{"Kaffrine":64 , "Nioro du Rip":560, "Foundiougne":66},
        "Nioro du Rip":{},
        "Foundiougne":{},
        "Sokone":{"Foundiougne":41 , "Kaolack":51 , "Banjul":69},
        "Kaffrine":{},
        "Banjul":{},
        "Senoba":{"Nioro du Rip":43 , "Bignona":133},
        "Bignona":{"Sédhiou":85 , "Ziguinchor":31, "Banjul":119},
        "Sédhiou":{},
        "Ziguinchor":{"Oussouye":42, "Sédhiou":138},
        "Oussouye":{"Cap-Skiring":28 , "Elinkine":20},
        "Cap-Skiring":{},
        "Elinkine":{},
        "Kolda":{"Ziguinchor":184 , "Sédhiou":85, "Vélingara":130},
        "Vélingara":{"Kolda":130, "Tambacounda":94},
        "Kédougou":{},
        "Tambacounda":{"Goudiri":298, "Kaffrine":214, "Kédougou":233}
        }

#Affichage des résultats
path = []
def affiche_resultat(previous_nodes, shortest_path, start_node, target_node):
    
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)



@app.route("/")
def index():

    return render_template("index.html")

@app.route("/chemin", methods=["GET","POST"])
def chemin():
    
    if request.method == 'POST':

        debut = request.form['debut']
        fin = request.form['fin']
    
        nodes = distance_villes.keys()
        
 
        init_graph = distance_villes
        graph = dijkstra.Graph(nodes, init_graph)
        previous_nodes, shortest_path = dijkstra.dijkstra(graph=graph, start_node=debut)
        

        affiche_resultat(previous_nodes, shortest_path, start_node=debut, target_node=fin)
  
        return render_template("chemin.html",start_node=debut, target_node=fin, chemin =" -> ".join(reversed(path)),
        distance = "{}.".format(shortest_path[fin]))
    else:
        return redirect('Données non valide.')


if __name__ == "__main__":
    app.run(debug=True)
