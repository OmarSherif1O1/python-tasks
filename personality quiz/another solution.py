# Initialize scores
scores = {"Thinker": 0, "Social_Butterfly": 0, "Explorer": 0, "Relaxer": 0}

# Define mappings for questions to personality types
answers_to_types = {
    "q1": {1: "Thinker", 2: "Social_Butterfly", 3: "Explorer", 4: "Relaxer"},
    "q2": {1: "Relaxer", 2: "Social_Butterfly", 3: "Explorer", 4: "Thinker"},
    "q3": {1: "Thinker", 2: "Social_Butterfly", 3: "Explorer", 4: "Relaxer"},
}

# Ask questions and update scores
questions = [
    "Q1 -> What’s your favorite way to spend a weekend? \n 1: Reading or watching movies \n 2: Going out with friends \n 3: Exploring new places \n 4: Relaxing at home \n",
    "Q2 -> What’s your favorite kind of vacation? \n 1: Beach getaway \n 2: City tour \n 3: Adventure trip \n 4: Staycation \n",
    "Q3 -> How do you usually make decisions? \n 1: By analyzing every detail \n 2: Based on advice from others \n 3: Trusting your instincts \n 4: Going with the flow \n",
]

for i, question in enumerate(questions, start=1):
    answer = int(input(question))
    scores[answers_to_types[f"q{i}"][answer]] += 1

# Determine personality type
max_score = max(scores.values())
top_types = [ptype for ptype, score in scores.items() if score == max_score]

# Print result
if len(top_types) == 1:
    personality = top_types[0]
    descriptions = {
        "Thinker": "- You are a Thinker \n- You’re introspective and thoughtful. You enjoy deep conversations and value alone time.",
        "Social_Butterfly": "- You are a Social Butterfly \n- You’re outgoing and thrive in social situations. You’re the life of the party!",
        "Explorer": "- You are an Explorer \n- You’re adventurous and curious. You love trying new things and exploring new places.",
        "Relaxer": "- You are a Relaxer \n- You’re easygoing and love your downtime. You know how to unwind and take life as it comes.",
    }
    print(descriptions[personality])
else:
    print("- It seems you have a balanced personality! You enjoy a mix of introspection, adventure, socializing, and relaxation.")
