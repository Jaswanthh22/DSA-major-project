# tribe_data.py

tribes = {
    "Warrior": {
        "traits": {"bravery", "strength", "honor", "discipline", "risk-taking"},
    },
    "Sage": {
        "traits": {"wisdom", "patience", "curiosity", "clarity"},
    },
    "Explorer": {
        "traits": {"adventure", "curiosity", "risk-taking", "freedom"},
    },
    "Artist": {
        "traits": {"creativity", "expression", "sensitivity", "emotion", "clarity"},
    }
}

# Step 1: Build graph (adjacency list) based on shared traits
def build_graph():
    graph = {tribe: set() for tribe in tribes}
    for t1 in tribes:
        for t2 in tribes:
            if t1 != t2:
                traits1 = tribes[t1]["traits"]
                traits2 = tribes[t2]["traits"]
                if traits1 & traits2:  # if they share any traits
                    graph[t1].add(t2)
                    graph[t2].add(t1)  # ensure bidirectional connection
    # Convert sets to lists for consistent output
    return {tribe: list(neighbors) for tribe, neighbors in graph.items()}

# Step 2: Find the best tribe match based on user traits
def find_best_tribe(user_traits):
    scores = []

    for name, data in tribes.items():
        traits = data["traits"]
        match_count = len(set(user_traits) & traits)
        percent = (match_count / len(traits)) * 100
        scores.append((name, match_count, percent))

    scores.sort(key=lambda x: x[1], reverse=True)
    best_tribe = scores[0][0] if scores and scores[0][1] > 0 else "Wanderer"
    description = tribes.get(best_tribe, {}).get("description", "You are unique and don't fit into a single tribe!")

    graph = build_graph()
    related_tribes = graph.get(best_tribe, []) if best_tribe in graph else []

    return best_tribe, description, scores, related_tribes