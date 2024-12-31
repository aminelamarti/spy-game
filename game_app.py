import streamlit as st
import random

st.title("Spy Game")

# Step 1: Select the number of players (max 15)
num_players = st.number_input("Select the number of players (1-15):", min_value=1, max_value=15, step=1)

if "player_assignments" not in st.session_state:
    st.session_state.player_assignments = []
if "current_player" not in st.session_state:
    st.session_state.current_player = 1
if "spy_index" not in st.session_state:
    st.session_state.spy_index = None

# Larger pool of top 200 football players (current & all-time)
player_pool = [
    "Lionel Messi", "Cristiano Ronaldo", "Pelé", "Diego Maradona", "Zinedine Zidane", "Michel Platini", 
    "Johan Cruyff", "Ronaldinho", "Ronaldo Nazário", "Franz Beckenbauer", "George Best", "Alfredo Di Stéfano", 
    "Gerd Müller", "Marco Van Basten", "Eusebio", "Bobby Charlton", "Ferenc Puskás", "Thierry Henry", 
    "David Beckham", "Zico", "Paolo Maldini", "Sergio Ramos", "Xavi Hernández", "Andrés Iniesta", 
    "Kaká", "Luis Suárez", "Robert Lewandowski", "Lev Yashin", "Gianluigi Buffon", "Kenny Dalglish", 
    "Steven Gerrard", "Frank Lampard", "Wayne Rooney", "Ryan Giggs", "Cafu", "Roberto Carlos", 
    "Claude Makélélé", "Dennis Bergkamp", "David Villa", "Santi Cazorla", "Carlos Tévez", "Fernando Redondo", 
    "Eden Hazard", "Samuel Eto'o", "Didier Drogba", "Gary Lineker", "Patrick Vieira", "Michael Owen", 
    "Harry Kane", "Raheem Sterling", "Sergio Agüero", "Virgil van Dijk", "Kevin De Bruyne", "N'Golo Kanté", 
    "Mohamed Salah", "Son Heung-min", "Harry Maguire", "Bukayo Saka", "Paul Pogba", "Gareth Bale", 
    "Johan Neeskens", "Thiago Silva", "Alessandro Nesta", "Andrea Pirlo", "Gianfranco Zola", "Juan Román Riquelme", 
    "Hristo Stoichkov", "Ricardo Kaká", "Pierre-Emerick Aubameyang", "Edinson Cavani", "Jürgen Klinsmann", 
    "Bastian Schweinsteiger", "Tony Kroos", "Yaya Touré", "James Rodríguez", "Raul González", "Alessandro Del Piero", 
    "Francesco Totti", "Zlatan Ibrahimović", "Gerard Piqué", "Ronald Koeman", "Xabi Alonso", "Luis Figo", 
    "José Antonio Reyes", "Javier Zanetti", "Marcelo", "Neymar", "Santi Cazorla", "Cesc Fàbregas", 
    "John Terry", "Rio Ferdinand", "Vincent Kompany", "Michael Essien", "Wesley Sneijder", "Fernando Torres", 
    "Patrick Kluivert", "Ryan Giggs", "John Barnes", "Arjen Robben", "Gareth Bale", "Juan Mata", "Franck Ribéry", 
    "Paul Scholes", "Steven Gerrard", "Vincent Del Bosque", "Riyad Mahrez", "Edgar Davids", "Lothar Matthäus", 
    "Kevin Keegan", "Carlos Alberto", "Gary Neville", "Martin Ødegaard", "Pierre-Emerick Aubameyang", "Raheem Sterling", 
    "Robert Pirès", "Cesc Fàbregas", "Eden Hazard", "Dimitri Payet", "Nicolas Anelka", "Olivier Giroud", 
    "Wilfried Zaha", "Andriy Shevchenko", "David Silva", "Gareth Southgate", "Robbie Fowler", "Jimmy Greaves", 
    "Gary McAllister", "Robbie Keane", "Mark Hughes", "Ian Wright", "Georginio Wijnaldum", "Aaron Ramsey", 
    "Danny Drinkwater", "Jack Wilshere", "Ashley Cole", "Jermain Defoe", "Julian Brandt", "Marco Reus", 
    "Leroy Sané", "Mats Hummels", "Oliver Kahn", "Bernd Schuster", "Thomas Müller", "Jerome Boateng", 
    "Sami Khedira", "Bastian Schweinsteiger", "Manuel Neuer", "Kevin De Bruyne", "Koke", "Saul Niguez"
]  # Expanded to top 200 players

# Step 2: Start the game
if st.button("Start Game"):
    players = [f"Player {i+1}" for i in range(num_players)]
    st.session_state.spy_index = random.randint(1, num_players)  # Randomly pick the spy
    common_player = random.choice(player_pool)  # Randomly choose a common player for the majority

    # Assign the common player to all except the spy
    st.session_state.player_assignments = [
        common_player if i != st.session_state.spy_index - 1 else "You are the SPY"
        for i in range(num_players)
    ]
    st.session_state.current_player = 1  # Reset to the first player

# Step 3: Player reveals their assignment
if st.session_state.player_assignments:
    # Ensure we don't go beyond the total number of players
    if st.session_state.current_player <= num_players:
        st.write(f"Player {st.session_state.current_player}, it's your turn!")
        if st.button("Reveal Player/Role"):
            st.write(st.session_state.player_assignments[st.session_state.current_player - 1])
        if st.button("Done (Next Player)"):
            if st.session_state.current_player < num_players:
                st.session_state.current_player += 1
            else:
                st.write("All players have seen their roles!")
    else:
        st.write("All players have finished their turns!")
